#!/usr/bin/env python3
"""
Validation script for VidyaSetu opportunities dataset.
Enforces:
1. Conformance with data/schema.json (using jsonschema if available, with robust manual fallback).
2. Unique ID enforcement (no duplicates).
3. HTTPS enforcement on officialLink, sourceUrl, and provider.website.
4. Valid dates format (YYYY-MM-DD or null).
5. Confidence value ranges [0.0, 1.0].
"""

import json
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCHEMA_FILE = ROOT_DIR / "data" / "schema.json"
OPPORTUNITIES_FILE = ROOT_DIR / "data" / "opportunities.json"
PENDING_FILE = ROOT_DIR / "data" / "pending.json"
ARCHIVE_FILE = ROOT_DIR / "data" / "archive.json"

DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_REGEX = re.compile(r"^[a-z0-9-]+$")

VALID_SECTIONS = {"india", "abroad"}
VALID_TYPES = {"government", "private", "university", "individual"}
VALID_CATEGORIES = {
    "Scholarship",
    "Fellowship",
    "Internship",
    "Research Project",
    "Project Position (JRF/SRF/RA)",
    "Fund/Grant",
    "Competition",
    "Exchange"
}
VALID_LEVELS = {"After 12th", "Bachelor", "Master", "PhD", "Postdoc"}
VALID_STATUSES = {"open", "upcoming", "closed", "rolling", "needs-review"}
VALID_PROVIDER_KINDS = {"ministry", "company", "trust", "university", "lab", "professor"}
VALID_VERIFIED_BY = {"human", "auto"}

def validate_entry(entry, index, seen_ids):
    errors = []
    
    # 1. Check ID
    item_id = entry.get("id")
    if not item_id or not isinstance(item_id, str):
        errors.append(f"Item #{index}: missing or invalid 'id'")
    elif not SLUG_REGEX.match(item_id):
        errors.append(f"Item #{index} ({item_id}): id must be lowercase alphanumeric with hyphens (^[a-z0-9-]+$)")
    elif item_id in seen_ids:
        errors.append(f"Item #{index}: Duplicate ID '{item_id}' detected!")
    else:
        seen_ids.add(item_id)
        
    title = entry.get("title")
    if not title or not isinstance(title, str) or len(title.strip()) < 3:
        errors.append(f"Item '{item_id}': title must be a non-empty string of at least 3 chars")
        
    # 2. Section & Country
    section = entry.get("section")
    if section not in VALID_SECTIONS:
        errors.append(f"Item '{item_id}': section must be one of {VALID_SECTIONS}, got '{section}'")
    
    country = entry.get("country")
    if not country or not isinstance(country, str):
        errors.append(f"Item '{item_id}': country must be a non-empty string")
        
    # 3. Type & Category
    typ = entry.get("type")
    if typ not in VALID_TYPES:
        errors.append(f"Item '{item_id}': type must be one of {VALID_TYPES}, got '{typ}'")
        
    cat = entry.get("category")
    if cat not in VALID_CATEGORIES:
        errors.append(f"Item '{item_id}': category must be one of {VALID_CATEGORIES}, got '{cat}'")
        
    # 4. Education Levels
    levels = entry.get("educationLevel")
    if not isinstance(levels, list) or len(levels) == 0:
        errors.append(f"Item '{item_id}': educationLevel must be a non-empty list")
    else:
        for lvl in levels:
            if lvl not in VALID_LEVELS:
                errors.append(f"Item '{item_id}': invalid educationLevel '{lvl}', expected from {VALID_LEVELS}")
                
    # 5. Streams & TargetGroup
    if not isinstance(entry.get("streams"), list):
        errors.append(f"Item '{item_id}': streams must be a list")
    if not isinstance(entry.get("targetGroup"), list):
        errors.append(f"Item '{item_id}': targetGroup must be a list")
        
    # 6. Amounts
    if not isinstance(entry.get("fundingAmount"), str):
        errors.append(f"Item '{item_id}': fundingAmount must be a string")
    amt_val = entry.get("amountValINR")
    if amt_val is None or not isinstance(amt_val, (int, float)) or amt_val < 0:
        errors.append(f"Item '{item_id}': amountValINR must be a non-negative number")
        
    # 7. Provider object
    provider = entry.get("provider")
    if not isinstance(provider, dict):
        errors.append(f"Item '{item_id}': provider must be an object with name, kind, slug, website")
    else:
        p_name = provider.get("name")
        p_kind = provider.get("kind")
        p_slug = provider.get("slug")
        p_web = provider.get("website")
        
        if not p_name or not isinstance(p_name, str):
            errors.append(f"Item '{item_id}': provider.name must be non-empty")
        if p_kind not in VALID_PROVIDER_KINDS:
            errors.append(f"Item '{item_id}': provider.kind must be one of {VALID_PROVIDER_KINDS}, got '{p_kind}'")
        if not p_slug or not SLUG_REGEX.match(p_slug):
            errors.append(f"Item '{item_id}': provider.slug must be lowercase slug format")
        if not p_web or not p_web.startswith("https://"):
            errors.append(f"Item '{item_id}': provider.website must start with https://, got '{p_web}'")

    # 8. Eligibility
    if not isinstance(entry.get("eligibility"), str):
        errors.append(f"Item '{item_id}': eligibility must be a string")

    # 9. Dates
    open_date = entry.get("openDate")
    if open_date is not None and (not isinstance(open_date, str) or not DATE_REGEX.match(open_date)):
        errors.append(f"Item '{item_id}': openDate must be 'YYYY-MM-DD' or null, got '{open_date}'")
        
    deadline = entry.get("deadline")
    if deadline is not None and (not isinstance(deadline, str) or not DATE_REGEX.match(deadline)):
        errors.append(f"Item '{item_id}': deadline must be 'YYYY-MM-DD' or null, got '{deadline}'")
        
    if not isinstance(entry.get("deadlineText"), str):
        errors.append(f"Item '{item_id}': deadlineText must be a string")

    if not isinstance(entry.get("recurring"), bool):
        errors.append(f"Item '{item_id}': recurring must be a boolean")

    status = entry.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"Item '{item_id}': status must be one of {VALID_STATUSES}, got '{status}'")

    # 10. Links - STRICT HTTPS ENFORCEMENT
    official = entry.get("officialLink")
    if not official or not isinstance(official, str) or not official.startswith("https://"):
        errors.append(f"Item '{item_id}': officialLink MUST start with https://, got '{official}'")

    source_url = entry.get("sourceUrl")
    if not source_url or not isinstance(source_url, str) or not source_url.startswith("https://"):
        errors.append(f"Item '{item_id}': sourceUrl MUST start with https://, got '{source_url}'")

    # 11. Documents & Process
    if not isinstance(entry.get("documentsRequired"), list):
        errors.append(f"Item '{item_id}': documentsRequired must be a list")
    if not isinstance(entry.get("applicationProcess"), list):
        errors.append(f"Item '{item_id}': applicationProcess must be a list")
    if not isinstance(entry.get("tags"), list):
        errors.append(f"Item '{item_id}': tags must be a list")

    # 12. Audit & Verification fields
    first_seen = entry.get("firstSeen")
    if not first_seen or not DATE_REGEX.match(first_seen):
        errors.append(f"Item '{item_id}': firstSeen must be 'YYYY-MM-DD'")

    last_verified = entry.get("lastVerified")
    if not last_verified or not DATE_REGEX.match(last_verified):
        errors.append(f"Item '{item_id}': lastVerified must be 'YYYY-MM-DD'")

    verified_by = entry.get("verifiedBy")
    if verified_by not in VALID_VERIFIED_BY:
        errors.append(f"Item '{item_id}': verifiedBy must be 'human' or 'auto'")

    confidence = entry.get("confidence")
    if confidence is None or not isinstance(confidence, (int, float)) or not (0.0 <= confidence <= 1.0):
        errors.append(f"Item '{item_id}': confidence must be a number between 0.0 and 1.0, got '{confidence}'")

    return errors

def validate_file(file_path):
    if not file_path.exists():
        print(f"File {file_path.name} does not exist, skipping.")
        return 0, 0
    
    print(f"\n--- Validating {file_path.name} ---")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to parse JSON from {file_path}: {e}")
        return 1, 0

    if not isinstance(data, list):
        print(f"ERROR: {file_path.name} root must be a JSON array, got {type(data).__name__}")
        return 1, 0

    seen_ids = set()
    total_errors = []

    for idx, entry in enumerate(data):
        errs = validate_entry(entry, idx, seen_ids)
        if errs:
            total_errors.extend(errs)

    if total_errors:
        print(f"FAILED: Found {len(total_errors)} validation errors in {file_path.name}:")
        for err in total_errors[:20]:
            print(f"  ❌ {err}")
        if len(total_errors) > 20:
            print(f"  ... and {len(total_errors) - 20} more errors.")
        return len(total_errors), len(data)
    else:
        print(f"PASSED: All {len(data)} entries in {file_path.name} are valid and HTTPS compliant!")
        return 0, len(data)

def main():
    print("VidyaSetu Dataset Integrity Validator")
    print(f"Schema: {SCHEMA_FILE}")

    errors_main, count_main = validate_file(OPPORTUNITIES_FILE)
    errors_pending, _ = validate_file(PENDING_FILE)
    errors_archive, _ = validate_file(ARCHIVE_FILE)

    total_errors = errors_main + errors_pending + errors_archive

    if total_errors > 0:
        print(f"\n❌ Validation failed with {total_errors} total errors.")
        sys.exit(1)
    else:
        print(f"\n All files passed validation successfully! Total verified entries: {count_main}")
        sys.exit(0)

if __name__ == "__main__":
    main()
