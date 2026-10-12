#!/usr/bin/env python3
"""
tests/test_portal.py - Unit tests for VidyaSetu integrity & verification rules.
Can be executed with `pytest` or `python3 -m unittest tests/test_portal.py`.
"""

import datetime
import json
import unittest
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from scripts.discover import (
    maintain_entries,
    find_duplicate_entry,
    check_for_scams,
    is_official_link,
    add_years_safe
)
from scripts.validate import validate_entry

class TestVidyaSetuRules(unittest.TestCase):

    def test_rollover_does_not_touch_last_verified(self):
        """Rollover on recurring schemes must clear openDate/deadline, set expected, and NOT touch lastVerified."""
        sample_item = {
            "id": "test-recurring-scheme",
            "title": "National Merit Fellowship",
            "deadline": "2026-08-01",
            "openDate": "2026-05-01",
            "deadlineText": "Usually May–Aug",
            "recurring": True,
            "status": "open",
            "dateConfidence": "confirmed",
            "lastVerified": "2026-06-15",
            "verifiedBy": "auto",
            "confidence": 0.9
        }
        today_date = "2026-10-12"
        updated_items, count_updated, count_archived = maintain_entries([sample_item], today_date)

        self.assertEqual(count_updated, 1)
        self.assertEqual(count_archived, 0)
        res = updated_items[0]
        # Must clear exact dates
        self.assertIsNone(res["deadline"])
        self.assertIsNone(res["openDate"])
        # Must mark expected
        self.assertEqual(res["dateConfidence"], "expected")
        self.assertEqual(res["status"], "upcoming")
        # CRITICAL: lastVerified must remain untouched (2026-06-15, NOT today!)
        self.assertEqual(res["lastVerified"], "2026-06-15")

    def test_leap_year_rollover_safe(self):
        """Ensure Feb 29 dates roll over safely to Feb 28 on non-leap years without throwing ValueError."""
        leap_day = datetime.date(2024, 2, 29)
        next_year_day = add_years_safe(leap_day, 1)
        self.assertEqual(next_year_day, datetime.date(2025, 2, 28))

    def test_deduplication_fuzzy_matching(self):
        """Same provider + fuzzy title similarity >= 0.85 must detect duplicate."""
        existing = [
            {
                "id": "iit-bombay-project-jrf-nanotech",
                "title": "Project JRF - Nanotechnology for Clean Energy",
                "provider": {"slug": "iit-bombay"}
            }
        ]
        candidate_dup = {
            "title": "Project JRF - Nanotechnology for Clean Energy Devices",
            "provider": {"slug": "iit-bombay"}
        }
        candidate_diff = {
            "title": "Project Associate - Concrete Civil Structures",
            "provider": {"slug": "iit-bombay"}
        }
        candidate_other_provider = {
            "title": "Project JRF - Nanotechnology for Clean Energy",
            "provider": {"slug": "iit-delhi"}
        }

        is_dup, match, _ = find_duplicate_entry(candidate_dup, existing, threshold=0.85)
        self.assertTrue(is_dup)
        self.assertEqual(match["id"], "iit-bombay-project-jrf-nanotech")

        is_dup2, _, _ = find_duplicate_entry(candidate_diff, existing, threshold=0.85)
        self.assertFalse(is_dup2)

        is_dup3, _, _ = find_duplicate_entry(candidate_other_provider, existing, threshold=0.85)
        self.assertFalse(is_dup3)

    def test_scam_flagging(self):
        """Scam keywords or free-mail contact addresses must be flagged for review."""
        legit_entry = {
            "title": "AICTE Pragati Scholarship for Girls",
            "eligibility": "Admitted to 1st year degree programme via centralized counselling.",
            "applicationProcess": ["Register on NSP portal with Aadhaar card."],
            "documentsRequired": ["Income certificate", "College fee receipt"]
        }
        is_scam, _ = check_for_scams(legit_entry)
        self.assertFalse(is_scam)

        fee_scam = {
            "title": "Direct Prime Minister Relief Grant",
            "eligibility": "Open to all students who pay registration fee of Rs 500.",
            "applicationProcess": [],
            "documentsRequired": []
        }
        is_scam_fee, reason_fee = check_for_scams(fee_scam)
        self.assertTrue(is_scam_fee)
        self.assertIn("registration fee", reason_fee)

        email_scam = {
            "title": "International Research Fellowship 2026",
            "eligibility": "Send your bio-data to prof_scholarship@gmail.com for guaranteed selection.",
            "applicationProcess": [],
            "documentsRequired": []
        }
        is_scam_email, reason_email = check_for_scams(email_scam)
        self.assertTrue(is_scam_email)

    def test_official_link_and_aggregator_prohibition(self):
        """Aggregator domains must be rejected as official links; official portals allowed."""
        self.assertTrue(is_official_link("https://scholarships.gov.in"))
        self.assertTrue(is_official_link("https://www.chevening.org/scholarship/india/"))
        self.assertTrue(is_official_link("https://www.iitb.ac.in/careers"))

        # Disallowed aggregators
        self.assertFalse(is_official_link("https://www.buddy4study.com/scholarship/some-scheme"))
        self.assertFalse(is_official_link("https://scholarships.net.in/1234.html"))
        self.assertFalse(is_official_link("http://scholarships.gov.in")) # HTTP rejected

    def test_link_quality_warnings(self):
        """validate_entry must warn when officialLink is homepage or equals provider.website."""
        sample_valid = {
            "id": "sample-valid-entry",
            "title": "Sample Valid Scheme For Higher Studies",
            "section": "india",
            "country": "India",
            "type": "government",
            "category": "Scholarship",
            "educationLevel": ["Bachelor"],
            "streams": ["All"],
            "targetGroup": ["All"],
            "fundingAmount": "₹50,000/year",
            "amountValINR": 50000,
            "provider": {
                "name": "Department of Science and Technology",
                "kind": "ministry",
                "slug": "dst-india",
                "website": "https://dst.gov.in"
            },
            "eligibility": "Top 1% in 12th board exams",
            "openDate": None,
            "deadline": None,
            "deadlineText": "Usually Oct–Dec",
            "recurring": True,
            "status": "upcoming",
            "officialLink": "https://online-inspire.gov.in/Content/GuidelineSHE",
            "guidelinesLink": "https://online-inspire.gov.in/Content/GuidelineSHE",
            "sourceUrl": "https://online-inspire.gov.in/Content/GuidelineSHE",
            "documentsRequired": ["Marksheet"],
            "applicationProcess": ["Apply online"],
            "tags": ["Inspire"],
            "firstSeen": "2026-10-12",
            "lastVerified": None,
            "verifiedBy": "auto",
            "confidence": 0.5,
            "dateConfidence": "expected"
        }
        errs, warns = validate_entry(sample_valid, 0, set())
        self.assertEqual(len(errs), 0)
        self.assertEqual(len(warns), 0)

        # Now test with empty path (homepage)
        sample_warn = dict(sample_valid)
        sample_warn["id"] = "sample-warn-entry"
        sample_warn["officialLink"] = "https://dst.gov.in"
        errs2, warns2 = validate_entry(sample_warn, 1, set())
        self.assertEqual(len(errs2), 0)
        self.assertTrue(any("empty path" in w or "equals provider.website" in w for w in warns2))

if __name__ == "__main__":
    unittest.main()
