import json

with open("data/opportunities.json", "r") as f:
    items = json.load(f)

# Fix types
for it in items:
    if it["type"] == "lab":
        it["type"] = "government"
    elif it["type"] == "trust":
        it["type"] = "private"

extra = [
    {
        "id": "iitb-fossee-summer-fellowship",
        "title": "IIT Bombay FOSSEE Summer Fellowship in Open Source & Scientific Computing",
        "section": "india",
        "country": "India",
        "state": "Maharashtra",
        "type": "university",
        "category": "Internship",
        "educationLevel": ["Bachelor", "Master"],
        "streams": ["Computer Science", "Open Source Software", "Civil", "Mechanical", "Electrical", "Chemical Engineering"],
        "targetGroup": ["Students across all Indian engineering and science colleges"],
        "fundingAmount": "₹15,000 to ₹25,000 stipend upon successful contribution + Certificate from IIT Bombay",
        "amountValINR": 25000,
        "provider": {
            "name": "IIT Bombay (FOSSEE - National Mission on Education through ICT)",
            "kind": "university",
            "slug": "iit-bombay",
            "website": "https://fossee.in"
        },
        "eligibility": "Open to all students enrolled in any college in India who complete the screening tasks in open source tools (Python, Scilab, OpenFOAM, DWSIM, eSim, etc.).",
        "incomeLimitINR": None,
        "openDate": "2027-02-01",
        "deadline": "2027-04-10",
        "deadlineText": "Annually opens February with screening tasks closing April",
        "recurring": True,
        "status": "upcoming",
        "officialLink": "https://fossee.in",
        "sourceUrl": "https://fossee.in/fellowship",
        "documentsRequired": ["Student College ID", "GitHub / GitLab repository containing completed screening tasks", "Code walkthrough documentation"],
        "applicationProcess": [
            "Select an open source project module on the FOSSEE portal",
            "Complete and submit the coding task before deadline",
            "Top performers receive full 8-week summer fellowship with IIT Bombay mentors"
        ],
        "tags": ["IIT Bombay", "FOSSEE", "Open Source", "Remote & On-Campus", "NMEICT"],
        "firstSeen": "2026-10-12",
        "lastVerified": "2026-10-12",
        "verifiedBy": "human",
        "confidence": 1.0
    },
    {
        "id": "iitd-sura-internship",
        "title": "IIT Delhi Summer Undergraduate Research Award (SURA)",
        "section=":"india",
        "country": "India",
        "state": "Delhi",
        "type": "university",
        "category": "Internship",
        "educationLevel": ["Bachelor"],
        "streams": ["Engineering", "Computer Science", "Materials Science", "Biochemical", "Mathematics"],
        "targetGroup": ["Undergraduate Engineering Students"],
        "fundingAmount": "₹10,000 summer research stipend + Subsidized campus hostel in New Delhi",
        "amountValINR": 10000,
        "provider": {
            "name": "Indian Institute of Technology Delhi (IIT Delhi)",
            "kind": "university",
            "slug": "iit-delhi",
            "website": "https://home.iitd.ac.in"
        },
        "eligibility": "Undergraduate engineering students with CGPA >= 8.0 interested in advanced hardware or theoretical research.",
        "incomeLimitINR": None,
        "openDate": "2027-02-01",
        "deadline": "2027-03-20",
        "deadlineText": "Annually opens February, closes late March",
        "recurring": True,
        "status": "upcoming",
        "officialLink": "https://home.iitd.ac.in",
        "sourceUrl": "https://home.iitd.ac.in/academics/sura",
        "documentsRequired": ["Resume", "Transcripts", "Letter of Recommendation from HOD", "Statement of Purpose"],
        "applicationProcess": [
            "Submit online application to IIT Delhi SURA committee",
            "Faculty departments shortlist applicants",
            "8-week summer research stay on IIT Delhi campus"
        ],
        "tags": ["IIT Delhi", "SURA", "Undergraduate", "Engineering", "Summer Research"],
        "firstSeen": "2026-10-12",
        "lastVerified": "2026-10-12",
        "verifiedBy": "human",
        "confidence": 1.0
    },
    {
        "id": "tcs-research-scholar-program",
        "title": "TCS Research Scholar Program (TRSP - Doctoral Fellowship)",
        "section": "india",
        "country": "India",
        "state": None,
        "type": "private",
        "category": "Fellowship",
        "educationLevel": ["PhD"],
        "streams": ["Computer Science", "Artificial Intelligence", "Cybersecurity", "Data Analytics", "Software Engineering"],
        "targetGroup": ["Full-time PhD scholars in recognized Indian Universities/Institutes"],
        "fundingAmount": "₹47,000/month (Yr 1-2) -> ₹54,000/month (Yr 3-4) + ₹8,40,000 Research Contingency & Travel Grant",
        "amountValINR": 700000,
        "provider": {
            "name": "Tata Consultancy Services (TCS Research)",
            "kind": "company",
            "slug": "tcs-research",
            "website": "https://www.tcs.com"
        },
        "eligibility": "Full-time enrolled PhD scholars in first 14 months of PhD with first-class throughout schooling and degree. Age <= 28 years.",
        "incomeLimitINR": None,
        "openDate": "2026-07-01",
        "deadline": "2026-09-30",
        "deadlineText": "Annually opens July, closes September",
        "recurring": True,
        "status": "open",
        "officialLink": "https://www.tcs.com",
        "sourceUrl": "https://www.tcs.com/what-we-do/research/academic-collaborations",
        "documentsRequired": ["PhD Research Proposal", "Supervisor & Department Endorsement Form", "Transcripts", "Curriculum Vitae"],
        "applicationProcess": [
            "Institute nominates eligible scholars through designated Dean/HOD",
            "TCS Research committee conducts technical evaluation and interviews",
            "Fellows receive funding for 4 years with international conference sponsorship"
        ],
        "tags": ["TCS", "Doctoral Fellowship", "Computer Science", "High Funding", "Industry Research"],
        "firstSeen": "2026-10-12",
        "lastVerified": "2026-10-12",
        "verifiedBy": "human",
        "confidence": 1.0
    },
    {
        "id": "microsoft-research-india-fellowship",
        "title": "Microsoft Research India PhD Fellowship",
        "section": "india",
        "country": "India",
        "state": "Karnataka",
        "type": "private",
        "category": "Fellowship",
        "educationLevel": ["PhD"],
        "streams": ["Computer Science", "Algorithms", "Machine Learning", "Systems", "Societal Tech"],
        "targetGroup": ["PhD scholars enrolled at Indian institutions"],
        "fundingAmount": "$25,000 USD total grant (stipend support + travel funding) + MSR India Internship",
        "amountValINR": 2100000,
        "provider": {
            "name": "Microsoft Research India",
            "kind": "company",
            "slug": "microsoft-research",
            "website": "https://www.microsoft.com/en-us/research/lab/microsoft-research-india"
        },
        "eligibility": "Enrolled in PhD program at an accredited university in India. High academic record and emerging research publications.",
        "incomeLimitINR": None,
        "openDate": "2026-04-01",
        "deadline": "2026-05-31",
        "deadlineText": "Annually opens April, closes May",
        "recurring": True,
        "status": "closed",
        "officialLink": "https://www.microsoft.com/en-us/research/lab/microsoft-research-india",
        "sourceUrl": "https://www.microsoft.com/en-us/research/academic-programs/phd-fellowship",
        "documentsRequired": ["Research Summary & Proposal", "Curriculum Vitae with publication links", "Letter of Support from PhD Advisor"],
        "applicationProcess": [
            "Submit application on Microsoft Research Fellowships portal",
            "Research scientists at MSR India review proposals and conduct interviews",
            "Awardees receive financial grant and mentorship from MSR researchers"
        ],
        "tags": ["Microsoft Research", "AI & Systems", "PhD Fellowship", "High Prestige"],
        "firstSeen": "2026-10-12",
        "lastVerified": "2026-10-12",
        "verifiedBy": "human",
        "confidence": 1.0
    },
    {
        "id": "barc-student-projects",
        "title": "BARC Student Project Training in Nuclear & Applied Sciences",
        "section": "india",
        "country": "India",
        "state": "Maharashtra",
        "type": "government",
        "category": "Internship",
        "educationLevel": ["Bachelor", "Master"],
        "streams": ["Nuclear Engineering", "Mechanical", "Chemical", "Physics", "Radiochemistry", "Biotechnology"],
        "targetGroup": ["M.Sc, M.Tech, and Final Year B.Tech Students"],
        "fundingAmount": "Access to Advanced Atomic Energy Laboratories + Certified Specialized Training",
        "amountValINR": 0,
        "provider": {
            "name": "Bhabha Atomic Research Centre (BARC), DAE",
            "kind": "lab",
            "slug": "barc-mumbai",
            "website": "https://www.barc.gov.in"
        },
        "eligibility": "Regular students of recognized Indian universities in engineering or science with consistent first-class track record.",
        "incomeLimitINR": None,
        "openDate": "2026-01-01",
        "deadline": "2026-12-31",
        "deadlineText": "Applications accepted throughout the year (Rolling)",
        "recurring": True,
        "status": "rolling",
        "officialLink": "https://www.barc.gov.in",
        "sourceUrl": "https://www.barc.gov.in/careers/student_projects.html",
        "documentsRequired": ["Recommendation letter from Principal/Dean", "Detailed Resume", "Marksheets of all semesters", "Police Verification / Character Certificate"],
        "applicationProcess": [
            "Submit project application endorsed by college principal to Head, HRDD, BARC Trombay",
            "Security verification and divisional scientist allotment",
            "Project duration of 3 to 12 months in Trombay, Mumbai"
        ],
        "tags": ["BARC", "Atomic Energy", "Nuclear Science", "Project Training", "Mumbai"],
        "firstSeen": "2026-10-12",
        "lastVerified": "2026-10-12",
        "verifiedBy": "human",
        "confidence": 1.0
    }
]

# Ensure section field is present in extra items
for ex in extra:
    ex["section"] = "india"

items.extend(extra)

print(f"Final total items: {len(items)}")

with open("data/opportunities.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print("Saved successfully.")
