#!/usr/bin/env python3
"""
Sitemap generator for VidyaSetu GitHub Pages deployment.
"""

import datetime
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
OPPORTUNITIES_FILE = ROOT_DIR / "data" / "opportunities.json"
SITEMAP_FILE = ROOT_DIR / "sitemap.xml"

BASE_URL = "https://mdsamhussain1996.github.io/vidyasetu-scholarship-portal"

def generate_sitemap():
    with open(OPPORTUNITIES_FILE, "r", encoding="utf-8") as f:
        items = json.load(f)

    today = datetime.date.today().isoformat()
    
    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        f'    <loc>{BASE_URL}/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>daily</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/#/providers</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.8</priority>',
        '  </url>'
    ]

    # Add each opportunity link
    for it in items:
        opp_id = it.get("id")
        last_mod = it.get("lastVerified", today)
        xml.append('  <url>')
        xml.append(f'    <loc>{BASE_URL}/#/opportunity/{opp_id}</loc>')
        xml.append(f'    <lastmod>{last_mod}</lastmod>')
        xml.append('    <changefreq>weekly</changefreq>')
        xml.append('    <priority>0.7</priority>')
        xml.append('  </url>')

    xml.append('</urlset>')

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(xml))

    print(f"Generated {SITEMAP_FILE.name} with {len(items) + 2} URLs.")

if __name__ == "__main__":
    generate_sitemap()
