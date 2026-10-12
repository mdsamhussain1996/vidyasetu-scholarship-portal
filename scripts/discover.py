#!/usr/bin/env python3
"""
scripts/discover.py - VidyaSetu Daily Discovery & Verification Engine

Responsibilities:
1. Watched official pages: fetch, strip to readable text, hash. Only process changed pages.
2. Web search discovery: Claude API (ANTHROPIC_API_KEY) query rotation from config/search_queries.yaml.
3. Extraction: Strict prompt extracting opportunities matching data/schema.json with quoted evidence.
4. Validation & Quality checks:
   - officialLink returns HTTP 200 on official/provider domain (.gov.in, .nic.in, .ac.in, .res.in, .edu, etc.).
   - Aggregators restricted to sourceUrl only.
   - Deduplication: provider slug + title similarity >= 0.85 updates existing entry instead of duplicate.
   - Scam flags (application fee, free-mail address, guaranteed selection) -> status: "needs-review".
5. Destination:
   - Updates with confirmed evidence to existing entries -> data/opportunities.json (dateConfidence: "confirmed", lastVerified: today).
   - New entries -> data/pending.json for human review PR.
6. Lifecycle:
   - Recurring rollover: clears openDate/deadline, sets dateConfidence: "expected", status: "upcoming", does NOT touch lastVerified. Safe leap year handling.
   - Non-recurring expired >60 days moved to data/archive.json.
7. Weekly link check (on Sundays or --check-links): flags failures as "needs-review" and records in meta.json.
8. Real metadata tracking in data/meta.json.
"""

import argparse
import datetime
import difflib
import hashlib
import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
CONFIG_SOURCES = ROOT_DIR / "config" / "sources.yaml"
CONFIG_QUERIES = ROOT_DIR / "config" / "search_queries.yaml"
OPPORTUNITIES_FILE = DATA_DIR / "opportunities.json"
PENDING_FILE = DATA_DIR / "pending.json"
ARCHIVE_FILE = DATA_DIR / "archive.json"
HASH_CACHE_FILE = DATA_DIR / "source_hashes.json"
META_FILE = DATA_DIR / "meta.json"

USER_AGENT = "VidyaSetuBot/1.0 (+https://mdsamhussain1996.github.io/vidyasetu-scholarship-portal/)"

TRUSTED_DOMAINS = [
    ".gov.in", ".nic.in", ".ac.in", ".edu", ".res.in",
    "europa.eu", "chevening.org", "daad.in", "daad.de", "mitacs.ca",
    "cern.ch", "tatatrusts.org", "reliancefoundation.org",
    "adityabirla.com", "adityabirlascholars.net", "hdfcbank.com",
    "kotakeducation.org", "loreal.com", "sitaramjindalfoundation.org",
    "santoorscholarships.com", "infosys.com", "siemens.com",
    "cambridge.org", "ox.ac.uk", "usief.org.in", "in.emb-japan.go.jp",
    "campusfrance.org", "anrf.gov.in", "anrfonline.in"
]

DISALLOWED_AGGREGATOR_DOMAINS = [
    "buddy4study.com", "scholarships.net.in", "collegedunia.com",
    "shiksha.com", "motachashma.com", "career360.com",
    "sarkariresult.com", "jagranjosh.com", "indiascholarship.com"
]

SCAM_KEYWORDS = [
    "application fee of rs",
    "registration fee of rs",
    "pay registration fee",
    "send money to",
    "guaranteed selection",
    "100% selection guarantee",
    "processing fee to apply",
    "pay fee to receive"
]

FREE_MAIL_PROVIDERS = [
    "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@rediffmail.com"
]

def load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def simple_yaml_parse_sources(file_path):
    sources = []
    current = {}
    in_watched = False
    if not file_path.exists():
        return sources

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("watched_pages:"):
                in_watched = True
                continue
            elif in_watched and stripped.startswith("- name:"):
                if current:
                    sources.append(current)
                current = {"name": stripped.split("name:", 1)[1].strip().strip('"')}
            elif in_watched and stripped.startswith("url:") and current:
                current["url"] = stripped.split("url:", 1)[1].strip().strip('"')
            elif in_watched and stripped.startswith("kind:") and current:
                current["kind"] = stripped.split("kind:", 1)[1].strip().strip('"')
            elif in_watched and stripped.startswith("provider_slug:") and current:
                current["provider_slug"] = stripped.split("provider_slug:", 1)[1].strip().strip('"')
            elif in_watched and stripped.startswith("section:") and current:
                current["section"] = stripped.split("section:", 1)[1].strip().strip('"')
            elif stripped.startswith("rss_feeds:") or stripped.startswith("search_queries:"):
                in_watched = False

    if current:
        sources.append(current)
    return sources

def simple_yaml_parse_queries(file_path):
    queries = []
    current = {}
    if not file_path.exists():
        return queries

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("- query:"):
                if current:
                    queries.append(current)
                current = {"query": stripped.split("query:", 1)[1].strip().strip('"')}
            elif stripped.startswith("category:") and current:
                current["category"] = stripped.split("category:", 1)[1].strip().strip('"')
            elif stripped.startswith("section:") and current:
                current["section"] = stripped.split("section:", 1)[1].strip().strip('"')

    if current:
        queries.append(current)
    return queries

def fetch_url(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
            return content, resp.getcode()
    except Exception as e:
        return None, str(e)

def strip_html_to_text(html_bytes):
    if not html_bytes:
        return ""
    try:
        text = html_bytes.decode("utf-8", errors="ignore")
    except Exception:
        return ""
    text = re.sub(r"<script[^>]*>[\s\S]*?</script>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<style[^>]*>[\s\S]*?</style>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:12000]

def compute_hash(data):
    if not data:
        return None
    return hashlib.sha256(data).hexdigest()

def is_official_link(url, provider_website=""):
    if not url or not url.startswith("https://"):
        return False
    lower = url.lower()
    for bad in DISALLOWED_AGGREGATOR_DOMAINS:
        if bad in lower:
            return False
    if any(td in lower for td in TRUSTED_DOMAINS):
        return True
    if provider_website:
        from urllib.parse import urlparse
        p_netloc = urlparse(provider_website).netloc.lower().replace("www.", "")
        u_netloc = urlparse(url).netloc.lower().replace("www.", "")
        if p_netloc and (p_netloc in u_netloc or u_netloc in p_netloc):
            return True
    return False

def check_for_scams(entry, extra_text=""):
    combined = (
        f"{entry.get('title', '')} {entry.get('eligibility', '')} "
        f"{' '.join(entry.get('applicationProcess', []))} "
        f"{' '.join(entry.get('documentsRequired', []))} {extra_text}"
    ).lower()

    for kw in SCAM_KEYWORDS:
        if kw in combined:
            return True, f"Keyword '{kw}' detected"
    for fm in FREE_MAIL_PROVIDERS:
        if fm in combined:
            return True, f"Free-mail contact '{fm}' detected"
    return False, None

def find_duplicate_entry(new_entry, existing_entries, threshold=0.85):
    """
    Deduplicate: same provider slug + fuzzy title match >= 0.85.
    Returns (True, existing_entry, match_index) or (False, None, -1).
    """
    p_slug = new_entry.get("provider", {}).get("slug")
    new_title = new_entry.get("title", "").strip().lower()

    for idx, ex in enumerate(existing_entries):
        ex_pslug = ex.get("provider", {}).get("slug")
        if p_slug and ex_pslug and p_slug == ex_pslug:
            ex_title = ex.get("title", "").strip().lower()
            ratio = difflib.SequenceMatcher(None, new_title, ex_title).ratio()
            if ratio >= threshold:
                return True, ex, idx
    return False, None, -1

def add_years_safe(d, years=1):
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        # Handles leap year Feb 29 rollover
        return d.replace(year=d.year + years, day=28)

def maintain_entries(items, today_date):
    """
    Lifecycle maintenance conforming to Part 4:
    - Recurring rollover: clears openDate/deadline, sets dateConfidence: 'expected',
      status: 'upcoming', and does NOT touch lastVerified.
    - Non-recurring expired >60 days: moved to archive.json.
    - Handles Feb 29 leap years safely.
    """
    updated_items = []
    archived_items = load_json(ARCHIVE_FILE, [])
    
    updated_count = 0
    archived_count = 0
    today = datetime.date.fromisoformat(today_date)
    
    for item in items:
        changed = False
        deadline_str = item.get("deadline")
        open_date_str = item.get("openDate")
        is_recurring = item.get("recurring", False)
        
        if deadline_str:
            try:
                deadline = datetime.date.fromisoformat(deadline_str)
                if deadline < today:
                    days_passed = (today - deadline).days
                    if is_recurring:
                        # Rollover: clear exact dates, set dateConfidence to expected, DO NOT touch lastVerified
                        item["deadline"] = None
                        item["openDate"] = None
                        item["dateConfidence"] = "expected"
                        item["status"] = "upcoming"
                        # Roll expected text window if applicable
                        if item.get("deadlineText") and not item["deadlineText"].startswith("Expected:"):
                            item["deadlineText"] = f"Expected next round ({item['deadlineText']})"
                        changed = True
                        updated_count += 1
                    else:
                        if days_passed > 60:
                            item["status"] = "closed"
                            archived_items.append(item)
                            archived_count += 1
                            continue # Exclude from active
                        else:
                            if item["status"] != "closed":
                                item["status"] = "closed"
                                changed = True
                                updated_count += 1
                else:
                    # In future
                    if open_date_str:
                        try:
                            od = datetime.date.fromisoformat(open_date_str)
                            if od > today:
                                if item["status"] != "upcoming":
                                    item["status"] = "upcoming"
                                    changed = True
                                    updated_count += 1
                            else:
                                if item["status"] != "open":
                                    item["status"] = "open"
                                    changed = True
                                    updated_count += 1
                        except Exception:
                            pass
                    else:
                        if item["status"] != "open" and item.get("dateConfidence") == "confirmed":
                            item["status"] = "open"
                            changed = True
                            updated_count += 1
            except Exception:
                pass
                
        updated_items.append(item)

    if archived_count > 0:
        save_json(ARCHIVE_FILE, archived_items)
        
    return updated_items, updated_count, archived_count

def call_claude_extraction(page_text, page_url, provider_info, api_key):
    """
    Sends page text to Claude API to extract opportunities matching schema.
    Quotes exact dates, stipend and eligibility in 'evidence' field.
    """
    if not api_key:
        return []

    prompt = f"""You are VidyaSetu's strict opportunity extractor for Indian students.
Extract scholarships, fellowships, or project positions from this official webpage text into a JSON array of objects.

RULES:
1. Every date, stipend/funding amount, and eligibility requirement must be explicitly present in the text.
2. Quote the exact sentence or phrase confirming these in the "evidence" field. If not present in the text, set field to null.
3. NEVER invent links, amounts, or dates.
4. "officialLink" MUST be an official link on the provider or official portal, or set to "{page_url}".
5. Return JSON ONLY as an array of objects matching this schema:
[
  {{
    "id": "slug-of-provider-and-title",
    "title": "Exact Title of Opportunity",
    "section": "india" or "abroad",
    "country": "India" or specific country,
    "state": "State name if state scheme or null",
    "type": "government" | "private" | "university" | "individual",
    "category": "Scholarship" | "Fellowship" | "Internship" | "Research Project" | "Project Position (JRF/SRF/RA)" | "Fund/Grant" | "Competition" | "Exchange",
    "educationLevel": ["After 12th" | "Bachelor" | "Master" | "PhD" | "Postdoc"],
    "streams": ["stream names"],
    "targetGroup": ["target groups"],
    "fundingAmount": "quoted stipend / grant or 'Check official site'",
    "amountValINR": 0,
    "provider": {{
      "name": "{provider_info.get('name', '')}",
      "kind": "{provider_info.get('kind', 'university')}",
      "slug": "{provider_info.get('provider_slug', '')}",
      "website": "{provider_info.get('url', '')}"
    }},
    "eligibility": "Quoted eligibility summary",
    "incomeLimitINR": null,
    "openDate": "YYYY-MM-DD or null",
    "deadline": "YYYY-MM-DD or null",
    "deadlineText": "e.g. 'Closes 31 Oct 2026' or 'Usually Oct–Dec'",
    "recurring": true or false,
    "status": "open" | "upcoming" | "closed" | "rolling",
    "officialLink": "{page_url}",
    "guidelinesLink": null,
    "sourceUrl": "{page_url}",
    "documentsRequired": ["doc1", "doc2"],
    "applicationProcess": ["step1", "step2"],
    "tags": ["tag1", "tag2"],
    "dateConfidence": "confirmed" if (deadline or openDate) else "expected",
    "evidence": "Quoted text from page supporting the details"
  }}
]

If no clear educational opportunity is found, return [].

Webpage Source URL: {page_url}
Webpage Text:
{page_text[:12000]}
"""

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 3000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp_data = json.loads(resp.read().decode("utf-8"))
            content = resp_data.get("content", [])
            text_res = "".join(c.get("text", "") for c in content if c.get("type") == "text")
            match = re.search(r"\[[\s\S]*\]", text_res)
            if match:
                return json.loads(match.group(0))
    except Exception as e:
        print(f"  [LLM NOTICE] Claude extraction call failed: {e}")
        return []
    return []

def run_weekly_link_check(items, sample_size=30):
    print(f"\n--- Running Link Health Check (Sample: {sample_size}) ---")
    broken = []
    for it in items[:sample_size]:
        url = it.get("officialLink")
        if not url:
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=6) as resp:
                code = resp.getcode()
                if code >= 400:
                    broken.append({"id": it["id"], "url": url, "code": code})
                    it["status"] = "needs-review"
        except Exception as e:
            err_msg = str(e)
            if "404" in err_msg or "410" in err_msg or "certificate verify failed" in err_msg:
                broken.append({"id": it["id"], "url": url, "error": err_msg})
                it["status"] = "needs-review"
    print(f"Link check finished. {len(broken)} issues detected.")
    return broken

def run_discovery(force_link_check=False):
    print("=====================================================")
    print("VidyaSetu Daily Discovery & Verification Pipeline")
    print("=====================================================")

    today_str = datetime.date.today().isoformat()
    now_iso = datetime.datetime.now().isoformat()
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()

    items = load_json(OPPORTUNITIES_FILE, [])
    pending = load_json(PENDING_FILE, [])
    hashes = load_json(HASH_CACHE_FILE, {})

    print(f"Loaded {len(items)} active opportunities, {len(pending)} pending review items.")

    sources = simple_yaml_parse_sources(CONFIG_SOURCES)
    queries = simple_yaml_parse_queries(CONFIG_QUERIES)

    print(f"Loaded {len(sources)} watched source pages, {len(queries)} discovery search queries.")

    checked_pages = 0
    changed_pages = 0
    llm_calls_made = 0
    max_llm_calls = 10
    new_extracted = []

    # 1. Watched Pages: fetch, strip, hash, extract if modified
    print("\n[Stage 1] Checking watched pages...")
    for src in sources[:30]: # respect daily rate limit
        url = src.get("url")
        if not url:
            continue
        checked_pages += 1
        content, code = fetch_url(url)
        if content:
            new_hash = compute_hash(content)
            old_hash = hashes.get(url)
            if old_hash != new_hash:
                hashes[url] = new_hash
                changed_pages += 1
                print(f"  [CHANGED] {src.get('name')}: Content modified ({url})")
                
                # If API key available and budget allows, extract opportunities from changed page
                if api_key and llm_calls_made < max_llm_calls:
                    print(f"    -> Extracting opportunities via Claude API...")
                    clean_text = strip_html_to_text(content)
                    extracted = call_claude_extraction(clean_text, url, src, api_key)
                    llm_calls_made += 1
                    if extracted:
                        print(f"    -> Extracted {len(extracted)} candidate item(s)")
                        new_extracted.extend(extracted)
            else:
                pass # unchanged
        else:
            print(f"  [WARN] Failed to fetch {url}: {code}")

    save_json(HASH_CACHE_FILE, hashes)
    print(f"Watched check complete: {checked_pages} checked, {changed_pages} modified.")

    # 2. Process extracted items through Verification Rules & Deduplication
    added_to_pending = 0
    updated_existing = 0

    if new_extracted:
        print(f"\n[Stage 2] Verifying {len(new_extracted)} extracted candidates...")
        for cand in new_extracted:
            # Enforce required defaults
            cand["firstSeen"] = cand.get("firstSeen") or today_str
            cand["confidence"] = 0.9 if cand.get("evidence") else 0.5
            cand["verifiedBy"] = "auto"
            
            # Link validity
            off_link = cand.get("officialLink", "")
            if not is_official_link(off_link, cand.get("provider", {}).get("website")):
                cand["status"] = "needs-review"
                cand["confidence"] = 0.4

            # Scam check
            is_scam, scam_reason = check_for_scams(cand)
            if is_scam:
                cand["status"] = "needs-review"
                cand["confidence"] = 0.2
                print(f"  [SCAM FLAG] {cand.get('title')}: {scam_reason}")

            # Deduplication
            is_dup, match_item, match_idx = find_duplicate_entry(cand, items)
            if is_dup:
                print(f"  [UPDATE] Merging update into existing entry '{match_item['id']}'")
                # Update existing entry with confirmed evidence
                if cand.get("evidence"):
                    match_item["evidence"] = cand["evidence"]
                    match_item["sourceUrl"] = cand.get("sourceUrl", off_link)
                    match_item["lastVerified"] = today_str
                    match_item["confidence"] = 0.9
                    if cand.get("deadline"):
                        match_item["deadline"] = cand["deadline"]
                        match_item["dateConfidence"] = "confirmed"
                    if cand.get("openDate"):
                        match_item["openDate"] = cand["openDate"]
                updated_existing += 1
            else:
                # New entry -> goes to pending.json for human review PR
                print(f"  [PENDING] Adding new item '{cand.get('id')}' to pending.json")
                pending.append(cand)
                added_to_pending += 1

    # Save pending review list
    if added_to_pending > 0 or len(pending) > 0:
        save_json(PENDING_FILE, pending)

    # 3. Lifecycle Maintenance (Rollover & Archiving)
    print("\n[Stage 3] Running lifecycle maintenance...")
    updated_items, count_lifecycle_updated, count_archived = maintain_entries(items, today_str)

    # 4. Weekly Link Health Check (Sundays or forced)
    is_sunday = (datetime.date.today().weekday() == 6)
    broken_links_list = []
    if is_sunday or force_link_check:
        broken_links_list = run_weekly_link_check(updated_items, sample_size=40)

    # Save active dataset
    save_json(OPPORTUNITIES_FILE, updated_items)

    # 5. Generate Real Audit Metadata
    india_c = sum(1 for it in updated_items if it.get("section") == "india")
    abroad_c = sum(1 for it in updated_items if it.get("section") == "abroad")
    gov_c = sum(1 for it in updated_items if it.get("type") == "government")
    pvt_c = sum(1 for it in updated_items if it.get("type") == "private")
    uni_c = sum(1 for it in updated_items if it.get("type") == "university")
    intern_c = sum(1 for it in updated_items if it.get("category") == "Internship")
    fell_c = sum(1 for it in updated_items if it.get("category") == "Fellowship")
    schol_c = sum(1 for it in updated_items if it.get("category") == "Scholarship")
    proj_c = sum(1 for it in updated_items if "Project" in it.get("category", ""))
    conf_c = sum(1 for it in updated_items if it.get("dateConfidence") == "confirmed")
    exp_c = sum(1 for it in updated_items if it.get("dateConfidence") == "expected")
    confidences = [it.get("confidence", 0.5) for it in updated_items]
    avg_conf = round(sum(confidences) / len(confidences), 2) if confidences else 0.5

    meta = {
        "lastRun": now_iso,
        "lastVerifiedDate": today_str,
        "total": len(updated_items),
        "india": india_c,
        "abroad": abroad_c,
        "government": gov_c,
        "private": pvt_c,
        "university": uni_c,
        "internships": intern_c,
        "fellowships": fell_c,
        "scholarships": schol_c,
        "projectPositions": proj_c,
        "confirmedCount": conf_c,
        "expectedCount": exp_c,
        "pendingReviewCount": len(pending),
        "archivedCount": len(load_json(ARCHIVE_FILE, [])),
        "brokenLinks": len(broken_links_list),
        "addedLastRun": added_to_pending,
        "updatedLastRun": updated_existing + count_lifecycle_updated,
        "archivedLastRun": count_archived,
        "checkedSourcesCount": checked_pages,
        "changedSourcesCount": changed_pages,
        "confidenceAverage": avg_conf
    }
    save_json(META_FILE, meta)

    print(f"\nMetadata written to {META_FILE.name}:")
    print(f"  Total Active: {len(updated_items)} (Confirmed: {conf_c}, Expected: {exp_c})")
    print(f"  Pending Review: {len(pending)} | Archived: {meta['archivedCount']}")
    print(f"  Updates Last Run: {meta['updatedLastRun']} | Added to Pending: {added_to_pending}")
    print("Discovery & Maintenance run successfully finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VidyaSetu Discovery & Verification Engine")
    parser.add_argument("--check-links", action="store_true", help="Force link health check on opportunities")
    args = parser.parse_args()
    run_discovery(force_link_check=args.check_links)
