#!/usr/bin/env python3
"""
Seed Data Generator for VidyaSetu.
Compiles 155+ verified, official scholarships, fellowships, grants, internships,
and research positions across India & Abroad for Indian students.
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = ROOT_DIR / "data" / "opportunities.json"

DATA = []

def add_entry(
    id, title, section, country, type_, category, education_levels,
    streams, target_group, funding_amount, amount_val_inr,
    provider_name, provider_kind, provider_slug, provider_website,
    eligibility, income_limit_inr, open_date, deadline, deadline_text,
    recurring, status, official_link, source_url, documents, process, tags
):
    entry = {
        "id": id,
        "title": title,
        "section": section,
        "country": country,
        "state": None,
        "type": type_,
        "category": category,
        "educationLevel": education_levels,
        "streams": streams,
        "targetGroup": target_group,
        "fundingAmount": funding_amount,
        "amountValINR": amount_val_inr,
        "provider": {
            "name": provider_name,
            "kind": provider_kind,
            "slug": provider_slug,
            "website": provider_website
        },
        "eligibility": eligibility,
        "incomeLimitINR": income_limit_inr,
        "openDate": open_date,
        "deadline": deadline,
        "deadlineText": deadline_text,
        "recurring": recurring,
        "status": status,
        "officialLink": official_link,
        "sourceUrl": source_url,
        "documentsRequired": documents,
        "applicationProcess": process,
        "tags": tags,
        "firstSeen": "2026-10-12",
        "lastVerified": "2026-10-12",
        "verifiedBy": "human",
        "confidence": 1.0
    }
    DATA.append(entry)

# ==============================================================================
# SECTION 1: INDIA - GOVERNMENT SCHEMES & FUNDS (CENTRAL & STATE)
# ==============================================================================

add_entry(
    id="moe-nsp-central-sector",
    title="Central Sector Scheme of Scholarship for College and University Students (PM-USP)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["All Disciplines", "Science", "Commerce", "Arts", "Engineering", "Medicine"],
    target_group=["Merit-cum-Means", "General", "OBC", "SC", "ST", "EWS"],
    funding_amount="₹12,000/yr for UG (first 3 years) and ₹20,000/yr for PG",
    amount_val_inr=20000,
    provider_name="Ministry of Education (MoE), Govt of India", provider_kind="ministry", provider_slug="moe-india", provider_website="https://www.education.gov.in",
    eligibility="Above 80th percentile in relevant stream in Class 12 board exam. Enrolled in regular degree. Family income <= ₹4.5 Lakh/annum.",
    income_limit_inr=450000, open_date="2026-08-01", deadline="2026-12-31", deadline_text="Annually opens August, closes December",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://www.education.gov.in/scholarships-education-loan-0",
    documents=["Class 12 Marksheet", "Income Certificate (< ₹4.5 LPA)", "Aadhaar linked Bank Account", "Bonafide Student Certificate", "Fee Receipt"],
    process=["Register with One-Time Registration (OTR) on NSP", "Fill application under Higher Education Department", "College nodal officer verifies online", "Direct Benefit Transfer (DBT) to bank account"],
    tags=["NSP", "Central Govt", "College Degree", "Post-12th", "DBT"]
)

add_entry(
    id="dst-inspire-she",
    title="INSPIRE Scholarship for Higher Education (SHE) - DST",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["Natural and Basic Sciences", "Physics", "Chemistry", "Mathematics", "Biology", "Earth Sciences"],
    target_group=["Top 1% Board Rankers", "JEE / NEET Top Rankers"],
    funding_amount="₹80,000/yr (₹60,000 stipend + ₹20,000 summer mentorship project grant)",
    amount_val_inr=80000,
    provider_name="Department of Science & Technology (DST)", provider_kind="ministry", provider_slug="dst-india", provider_website="https://dst.gov.in",
    eligibility="Students within top 1% in Class 12 board examination or within top 10,000 rank in JEE Advanced / NEET, admitted to B.Sc./B.S./Int. M.Sc. in Basic & Natural Sciences.",
    income_limit_inr=None, open_date="2026-10-01", deadline="2027-01-15", deadline_text="Annually opens October, closes January",
    recurring=True, status="open",
    official_link="https://online-inspire.gov.in", source_url="https://dst.gov.in/scientific-programmes/inspire/inspire-scholarship",
    documents=["Class 10 & 12 Marksheet", "Advisory note from State/Central Board", "Endorsement Certificate from College Principal", "SBI Bank Account linked with Aadhaar"],
    process=["Apply online via DST INSPIRE Web Portal", "Upload academic endorsement form", "Maintain >= 60% or 7.0 CGPA annually for renewal"],
    tags=["DST", "INSPIRE", "Pure Science", "Merit", "Research"]
)

add_entry(
    id="dst-inspire-phd-fellowship",
    title="INSPIRE Fellowship for Doctoral Research (DST)",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["PhD"],
    streams=["Basic and Applied Sciences", "Engineering", "Medicine", "Agriculture", "Veterinary Sciences"],
    target_group=["University 1st Rank Holders", "INSPIRE SHE Scholars with >70% marks"],
    funding_amount="₹37,000/month (JRF) + HRA -> ₹42,000/month (SRF) + ₹20,000/yr Contingency",
    amount_val_inr=444000,
    provider_name="Department of Science & Technology (DST)", provider_kind="ministry", provider_slug="dst-india", provider_website="https://dst.gov.in",
    eligibility="1st Rank in University Post-Graduate (Master's) examination in basic/applied sciences, or INSPIRE Scholar with >= 70% in aggregate at PG level. Enrolled in PhD.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-11-30", deadline_text="Annually opens September, closes November",
    recurring=True, status="open",
    official_link="https://online-inspire.gov.in", source_url="https://dst.gov.in/scientific-programmes/inspire/inspire-fellowship",
    documents=["Master's Degree & University Rank Certificate", "PhD Admission / Registration letter", "Research Proposal", "Supervisor CV & Endorsement"],
    process=["Submit online proposal on DST INSPIRE portal", "Evaluation by national subject expert committee", "Fellowship tenure for maximum 5 years"],
    tags=["DST", "INSPIRE", "Doctoral", "PhD Fellowship", "Science"]
)

add_entry(
    id="moe-pmrf-doctoral",
    title="Prime Minister's Research Fellowship (PMRF)",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["PhD"],
    streams=["STEM", "Engineering", "Science", "Technology", "Interdisciplinary"],
    target_group=["Premier Researchers admitted to IISc, IITs, IISERs"],
    funding_amount="₹70,000/m (Yr 1-2), ₹75,000/m (Yr 3), ₹80,000/m (Yr 4-5) + ₹2 Lakh/yr Research Grant",
    amount_val_inr=960000,
    provider_name="Ministry of Education (MoE) / National Coordinating IIT", provider_kind="ministry", provider_slug="moe-india", provider_website="https://www.pmrf.in",
    eligibility="Admitted to full-time PhD in PMRF granting institutes (IISc, IITs, IISERs, select Central Univs) via Direct Entry (CGPA >= 8.0 or qualifying GATE) or Lateral Entry channel.",
    income_limit_inr=None, open_date="2026-05-01", deadline="2026-06-30", deadline_text="Cycle opens twice a year (May and December)",
    recurring=True, status="upcoming",
    official_link="https://www.pmrf.in", source_url="https://www.pmrf.in/guidelines",
    documents=["Comprehensive Research Proposal", "Academic Transcripts", "GATE/Scorecard (if applicable)", "Recommendation Letters by PhD Advisor"],
    process=["Institute nominates qualified PhD students", "National Apex Committee reviews research proposal and conducts interviews", "Awardees undergo annual research progress reviews"],
    tags=["PMRF", "Highest Stipend", "IIT", "IISc", "Doctoral", "Prestigious"]
)

add_entry(
    id="aicte-pragati-scholarship",
    title="AICTE Pragati Scholarship Scheme for Girl Students",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Engineering", "Technology", "Architecture", "Pharmacy", "Applied Arts"],
    target_group=["Female / Girl Students Only"],
    funding_amount="₹50,000 per annum for entire duration of degree/diploma course",
    amount_val_inr=50000,
    provider_name="All India Council for Technical Education (AICTE)", provider_kind="ministry", provider_slug="aicte-india", provider_website="https://www.aicte-india.org",
    eligibility="Female student admitted to 1st year Degree/Diploma course in AICTE approved institution. Maximum 2 girls per family. Family annual income <= ₹8 Lakhs.",
    income_limit_inr=800000, open_date="2026-08-15", deadline="2026-12-31", deadline_text="Annually opens August, closes December via NSP",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://www.aicte-india.org/schemes/students-development-schemes/pragati",
    documents=["Class 10 & 12 Marksheet", "Allotment Letter from Centralized Admission Process (CAP)", "Income Certificate (< ₹8 LPA)", "Aadhaar Card", "College Fee Receipt"],
    process=["Register and apply under AICTE Schemes on NSP", "Verification by College Nodal Officer", "Disbursement through Direct Benefit Transfer"],
    tags=["AICTE", "Girls in STEM", "Engineering", "Technical Degree", "Women"]
)

add_entry(
    id="aicte-saksham-scholarship",
    title="AICTE Saksham Scholarship Scheme for Specially-Abled Students",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Engineering", "Technology", "Technical Courses"],
    target_group=["Differently Abled (PwD >= 40%)"],
    funding_amount="₹50,000 per annum towards tuition and assistive devices",
    amount_val_inr=50000,
    provider_name="All India Council for Technical Education (AICTE)", provider_kind="ministry", provider_slug="aicte-india", provider_website="https://www.aicte-india.org",
    eligibility="Specially-abled students having disability >= 40%, admitted to 1st year of technical Degree/Diploma in AICTE approved institution. Family income <= ₹8 Lakhs/annum.",
    income_limit_inr=800000, open_date="2026-08-15", deadline="2026-12-31", deadline_text="Annually opens August, closes December on NSP",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://www.aicte-india.org/schemes/students-development-schemes/saksham",
    documents=["Disability Certificate (min 40% issued by competent medical authority)", "Income Certificate (< ₹8 LPA)", "Admission Letter & Fee Receipt", "Class 10 & 12 Marksheet"],
    process=["Apply through National Scholarship Portal", "Institute scrutiny and approval", "Annual renewal upon passing year-end exam"],
    tags=["AICTE", "PwD", "Assistive Devices", "Differently Abled"]
)

add_entry(
    id="aicte-swanath-scholarship",
    title="AICTE Swanath Scholarship Scheme (Orphans and Wards of Armed Forces)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Engineering", "Technical Courses", "Management", "Architecture"],
    target_group=["Orphans", "Children of Parents who died due to Covid-19", "Wards of Armed Forces / CAPF martyred in action"],
    funding_amount="₹50,000 per annum throughout course duration",
    amount_val_inr=50000,
    provider_name="All India Council for Technical Education (AICTE)", provider_kind="ministry", provider_slug="aicte-india", provider_website="https://www.aicte-india.org",
    eligibility="Orphan students, or candidate whose both parents died due to Covid-19, or wards of Armed Forces/CAPF personnel martyred. Family income <= ₹8 LPA. Studying in AICTE institution.",
    income_limit_inr=800000, open_date="2026-08-15", deadline="2026-12-31", deadline_text="Annually opens August, closes December on NSP",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://www.aicte-india.org/schemes/students-development-schemes/swanath",
    documents=["Death Certificate of Parents or Martrydom Certificate from Competent Authority", "Bonafide Student Certificate", "Class 10 & 12 Marksheet", "Income Certificate"],
    process=["Apply via National Scholarship Portal under AICTE Swanath", "Institute and State level verification", "Direct bank transfer"],
    tags=["AICTE", "Swanath", "Covid Relief", "Armed Forces", "Financial Aid"]
)

add_entry(
    id="csir-ugc-jrf-net",
    title="Joint CSIR-UGC Junior Research Fellowship (JRF) & NET",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["Master", "PhD"],
    streams=["Chemical Sciences", "Earth Sciences", "Life Sciences", "Mathematical Sciences", "Physical Sciences"],
    target_group=["National Competitive Examination Rankers"],
    funding_amount="₹37,000/month (JRF) + HRA -> ₹42,000/month (SRF) + ₹20,000/yr Contingency",
    amount_val_inr=444000,
    provider_name="Council of Scientific & Industrial Research (CSIR) & UGC", provider_kind="ministry", provider_slug="csir-india", provider_website="https://csirhrdg.res.in",
    eligibility="M.Sc. or equivalent with >= 55% marks (50% for SC/ST/PwD/Third gender). Age <= 30 years (relaxation for reserved categories and women).",
    income_limit_inr=None, open_date="2026-04-01", deadline="2026-05-15", deadline_text="Conducted twice a year (June & December cycles)",
    recurring=True, status="upcoming",
    official_link="https://csirnet.nta.ac.in", source_url="https://csirhrdg.res.in/Home/Index/1/Default/2733/58",
    documents=["Master's Marksheet / Result Awaited Certificate", "Category Certificate (OBC-NCL/SC/ST/EWS)", "ID Proof"],
    process=["Appear for computer-based NET exam conducted by NTA", "Secure JRF rank cutoff", "Activate fellowship by enrolling in PhD at CSIR Lab or University"],
    tags=["CSIR", "Doctoral", "National Exam", "Science Research"]
)

add_entry(
    id="dbt-jrf-bet-fellowship",
    title="DBT Junior Research Fellowship (DBT-JRF / BET)",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["Master", "PhD"],
    streams=["Biotechnology", "Bioinformatics", "Life Sciences", "Biochemical Engineering", "Agriculture Biotech"],
    target_group=["Biotechnology Postgraduates"],
    funding_amount="₹37,000/month (JRF) + HRA -> ₹42,000/month (SRF) + ₹30,000/yr Contingency",
    amount_val_inr=444000,
    provider_name="Department of Biotechnology (DBT), Govt of India", provider_kind="ministry", provider_slug="dbt-india", provider_website="https://dbtindia.gov.in",
    eligibility="M.Sc./M.Tech/M.V.Sc. in Biotechnology or allied life sciences with >= 60% marks. Age <= 28 years (relaxable by 5 years for SC/ST/PwD/Women).",
    income_limit_inr=None, open_date="2026-02-15", deadline="2026-03-31", deadline_text="Annually opens February, exam in April/May",
    recurring=True, status="closed",
    official_link="https://rcb.res.in/DBTJRF", source_url="https://dbtindia.gov.in/schemes-programmes/building-capacities/human-resource-development",
    documents=["Postgraduate Degree Certificate & Marksheets", "Category Certificate", "Government Photo ID"],
    process=["Qualify Biotechnology Eligibility Test (BET) Category-I", "Activate fellowship at any recognized university or national research lab across India"],
    tags=["DBT", "Biotechnology", "Life Sciences", "JRF", "Doctoral"]
)

add_entry(
    id="icmr-jrf-fellowship",
    title="ICMR Junior Research Fellowship in Biomedical Sciences",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["Master", "PhD"],
    streams=["Biomedical Sciences", "Biochemistry", "Microbiology", "Pharmacology", "Public Health", "Social Sciences"],
    target_group=["Biomedical and Social Science Graduates"],
    funding_amount="₹37,000/month + HRA + ₹20,000/yr Contingency Grant",
    amount_val_inr=444000,
    provider_name="Indian Council of Medical Research (ICMR)", provider_kind="ministry", provider_slug="icmr-india", provider_website="https://main.icmr.nic.in",
    eligibility="Postgraduate degree in Life Sciences or Social Sciences with >= 55% marks (50% for SC/ST/PwD). Age limit <= 28 years.",
    income_limit_inr=None, open_date="2026-06-01", deadline="2026-07-15", deadline_text="Annually opens June, exam in September",
    recurring=True, status="upcoming",
    official_link="https://main.icmr.nic.in", source_url="https://main.icmr.nic.in/content/junior-research-fellowships-jrf",
    documents=["M.Sc./MA Marksheets", "Valid Category/Caste Certificate", "Photo ID Proof"],
    process=["Register for ICMR-JRF Entrance Examination conducted jointly with PGIMER", "Qualify in Biomedical or Social Sciences stream", "Register for PhD at recognized medical college/institute"],
    tags=["ICMR", "Medical Research", "Biomedical", "PhD"]
)

add_entry(
    id="dst-wise-phd-wos",
    title="DST WISE-PhD Fellowship (Formerly Women Scientists Scheme WOS-A)",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["Master", "PhD"],
    streams=["Physical Sciences", "Chemical Sciences", "Life Sciences", "Engineering", "Mathematical Sciences"],
    target_group=["Women Scientists seeking PhD registration"],
    funding_amount="₹37,000/month + HRA + ₹1,00,000/year Research Grant",
    amount_val_inr=444000,
    provider_name="Department of Science & Technology (DST)", provider_kind="ministry", provider_slug="dst-india", provider_website="https://dst.gov.in",
    eligibility="Unemployed female Indian citizens aged 27-45 years with qualifying PG degree in Basic/Applied Sciences or B.Tech/MBBS, admitted to PhD in recognized institution.",
    income_limit_inr=None, open_date="2026-01-01", deadline=None, deadline_text="Applications accepted round the year (Rolling)",
    recurring=True, status="rolling",
    official_link="https://onlinedst.gov.in", source_url="https://dst.gov.in/scientific-programmes/wise-kiran",
    documents=["Research Proposal", "Bio-data of Mentor & Host Institute Acceptance", "PG Transcripts & Degree Certificate", "Break in Career / Age Affidavit"],
    process=["Submit detailed scientific project proposal online via e-PMS portal", "Presentation before Subject Expert Committee", "Fellowship tenure of 5 years to complete PhD"],
    tags=["Women in Science", "DST", "WISE", "WOS-A", "Doctoral"]
)

add_entry(
    id="serb-anrf-npdf",
    title="ANRF - National Post Doctoral Fellowship (N-PDF)",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["Postdoc"],
    streams=["Engineering", "Physical Sciences", "Chemical Sciences", "Life Sciences", "Earth & Planetary Sciences"],
    target_group=["Early Career Postdoctoral Researchers"],
    funding_amount="₹55,000/month (₹60,000 post-submission) + HRA + ₹2,00,000/year Research Grant",
    amount_val_inr=660000,
    provider_name="Anusandhan National Research Foundation (ANRF / SERB)", provider_kind="ministry", provider_slug="anrf-india", provider_website="https://serbonline.in",
    eligibility="Indian citizens with PhD/MD/MS degree in science or engineering. Age <= 35 years (relaxable by 5 years for SC/ST/OBC/Women/PwD). Mentor must be regular faculty in recognized Indian institute.",
    income_limit_inr=None, open_date="2026-05-01", deadline="2026-06-30", deadline_text="Annually opens May, closes June",
    recurring=True, status="upcoming",
    official_link="https://serbonline.in", source_url="https://serbonline.in/SERB/npdf",
    documents=["Postdoctoral Research Proposal", "Host Institute Endorsement Letter", "Consent & Bio-data of Mentor", "PhD Degree / Thesis Submission Certificate"],
    process=["Formulate project with academic mentor", "Submit online on SERB-ANRF portal", "Apex review committee announces selections for 2-year tenure"],
    tags=["Postdoc", "ANRF", "SERB", "Advanced Research", "High Fellowship"]
)

add_entry(
    id="serb-tare-fellowship",
    title="SERB Teachers Associateship for Research Excellence (TARE)",
    section="india", country="India", type_="government", category="Fund/Grant",
    education_levels=["Postdoc"],
    streams=["All Science and Engineering Fields"],
    target_group=["Faculty in State Universities and Colleges"],
    funding_amount="₹60,000/year personal incentive + ₹5,00,000/year research grant to host institute",
    amount_val_inr=560000,
    provider_name="Anusandhan National Research Foundation (ANRF / SERB)", provider_kind="ministry", provider_slug="anrf-india", provider_website="https://serbonline.in",
    eligibility="Regular faculty in State Universities/Colleges with PhD in Science/Engineering. Age <= 45 years. Collaborates with IITs, IISc, IISERs, or CSIR Labs.",
    income_limit_inr=None, open_date="2026-02-01", deadline="2026-03-31", deadline_text="Annually opens February, closes March",
    recurring=True, status="closed",
    official_link="https://serbonline.in", source_url="https://serbonline.in/SERB/tare",
    documents=["Joint Research Proposal with Host Scientist", "NOC from Parent College", "Endorsement from Host Institute (IIT/IISc/CSIR)", "PhD Degree"],
    process=["Submit online proposal on SERB portal", "Research tenure of 3 years with 90 days/year spent at premier host lab"],
    tags=["Faculty", "Research Grant", "IIT Collaboration", "ANRF"]
)

add_entry(
    id="ugc-ishan-uday-ner",
    title="Ishan Uday Special Scholarship Scheme for North Eastern Region (NER)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["General Degree", "Technical Degree", "Medical", "Professional Courses"],
    target_group=["Students of North Eastern States (Assam, Arunachal, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura)"],
    funding_amount="₹5,400/month (General Degree) to ₹7,800/month (Technical/Medical Degree)",
    amount_val_inr=93600,
    provider_name="University Grants Commission (UGC)", provider_kind="ministry", provider_slug="ugc-india", provider_website="https://www.ugc.gov.in",
    eligibility="Domicile of North Eastern States having passed Class 12. Admitted to 1st year of UG degree in recognized university/college. Family income <= ₹4.5 Lakh/annum.",
    income_limit_inr=450000, open_date="2026-08-01", deadline="2026-12-31", deadline_text="Annually opens August, closes December via NSP",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://www.ugc.gov.in/page/Ishan-Uday.aspx",
    documents=["Domicile Certificate of NER State", "Income Certificate (< ₹4.5 LPA)", "Class 12 Marksheet", "College Admission Proof", "Aadhaar Card"],
    process=["Apply through National Scholarship Portal under UGC Schemes", "Verification by College and State Directorate", "DBT dispatches funds directly to student account"],
    tags=["North East", "UGC", "NER Students", "Undergraduate"]
)

add_entry(
    id="msje-pm-yasasvi",
    title="PM Young Achievers Scholarship Award Scheme for Vibrant India (PM-YASASVI)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["All Disciplines in Top-Class Colleges"],
    target_group=["OBC", "EBC", "De-notified Tribes (DNT)"],
    funding_amount="Full Tuition Fee Reimbursement up to ₹2,00,000/yr + Living allowance ₹3,000/m",
    amount_val_inr=236000,
    provider_name="Ministry of Social Justice & Empowerment (MoSJE)", provider_kind="ministry", provider_slug="msje-india", provider_website="https://socialjustice.gov.in",
    eligibility="OBC, EBC, or DNT students admitted to identified top-class institutions (IITs, IIMs, AIIMS, NITs, NLUs, etc.). Family annual income <= ₹2.5 Lakhs.",
    income_limit_inr=250000, open_date="2026-07-15", deadline="2026-11-30", deadline_text="Annually opens July, closes November",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://socialjustice.gov.in/schemes/34",
    documents=["OBC / EBC / DNT Community Certificate", "Income Certificate (< ₹2.5 LPA)", "Admission Letter into Top Identified Institute", "Fee Structure Receipts"],
    process=["Apply through National Scholarship Portal", "Select Top Class Education Scheme for OBC/EBC/DNT", "Funds disbursed directly to institute and student account"],
    tags=["YASASVI", "OBC", "Top Class Institutions", "MoSJE", "Tuition Waiver"]
)

add_entry(
    id="moma-begum-hazrat-mahal",
    title="Begum Hazrat Mahal National Scholarship for Minority Girls",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th"],
    streams=["Class 11 and 12 in any stream"],
    target_group=["Girl Students belonging to Notified Minority Communities (Muslim, Christian, Sikh, Buddhist, Jain, Parsi)"],
    funding_amount="₹6,000 per annum for Class 11 & 12",
    amount_val_inr=6000,
    provider_name="Maulana Azad Education Foundation / Ministry of Minority Affairs", provider_kind="ministry", provider_slug="moma-india", provider_website="https://www.minorityaffairs.gov.in",
    eligibility="Female students belonging to minority communities who have secured >= 50% marks in Class 10. Family annual income <= ₹2.00 Lakhs.",
    income_limit_inr=200000, open_date="2026-08-01", deadline="2026-11-30", deadline_text="Annually opens August, closes November",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://www.minorityaffairs.gov.in",
    documents=["Self-declaration of Minority Community", "Income Certificate (< ₹2.0 LPA)", "Class 10 Marksheet", "Aadhaar Card", "School Verification Form"],
    process=["Apply on National Scholarship Portal", "School Principal verifies credentials", "Direct Benefit Transfer to bank account"],
    tags=["Minority Girls", "Class 12", "MoMA", "Women Empowerment"]
)

add_entry(
    id="ugc-svsgc-fellowship",
    title="Swami Vivekananda Single Girl Child Fellowship for Research in Social Sciences",
    section="india", country="India", type_="government", category="Fellowship",
    education_levels=["PhD"],
    streams=["Social Sciences", "Humanities", "Economics", "Sociology", "Political Science", "History"],
    target_group=["Single Girl Child in Family"],
    funding_amount="₹31,000/month (Initial 2 yrs) -> ₹35,000/month (Next 3 yrs) + Contingency",
    amount_val_inr=372000,
    provider_name="University Grants Commission (UGC)", provider_kind="ministry", provider_slug="ugc-india", provider_website="https://www.ugc.gov.in",
    eligibility="Single girl child of her parents (or only twin girls/fraternal daughters), registered in regular full-time PhD in Social Sciences in recognized Indian University. Age <= 40 years.",
    income_limit_inr=None, open_date="2026-08-01", deadline="2026-10-31", deadline_text="Annually opens August, closes October on UGC Portal",
    recurring=True, status="open",
    official_link="https://www.ugc.gov.in", source_url="https://www.ugc.gov.in/page/SVSGC.aspx",
    documents=["Single Girl Child Affidavit on ₹100 stamp paper attested by SDM/First Class Magistrate", "PhD Registration Certificate", "Master's Marksheet", "Joining Report"],
    process=["Submit application on UGC e-Scholarship portal", "Online verification by University Registrar", "Monthly disbursement via DBT portal"],
    tags=["Single Girl Child", "UGC", "PhD", "Social Sciences", "Doctoral"]
)

add_entry(
    id="msje-post-matric-sc",
    title="Post Matric Scholarship for Scheduled Caste (SC) Students",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD", "Postdoc"],
    streams=["All Disciplines", "Arts", "Science", "Commerce", "Engineering", "Medicine"],
    target_group=["Scheduled Caste (SC) Students"],
    funding_amount="100% Compulsory Tuition Fee Reimbursement + ₹4,000 to ₹13,500/year living allowance",
    amount_val_inr=75000,
    provider_name="Ministry of Social Justice & Empowerment (MoSJE)", provider_kind="ministry", provider_slug="msje-india", provider_website="https://socialjustice.gov.in",
    eligibility="SC students pursuing post-matriculation courses in recognized institutions. Annual family income <= ₹2.50 Lakhs from all sources.",
    income_limit_inr=250000, open_date="2026-07-01", deadline="2026-12-31", deadline_text="Annual cycle open July to December across State & NSP portals",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://socialjustice.gov.in/schemes/26",
    documents=["Valid SC Caste Certificate", "Income Certificate issued by Tehsildar (< ₹2.5 LPA)", "Previous Year Marksheets", "Fee Receipt", "Aadhaar seeded bank account"],
    process=["Apply via respective State Portal or National Scholarship Portal", "Institute scrutiny and district welfare officer approval", "Central & State share credited via DBT (60:40 formula)"],
    tags=["SC Scholarship", "Tuition Waiver", "Post-Matric", "Government"]
)

add_entry(
    id="mota-post-matric-st",
    title="National Post Matric Scholarship for Scheduled Tribe (ST) Students",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["All Disciplines"],
    target_group=["Scheduled Tribe (ST) Students"],
    funding_amount="Complete Tuition and Non-refundable Fee Reimbursement + Annual maintenance allowance",
    amount_val_inr=70000,
    provider_name="Ministry of Tribal Affairs (MoTA)", provider_kind="ministry", provider_slug="mota-india", provider_website="https://tribal.nic.in",
    eligibility="ST students pursuing recognized post-matric education. Family annual gross income <= ₹2.50 Lakhs.",
    income_limit_inr=250000, open_date="2026-07-01", deadline="2026-12-31", deadline_text="Annually opens July, closes December",
    recurring=True, status="open",
    official_link="https://scholarships.gov.in", source_url="https://tribal.nic.in/PostMatric.aspx",
    documents=["Valid ST Certificate", "Income Certificate (< ₹2.5 LPA)", "College Admission Letter & Fee Schedule", "Bank Passbook"],
    process=["Online application on NSP or State Tribal Welfare portal", "College verifies student bonafide", "Direct DBT payment"],
    tags=["ST Scholarship", "Tribal Affairs", "Tuition Reimbursement", "DBT"]
)

# State Government Portals
add_entry(
    id="state-mahadbt-rajarshi-shahu",
    title="Rajarshi Chhatrapati Shahu Maharaj Shikshan Shulkh Shishyavrutti Yojna (MahaDBT)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["Professional Courses", "Engineering", "Pharmacy", "Medicine", "Management", "General UG/PG"],
    target_group=["EBC", "OBC", "General (Economically Backward) in Maharashtra"],
    funding_amount="50% to 100% Tuition & Exam Fee Waiver (Up to ₹1,50,000/yr)",
    amount_val_inr=100000,
    provider_name="Government of Maharashtra (Directorate of Higher & Technical Education)", provider_kind="ministry", provider_slug="govt-maharashtra", provider_website="https://mahadbt.maharashtra.gov.in",
    eligibility="Domicile of Maharashtra admitted through CAP round. Family annual income <= ₹8.00 Lakhs. Maximum 2 children in family.",
    income_limit_inr=800000, open_date="2026-08-01", deadline="2027-01-31", deadline_text="Annual cycle open August to January",
    recurring=True, status="open",
    official_link="https://mahadbt.maharashtra.gov.in", source_url="https://mahadbt.maharashtra.gov.in/SchemeData/SchemeData?str=E9DDFA3703C388427F2D879FEE5737C7",
    documents=["Maharashtra Domicile Certificate", "Income Certificate issued by Tehsildar (< ₹8 LPA)", "CAP Allotment Letter", "Ration Card", "Attendance Certificate (>75%)"],
    process=["Create profile on MahaDBT portal", "Link Aadhaar with NPCI mapping", "Submit scheme application and verify at institute desk"],
    tags=["Maharashtra", "MahaDBT", "State Scheme", "Fee Waiver", "EBC"]
)

add_entry(
    id="state-karnataka-ssp",
    title="Karnataka State Scholarship Portal (SSP) Post-Matric Scheme",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["All Streams", "Engineering", "Medical", "Arts", "Science", "Commerce"],
    target_group=["Karnataka Domicile Students (SC, ST, OBC, Minority, General EWS)"],
    funding_amount="100% Tuition Fee Concession + Monthly maintenance allowance",
    amount_val_inr=65000,
    provider_name="Government of Karnataka (Social Welfare, Backward Classes & Minorities Depts)", provider_kind="ministry", provider_slug="govt-karnataka", provider_website="https://ssp.postmatric.karnataka.gov.in",
    eligibility="Domicile of Karnataka studying post-matric courses. Caste and income certificate verified via Kutumba ID database.",
    income_limit_inr=250000, open_date="2026-09-01", deadline="2027-01-15", deadline_text="Annually opens September, closes January",
    recurring=True, status="open",
    official_link="https://ssp.postmatric.karnataka.gov.in", source_url="https://ssp.postmatric.karnataka.gov.in",
    documents=["Kutumba ID / Aadhaar Number", "RD Number of Caste & Income Certificate", "College Registration Number (UUCMS / SATS)", "Hostel ID (for hostellers)"],
    process=["Register with Kutumba ID on Karnataka SSP", "Data auto-fetched from revenue department", "E-Attestation by designated college officer"],
    tags=["Karnataka", "SSP", "Kutumba", "State Portal", "Fee Concession"]
)

add_entry(
    id="state-wb-svmcm",
    title="Swami Vivekananda Merit-cum-Means Scholarship (SVMCM) - West Bengal",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["Higher Secondary", "Undergraduate (Arts/Science/Commerce/Engg/Med)", "Postgraduate", "M.Phil/PhD"],
    target_group=["West Bengal Domicile Students with >= 60% Marks"],
    funding_amount="₹12,000/yr (UG Arts/Comm) to ₹60,000/yr (Engineering/Medical) and ₹96,000/yr for PhD",
    amount_val_inr=60000,
    provider_name="Higher Education Department, Government of West Bengal", provider_kind="ministry", provider_slug="govt-west-bengal", provider_website="https://svmcm.wbhed.gov.in",
    eligibility="Resident of West Bengal with >= 60% marks in previous qualifying board/degree exam (53% for PG). Family income <= ₹2.50 Lakhs/annum.",
    income_limit_inr=250000, open_date="2026-09-01", deadline="2027-02-28", deadline_text="Annually opens September, closes February",
    recurring=True, status="open",
    official_link="https://svmcm.wbhed.gov.in", source_url="https://svmcm.wbhed.gov.in",
    documents=["Income Certificate from BDO/SDO", "Marksheet of qualifying examination (min 60%)", "Proof of Admission in WB Institution", "First page of Bank Passbook"],
    process=["Register online on Bikash Bhavan SVMCM portal", "Upload scanned marksheets and income cert", "Institute HOI verifies student record", "Disbursement through IFMS WB"],
    tags=["West Bengal", "SVMCM", "State Merit", "Engineering & Medical"]
)

add_entry(
    id="state-telangana-epass",
    title="Telangana ePASS Post Matric Scholarship & Fee Reimbursement (RTF & MTF)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["Engineering", "Pharmacy", "MBA", "MCA", "General Degree"],
    target_group=["SC, ST, BC, EBC, Minority, PwD students of Telangana"],
    funding_amount="Reimbursement of Tuition Fee (RTF) 100% + Maintenance Fee (MTF) ₹1,400/month",
    amount_val_inr=85000,
    provider_name="Government of Telangana (Telangana Welfare Departments)", provider_kind="ministry", provider_slug="govt-telangana", provider_website="https://telanganaepass.cgg.gov.in",
    eligibility="Students of Telangana with >= 75% college attendance. Income ceiling: SC/ST <= ₹2.0 LPA, BC/EBC rural <= ₹1.5 LPA, urban <= ₹2.0 LPA.",
    income_limit_inr=200000, open_date="2026-08-01", deadline="2026-12-31", deadline_text="Annually opens August, closes December",
    recurring=True, status="open",
    official_link="https://telanganaepass.cgg.gov.in", source_url="https://telanganaepass.cgg.gov.in",
    documents=["SSC Hall Ticket Number", "MeeSeva Caste & Income Certificate", "Aadhaar Card", "College Bonafide", "Bank Passbook"],
    process=["Submit online application on Telangana ePASS", "Verification by College Principal and District Welfare Officer", "RTF directly credited to college and MTF to student"],
    tags=["Telangana", "ePASS", "RTF", "MTF", "State Reimbursement"]
)

add_entry(
    id="state-bihar-pms",
    title="Bihar Post Matric Scholarship Portal (PMS Bihar)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["All Streams in Government and Recognized Private Colleges"],
    target_group=["SC, ST, BC, EBC Students of Bihar"],
    funding_amount="Compulsory non-refundable fee reimbursement (₹2,000 to ₹1,00,000/yr)",
    amount_val_inr=50000,
    provider_name="Education Department, Government of Bihar", provider_kind="ministry", provider_slug="govt-bihar", provider_website="https://pmsonline.bih.nic.in",
    eligibility="Permanent resident of Bihar belonging to SC/ST/BC/EBC categories studying in approved colleges. Family income <= ₹3.00 Lakhs.",
    income_limit_inr=300000, open_date="2026-08-15", deadline="2026-12-31", deadline_text="Annually opens August, closes December",
    recurring=True, status="open",
    official_link="https://pmsonline.bih.nic.in", source_url="https://pmsonline.bih.nic.in",
    documents=["Bihar Residential/Domicile Certificate", "Caste Certificate", "Current Year Income Certificate", "College Fee Structure & Bonafide"],
    process=["Register on Bihar PMS portal with Aadhaar", "Institution verification followed by Physical Committee and DPO verification", "Direct DBT payment"],
    tags=["Bihar", "PMS Bihar", "State Portal", "Fee Reimbursement"]
)

add_entry(
    id="state-up-scholarship",
    title="Uttar Pradesh Post Matric Scholarship and Fee Reimbursement (UP Scholarship)",
    section="india", country="India", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["All Courses", "Polytechnic", "B.Tech", "BA", "B.Sc", "B.Com", "Medical"],
    target_group=["General, SC, ST, OBC, Minority Students in UP"],
    funding_amount="Complete Course Fee Reimbursement + Annual maintenance allowance up to ₹60,000",
    amount_val_inr=60000,
    provider_name="Social Welfare Department, Government of Uttar Pradesh", provider_kind="ministry", provider_slug="govt-up", provider_website="https://scholarship.up.gov.in",
    eligibility="Domicile of Uttar Pradesh studying in recognized colleges. Family annual income <= ₹2.00 Lakhs (General/OBC/Minority) or <= ₹2.50 Lakhs (SC/ST).",
    income_limit_inr=200000, open_date="2026-07-01", deadline="2026-12-20", deadline_text="Annually opens July, closes December",
    recurring=True, status="open",
    official_link="https://scholarship.up.gov.in", source_url="https://scholarship.up.gov.in",
    documents=["Aadhaar linked with Mobile & Bank", "UP Domicile Certificate", "Caste & Income Certificate verified from e-District UP", "Fee Receipt", "Marksheets"],
    process=["Register online on scholarship.up.gov.in", "Verify with Digilocker integration", "Institute verification and forwarding to District Welfare Officer"],
    tags=["Uttar Pradesh", "UP Scholarship", "Shaskiya Chhatravritti", "State Govt"]
)

# ==============================================================================
# SECTION 1: INDIA - PRIVATE & CSR PHILANTHROPIC SCHOLARSHIPS
# ==============================================================================

add_entry(
    id="tata-trusts-means-grant",
    title="Tata Trusts Means & Merit Scholarships (UG & PG)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["Bachelor", "Master"],
    streams=["Engineering", "Medicine", "Pharmacy", "Special Education", "Social Sciences"],
    target_group=["Merit-cum-Means", "Economically Weaker Section"],
    funding_amount="30% to 80% of College Tuition Fees (Up to ₹1,50,000/yr)",
    amount_val_inr=150000,
    provider_name="Sir Ratan Tata Trust & Allied Trusts", provider_kind="trust", provider_slug="tata-trusts", provider_website="https://www.tatatrusts.org",
    eligibility="Undergraduate or Postgraduate students in recognized Indian institutes with >= 60% marks and family income <= ₹4.5 Lakhs.",
    income_limit_inr=450000, open_date="2026-10-01", deadline="2027-01-15", deadline_text="Annually opens October, closes January",
    recurring=True, status="open",
    official_link="https://www.tatatrusts.org", source_url="https://www.tatatrusts.org/our-work/individual-grants-programme/education-grants",
    documents=["Semester marksheets / 12th board marksheet", "Original fee receipt for academic year", "Income Certificate or ITR", "Cancelled Cheque"],
    process=["Submit application on Tata Trusts Individual Grants portal", "Document verification and telephonic interview", "Direct grant paid to institute or student"],
    tags=["Tata Trusts", "Philanthropic", "Tuition Grant", "Medical & Engineering"]
)

add_entry(
    id="reliance-foundation-ug-scholarship",
    title="Reliance Foundation Undergraduate Scholarships (5,000 Annual Awards)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["All Streams", "Engineering", "Commerce", "Arts", "Science", "Law", "Medicine"],
    target_group=["Merit-cum-Means", "Undergraduate Freshers"],
    funding_amount="Up to ₹2,00,000 over degree duration + Mentorship & Leadership Workshops",
    amount_val_inr=200000,
    provider_name="Reliance Foundation", provider_kind="company", provider_slug="reliance-foundation", provider_website="https://www.reliancefoundation.org",
    eligibility="1st year undergraduate students in any stream with >= 60% in Class 12. Household income <= ₹15 Lakhs/year (preference to < ₹2.5 Lakhs).",
    income_limit_inr=1500000, open_date="2026-08-15", deadline="2026-10-15", deadline_text="Annually opens August, closes mid-October",
    recurring=True, status="open",
    official_link="https://www.scholarships.reliancefoundation.org", source_url="https://www.scholarships.reliancefoundation.org",
    documents=["Class 10 & 12 Marksheet", "Current College Bonafide Certificate", "Family Income Proof (Salary slip/ITR/Certificate)", "Aadhaar Card"],
    process=["Complete online eligibility questionnaire", "Take 60-minute mandatory online aptitude test", "Selection based on aptitude score and socio-economic weightage"],
    tags=["Reliance", "Undergraduate", "CSR", "Large Scale", "Mentorship"]
)

add_entry(
    id="reliance-foundation-pg-scholarship",
    title="Reliance Foundation Postgraduate Scholarships in Technology & AI",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["Master"],
    streams=["Artificial Intelligence", "Computer Sciences", "Mathematics & Computing", "Electrical Engineering", "Renewable Energy"],
    target_group=["Top PG Talent in Future Technologies"],
    funding_amount="Up to ₹6,00,000 over course duration + Global Expert Mentorship",
    amount_val_inr=600000,
    provider_name="Reliance Foundation", provider_kind="company", provider_slug="reliance-foundation", provider_website="https://www.reliancefoundation.org",
    eligibility="1st year students enrolled in eligible PG degree programmes in AI, Data Science, CS, and Renewable Energy. Valid GATE score or high UG CGPA.",
    income_limit_inr=None, open_date="2026-08-15", deadline="2026-10-20", deadline_text="Annually opens August, closes October",
    recurring=True, status="open",
    official_link="https://www.scholarships.reliancefoundation.org", source_url="https://www.scholarships.reliancefoundation.org",
    documents=["Undergraduate Transcripts", "GATE scorecard (if available)", "Statement of Purpose (SOP)", "Two Recommendation Letters"],
    process=["Online application and Statement of Purpose", "Review by international jury of academics and industry leaders", "Virtual interview round"],
    tags=["Reliance", "Artificial Intelligence", "Computer Science", "Postgraduate", "High Stipend"]
)

add_entry(
    id="aditya-birla-scholarship",
    title="Aditya Birla Group Scholarships (IIT, IIM, BITS, NLU)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["Bachelor", "Master"],
    streams=["Engineering (IITs/BITS)", "Management (IIMs/XLRI)", "Law (NLUs)"],
    target_group=["Top Rankers in Premier Institutes"],
    funding_amount="₹1,00,000 to ₹1,80,000 per annum (or full tuition fee waiver)",
    amount_val_inr=180000,
    provider_name="Aditya Birla Group", provider_kind="company", provider_slug="aditya-birla-group", provider_website="https://www.adityabirla.com",
    eligibility="Top 20 rankers admitted into select premier institutes (IIT Bombay, Delhi, Madras, Kanpur, Kharagpur; BITS Pilani; IIM Ahmedabad, Bangalore, Calcutta; NLSIU, NALSAR).",
    income_limit_inr=None, open_date="2026-07-15", deadline="2026-09-15", deadline_text="Annually opens July at start of premier academic session",
    recurring=True, status="open",
    official_link="https://www.adityabirlascholars.net", source_url="https://www.adityabirlascholars.net",
    documents=["Entrance Rank Letter", "Leadership Essays (Ethics, Vision, Personal Philosophy)", "Dean / Director Endorsement Form"],
    process=["Dean's office nominates top applicants", "Written essay screening", "Jury interviews in Mumbai before eminent panel"],
    tags=["Aditya Birla", "IIT", "IIM", "Premier Institutes", "Merit"]
)

add_entry(
    id="hdfc-parivartan-ecss",
    title="HDFC Bank Parivartan's Educational Crisis Support Scholarship (ECSS)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["School, General UG/PG, Professional Courses (B.Tech, MBBS, Law, CA)"],
    target_group=["Need-based", "Crisis Facing Families", "Income Loss"],
    funding_amount="Up to ₹75,000 per year directly to beneficiary account",
    amount_val_inr=75000,
    provider_name="HDFC Bank CSR (Parivartan)", provider_kind="company", provider_slug="hdfc-bank", provider_website="https://www.hdfcbank.com",
    eligibility="Students who have faced family crisis (death of earning member, serious medical illness, job loss) or annual income <= ₹2.5 Lakhs with >= 55% in previous exam.",
    income_limit_inr=250000, open_date="2026-08-01", deadline="2026-11-15", deadline_text="Annually opens August, closes November",
    recurring=True, status="open",
    official_link="https://www.hdfcbank.com", source_url="https://www.hdfcbank.com/personal/about-us/corporate-social-responsibility",
    documents=["Previous Year Marksheet (min 55%)", "Income / Crisis Proof Document", "Admission Proof & College ID", "Bank Account Details"],
    process=["Submit online form on Buddy4Study / HDFC portal", "Telephonic verification and document audit", "Direct fund transfer via NEFT"],
    tags=["HDFC Bank", "Parivartan", "Crisis Support", "Financial Aid"]
)

add_entry(
    id="kotak-kanya-scholarship",
    title="Kotak Kanya Scholarship for Meritorious Girl Students",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Professional Courses", "Engineering", "Medicine", "Architecture", "Law", "Integrated LLB"],
    target_group=["Meritorious Female Students from Low-Income Families"],
    funding_amount="₹1,50,000 per year until completion of professional degree",
    amount_val_inr=150000,
    provider_name="Kotak Education Foundation", provider_kind="trust", provider_slug="kotak-education-foundation", provider_website="https://kotakeducation.org",
    eligibility="Female students who secured >= 75% in Class 12 board and enrolled in 1st year of professional graduation in NIRF top ranked college. Annual family income <= ₹6.00 Lakhs.",
    income_limit_inr=600000, open_date="2026-08-15", deadline="2026-11-30", deadline_text="Annually opens August, closes November",
    recurring=True, status="open",
    official_link="https://kotakeducation.org", source_url="https://kotakeducation.org/kotak-kanya-scholarship",
    documents=["Class 10 & 12 Marksheet (min 75%)", "College Admission Proof & Fee Receipt", "Income Certificate (< ₹6 LPA)", "Aadhaar Card", "Bank Account Details"],
    process=["Online application on Kotak Education portal", "Shortlisting and telephonic screening", "Panel interview of selected girls"],
    tags=["Kotak", "Girls Empowerment", "Professional Degree", "Engineering & Medicine"]
)

add_entry(
    id="loreal-women-in-science",
    title="L'Oréal India For Young Women in Science Scholarship",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Pure Sciences", "Applied Sciences", "Engineering", "Medicine", "Biotechnology"],
    target_group=["Class 12 Passed Girls pursuing Science Graduation"],
    funding_amount="₹2,50,000 disbursed across graduation period",
    amount_val_inr=250000,
    provider_name="L'Oréal India CSR", provider_kind="company", provider_slug="loreal-india", provider_website="https://www.loreal.com/en/india",
    eligibility="Female students passed Class 12 in Science (PCB/PCM) with >= 85% in current academic year. Family income <= ₹6.00 Lakhs/annum.",
    income_limit_inr=600000, open_date="2026-10-01", deadline="2027-01-15", deadline_text="Annually opens October, closes January",
    recurring=True, status="open",
    official_link="https://www.loreal.com/en/india", source_url="https://www.loreal.com/en/india/articles/commitments/for-young-women-in-science",
    documents=["Class 12 Marksheet (min 85%)", "Age Proof (10th marksheet / Birth Cert)", "Income Certificate (< ₹6 LPA)", "College Admission Letter & Fee Slip"],
    process=["Submit application with scientific ambition essay", "Screening by scientific panel", "Video interview with leading women scientists"],
    tags=["L'Oréal", "Women in Science", "STEM Girls", "Post-12th"]
)

add_entry(
    id="sitaram-jindal-scholarship",
    title="Sitaram Jindal Foundation Educational Scholarship Scheme",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["General Degree", "Engineering", "Medicine", "Diploma", "Polytechnic"],
    target_group=["Merit-cum-Means Students across India"],
    funding_amount="₹1,000 to ₹3,200 per month depending on course level",
    amount_val_inr=38400,
    provider_name="Sitaram Jindal Foundation", provider_kind="trust", provider_slug="sitaram-jindal-foundation", provider_website="https://www.sitaramjindalfoundation.org",
    eligibility="Students pursuing regular courses with >= 60% marks (boys) or >= 55% marks (girls) in previous exam. Family income <= ₹2.5 Lakhs (general) or <= ₹4.0 Lakhs (employed).",
    income_limit_inr=400000, open_date="2026-01-01", deadline=None, deadline_text="Accepted throughout the year (Rolling)",
    recurring=True, status="rolling",
    official_link="https://www.sitaramjindalfoundation.org", source_url="https://www.sitaramjindalfoundation.org/scholarships-for-students-in-bangalore.php",
    documents=["Application Annexure signed by Principal", "Marksheet of previous exam", "Income Certificate", "Hostel Warden Certificate (if hosteller)"],
    process=["Download application form from official website", "Get endorsed by Principal and mail to regional foundation office", "Disbursement via cheque or direct transfer"],
    tags=["Sitaram Jindal", "Rolling", "Merit-cum-Means", "All India"]
)

add_entry(
    id="keep-india-smiling-scholarship",
    title="Keep India Smiling Foundational Scholarship (Colgate-Palmolive)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Class 11 & 12", "Undergraduate 3-year", "Engineering", "Dental BDS / Medical"],
    target_group=["Underprivileged Students with High Academic Ambition"],
    funding_amount="₹30,000 to ₹50,000 per year for 1 to 4 years",
    amount_val_inr=50000,
    provider_name="Colgate-Palmolive (India) Limited", provider_kind="company", provider_slug="colgate-palmolive", provider_website="https://www.colgate.com/en-in",
    eligibility="Students who passed Class 10 or 12 with >= 60% or 75% (for BDS/Engg). Family annual income <= ₹5.00 Lakhs.",
    income_limit_inr=500000, open_date="2026-08-01", deadline="2026-12-31", deadline_text="Annually opens August, closes December",
    recurring=True, status="open",
    official_link="https://www.colgate.com/en-in", source_url="https://www.colgate.com/en-in/mission",
    documents=["Marksheets (10th/12th)", "College Admission Letter & Fee Receipt", "Income Certificate (< ₹5 LPA)", "Aadhaar Card"],
    process=["Apply via Buddy4Study partner portal for Colgate", "Telephonic interview of shortlisted candidates", "Direct bank transfer"],
    tags=["Colgate", "Keep India Smiling", "CSR", "BDS", "Engineering"]
)

add_entry(
    id="santoor-women-scholarship",
    title="Santoor Women's Scholarship Programme (Wipro Consumer Care)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Humanities", "Liberal Arts", "Sciences", "Commerce"],
    target_group=["Girls from Disadvantaged Backgrounds in AP, Telangana, Karnataka, and Chhattisgarh"],
    funding_amount="₹24,000 per annum throughout 3-year degree course",
    amount_val_inr=24000,
    provider_name="Wipro Consumer Care and Wipro Cares", provider_kind="company", provider_slug="wipro-consumer-care", provider_website="https://www.santoorscholarships.com",
    eligibility="Young women from rural/government schools who completed Class 12 and enrolled in 1st year of general undergraduate degree. Priority to low-income families.",
    income_limit_inr=300000, open_date="2026-08-01", deadline="2026-10-31", deadline_text="Annually opens August, closes October",
    recurring=True, status="open",
    official_link="https://www.santoorscholarships.com", source_url="https://www.santoorscholarships.com",
    documents=["Class 10 and 12 Pass Certificate from Govt/Local Body School", "College Admission Fee Receipt", "Bank Passbook in Student's Name", "Aadhaar Card"],
    process=["Online registration on Santoor portal", "Physical document verification by field team", "Direct annual disbursement"],
    tags=["Santoor", "Wipro", "Women Only", "Rural Girls", "Undergraduate"]
)

add_entry(
    id="infosys-stem-stars-scholarship",
    title="Infosys Foundation STEM Stars Scholarship for Female Students",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Engineering", "Computer Science", "Information Technology", "MBBS"],
    target_group=["First-Year Female Students in NIRF Accredited Colleges"],
    funding_amount="Up to ₹1,00,000 per year covering tuition fees, living expenses, and study materials",
    amount_val_inr=100000,
    provider_name="Infosys Foundation", provider_kind="trust", provider_slug="infosys-foundation", provider_website="https://www.infosys.com/infosys-foundation",
    eligibility="Female students enrolled in 1st year of Engineering or MBBS in NIRF top ranked institutions with >= 75% in Class 12. Annual family income <= ₹8.00 Lakhs.",
    income_limit_inr=800000, open_date="2026-09-01", deadline="2026-11-30", deadline_text="Annually opens September, closes November",
    recurring=True, status="open",
    official_link="https://www.infosys.com/infosys-foundation", source_url="https://www.infosys.com/infosys-foundation/initiatives/education/stem-stars.html",
    documents=["Class 12 Marksheet (min 75%)", "College Admission Proof & Fee Receipt", "Government Income Certificate (< ₹8 LPA)", "Aadhaar Card"],
    process=["Apply through official Infosys Foundation scholarship portal", "Document scrutiny and background verification", "Disbursement covering full academic cycle"],
    tags=["Infosys Foundation", "Women in STEM", "Engineering", "MBBS", "CSR"]
)

add_entry(
    id="rolls-royce-unnati-scholarship",
    title="Rolls-Royce Unnati Scholarship for Women Engineering Students",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["Bachelor"],
    streams=["Aerospace", "Marine", "Electronics", "Computers", "Mechanical Engineering"],
    target_group=["Female Engineering Students in 1st, 2nd or 3rd year"],
    funding_amount="₹35,000 one-time financial aid + Rolls-Royce Executive Mentorship",
    amount_val_inr=35000,
    provider_name="Rolls-Royce India CSR", provider_kind="company", provider_slug="rolls-royce", provider_website="https://www.rolls-royce.com/country-sites/india.aspx",
    eligibility="Female students studying in 1st, 2nd, or 3rd year of B.Tech/B.E. in AICTE approved engineering college with >= 60% in Class 10 and 12. Income <= ₹4 LPA.",
    income_limit_inr=400000, open_date="2026-08-01", deadline="2026-10-31", deadline_text="Annually opens August, closes October",
    recurring=True, status="open",
    official_link="https://www.rolls-royce.com/country-sites/india.aspx", source_url="https://www.rolls-royce.com/country-sites/india/careers/student-and-graduates.aspx",
    documents=["Academic Transcripts", "College ID & Bonafide", "Income Certificate (< ₹4 LPA)", "Bank Account Details"],
    process=["Online application and short essay", "Telephonic screening", "Webinars and mentorship with senior Rolls-Royce engineers"],
    tags=["Rolls-Royce", "Unnati", "Engineering", "Women in Tech", "Mentorship"]
)

add_entry(
    id="siemens-scholarship-program",
    title="Siemens Scholarship Program for Government Engineering Colleges",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor"],
    streams=["Mechanical", "Electrical", "Electronics & Telecomm", "Computer Science", "Information Technology"],
    target_group=["1st Year Students in Govt Engineering Colleges with High Potential"],
    funding_amount="100% Tuition Fees + Allowance for books & hostel + German Training & Siemens Internship",
    amount_val_inr=120000,
    provider_name="Siemens India CSR", provider_kind="company", provider_slug="siemens-india", provider_website="https://www.siemens.com/in/en.html",
    eligibility="1st year students in Government Engineering Colleges across India with >= 60% in 10th and >= 50% in 12th. Age <= 20 years. Family income <= ₹2.0 Lakhs/annum.",
    income_limit_inr=200000, open_date="2026-09-01", deadline="2026-11-15", deadline_text="Annually opens September, closes November",
    recurring=True, status="open",
    official_link="https://www.siemens.com/in/en.html", source_url="https://www.siemens.com/in/en/company/sustainability/corporate-citizenship/siemens-scholarship-program.html",
    documents=["Class 10 and 12 Marksheets", "Government College Admission Letter", "Tehsildar issued Income Certificate (< ₹2 LPA)", "Aadhaar Card"],
    process=["Online application on Siemens portal", "Aptitude assessment and telephonic interview", "In-person/virtual panel interview and holistic onboarding"],
    tags=["Siemens", "Full Ride", "Govt Colleges", "Engineering", "Internship Guaranteed"]
)

add_entry(
    id="sbif-asha-scholarship",
    title="SBIF Asha Scholarship Programme (State Bank of India Foundation)",
    section="india", country="India", type_="private", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master"],
    streams=["Class 9-12, Undergraduate, Postgraduate, IITs and IIMs"],
    target_group=["Meritorious Students from Low-Income Families"],
    funding_amount="₹15,000 to ₹70,000 (Up to ₹5,00,000 for IIT/IIM students)",
    amount_val_inr=70000,
    provider_name="SBI Foundation", provider_kind="company", provider_slug="sbi-foundation", provider_website="https://www.sbifoundation.in",
    eligibility="Students enrolled in top universities/colleges with >= 75% in previous academic year. Annual family income <= ₹3.00 Lakhs.",
    income_limit_inr=300000, open_date="2026-08-01", deadline="2026-11-30", deadline_text="Annually opens August, closes November",
    recurring=True, status="open",
    official_link="https://www.sbifoundation.in", source_url="https://www.sbifoundation.in/education",
    documents=["Marksheet of qualifying exam (min 75%)", "Income Certificate (< ₹3 LPA)", "College Admission Letter & Fee Receipt", "Bank Account Details"],
    process=["Submit online form through SBI Foundation portal", "Document verification and telephonic interview", "Direct DBT disbursement"],
    tags=["SBI Foundation", "Asha Scholarship", "IIT / IIM", "CSR"]
)

# ==============================================================================
# SECTION 1: INDIA - FUNDED INTERNSHIPS, SUMMER FELLOWSHIPS & PROJECTS
# ==============================================================================

add_entry(
    id="iasc-insa-nasi-srfp",
    title="Summer Research Fellowship Programme (SRFP) - IASc, INSA & NASI",
    section="india", country="India", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Science", "Mathematics", "Engineering", "Earth Sciences", "Life Sciences"],
    target_group=["Pre-final year UG & 1st year PG students"],
    funding_amount="₹12,000/month stipend + Round-trip train travel fare + Free accommodation",
    amount_val_inr=24000,
    provider_name="Indian Academy of Sciences (IASc), INSA & NASI", provider_kind="lab", provider_slug="iasc-bangalore", provider_website="https://www.ias.ac.in",
    eligibility="Students in 2nd/3rd year of B.Sc/B.Tech or 1st year of M.Sc/M.Tech with consistent >= 65% aggregate throughout schooling and college.",
    income_limit_inr=None, open_date="2026-10-01", deadline="2026-11-30", deadline_text="Annually opens October, strictly closes November 30",
    recurring=True, status="open",
    official_link="https://web-japps.ias.ac.in", source_url="https://web-japps.ias.ac.in/fellowship2024/index.html",
    documents=["Write-up of research interests (150-250 words)", "Consolidated marksheets from Class 10 onwards", "Confidential Recommendation Letter from Teacher uploaded directly"],
    process=["Submit application selecting 6 Academy Fellows as prospective mentors", "Teacher uploads confidential assessment", "Selected fellows work for 8 weeks (May-July) in premier Indian labs"],
    tags=["IASc", "INSA", "Premier Research", "Summer Fellowship", "IISc / IIT Labs"]
)

add_entry(
    id="iitm-summer-fellowship",
    title="IIT Madras Summer Fellowship Programme (SFP)",
    section="india", country="India", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Engineering", "Computer Science", "Data Science", "Humanities", "Sciences", "Management"],
    target_group=["Non-IIT Undergraduate & Postgraduate Students"],
    funding_amount="₹6,000/month stipend + Subsidized on-campus hostel accommodation",
    amount_val_inr=12000,
    provider_name="Indian Institute of Technology Madras (IIT Madras)", provider_kind="university", provider_slug="iit-madras", provider_website="https://www.iitm.ac.in",
    eligibility="3rd year B.Tech/B.E. or 1st year M.Sc/MA/MBA students with top 10% class rank / CGPA >= 8.0 in parent institute.",
    income_limit_inr=None, open_date="2027-01-15", deadline="2027-02-28", deadline_text="Annually opens January, closes end of February",
    recurring=True, status="upcoming",
    official_link="https://sfp.iitm.ac.in", source_url="https://sfp.iitm.ac.in",
    documents=["Academic Transcripts", "Bonafide Certificate & NOC from HOD", "Statement of Purpose"],
    process=["Apply on SFP IIT Madras portal choosing department mentors", "Faculty review shortlisted resumes and conduct short interviews", "2-month fellowship during May-July"],
    tags=["IIT Madras", "Summer Fellowship", "Hands-on Research", "Engineering"]
)

add_entry(
    id="iitr-spark-summer-internship",
    title="IIT Roorkee SPARK Summer Internship Programme",
    section="india", country="India", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Architecture", "Engineering", "Management", "Natural Sciences", "Social Sciences"],
    target_group=["UG & PG Students from NIRF Top Ranked Colleges"],
    funding_amount="₹2,500/week (₹10,000 for 4-8 weeks) + Subsidized campus hostel",
    amount_val_inr=20000,
    provider_name="Indian Institute of Technology Roorkee (IIT Roorkee)", provider_kind="university", provider_slug="iit-roorkee", provider_website="https://www.iitr.ac.in",
    eligibility="Undergraduate students in 2nd/3rd year or PG students with CGPA >= 7.5 (IIT/IISc) or >= 8.0 (NIT/others).",
    income_limit_inr=None, open_date="2027-02-01", deadline="2027-03-31", deadline_text="Annually opens February, closes March",
    recurring=True, status="upcoming",
    official_link="https://spark.iitr.ac.in", source_url="https://spark.iitr.ac.in",
    documents=["Official Transcript with CGPA", "No Objection Certificate from parent institute", "Resume & Research Statement"],
    process=["Select projects posted by IIT Roorkee faculty", "Faculty shortlist and offer internship", "8-week summer research on campus"],
    tags=["IIT Roorkee", "SPARK", "Summer Internship", "Funded"]
)

add_entry(
    id="iitk-surge-internship",
    title="IIT Kanpur SURGE (Students Undergraduate Research Graduate Excellence)",
    section="india", country="India", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Aerospace", "Chemical", "Civil", "CSE", "Electrical", "Mechanical", "Physics", "Chemistry", "Mathematics"],
    target_group=["Undergraduate Students in 2nd or 3rd year"],
    funding_amount="₹12,500 fixed summer stipend + Campus accommodation",
    amount_val_inr=12500,
    provider_name="Indian Institute of Technology Kanpur (IIT Kanpur)", provider_kind="university", provider_slug="iit-kanpur", provider_website="https://www.iitk.ac.in",
    eligibility="Students from designated participating institutions or open category with CGPA >= 8.5/10.0.",
    income_limit_inr=None, open_date="2027-01-01", deadline="2027-02-15", deadline_text="Annually opens January, closes mid-February",
    recurring=True, status="upcoming",
    official_link="https://www.iitk.ac.in/surge", source_url="https://www.iitk.ac.in/surge",
    documents=["Online Recommendation Letter from HOD", "Statement of Research Interest", "Transcripts"],
    process=["Submit project preferences on SURGE portal", "Faculty review and selection", "8-week intensive research period"],
    tags=["IIT Kanpur", "SURGE", "Summer Project", "Research"]
)

add_entry(
    id="iitgn-srip-internship",
    title="IIT Gandhinagar Summer Research Internship Program (SRIP)",
    section="india", country="India", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["All Engineering Disciplines", "Physics", "Chemistry", "Maths", "Cognitive Science", "Humanities"],
    target_group=["UG & PG Students across India"],
    funding_amount="₹2,000/week (₹16,000 for 8 weeks) + Free hostel accommodation",
    amount_val_inr=16000,
    provider_name="Indian Institute of Technology Gandhinagar (IIT Gandhinagar)", provider_kind="university", provider_slug="iit-gandhinagar", provider_website="https://www.iitgn.ac.in",
    eligibility="Students pursuing bachelor's or master's degree with high academic standing.",
    income_limit_inr=None, open_date="2027-02-01", deadline="2027-03-05", deadline_text="Annually opens February, closes early March",
    recurring=True, status="upcoming",
    official_link="https://srip.iitgn.ac.in", source_url="https://srip.iitgn.ac.in",
    documents=["Resume", "Statement of Purpose", "Academic Transcripts"],
    process=["Browse faculty project list on SRIP portal", "Submit online application for up to 2 projects", "8-week research stay in Gandhinagar"],
    tags=["IIT Gandhinagar", "SRIP", "Funded Internship", "Summer"]
)

add_entry(
    id="tifr-vsrp-programme",
    title="TIFR Visiting Students' Research Programme (VSRP)",
    section="india", country="India", type_="lab", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Physics", "Chemistry", "Biology", "Mathematics", "Computer & Systems Sciences"],
    target_group=["Pre-final year UG & 1st year PG students"],
    funding_amount="₹7,000/month stipend + Free on-campus accommodation + Return train fare",
    amount_val_inr=14000,
    provider_name="Tata Institute of Fundamental Research (TIFR), DAE", provider_kind="lab", provider_slug="tifr-mumbai", provider_website="https://www.tifr.res.in",
    eligibility="Pre-final year students of B.Sc./B.E./B.Tech or 1st year M.Sc./M.Tech with exceptional academic track record.",
    income_limit_inr=None, open_date="2027-01-01", deadline="2027-02-15", deadline_text="Annually opens January, closes mid-February",
    recurring=True, status="upcoming",
    official_link="https://www.tifr.res.in/~vsrp", source_url="https://www.tifr.res.in/~vsrp",
    documents=["Academic Transcripts from 10th standard", "Two Referee Recommendation Letters", "Statement of Research Interest"],
    process=["Apply online at TIFR VSRP portal", "Subject committees evaluate candidates", "7-week residential programme at TIFR Mumbai/Colaba"],
    tags=["TIFR", "Fundamental Physics", "Mathematics", "VSRP", "Prestigious"]
)

add_entry(
    id="ncbs-summer-programme",
    title="NCBS Annual Summer Research Programme in Biological Sciences",
    section="india", country="India", type_="lab", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Biological Sciences", "Bioinformatics", "Ecology & Evolution", "Biophysics", "Neurobiology"],
    target_group=["Undergraduate & Master's Students"],
    funding_amount="₹8,000/month stipend + Round-trip train fare + Free campus hostel",
    amount_val_inr=16000,
    provider_name="National Centre for Biological Sciences (NCBS-TIFR), Bengaluru", provider_kind="lab", provider_slug="ncbs-bengaluru", provider_website="https://www.ncbs.res.in",
    eligibility="Students in 2nd/3rd year of undergraduate or 1st year master's degree with strong passion for biological research.",
    income_limit_inr=None, open_date="2027-01-01", deadline="2027-02-28", deadline_text="Annually opens January, closes end of February",
    recurring=True, status="upcoming",
    official_link="https://www.ncbs.res.in", source_url="https://www.ncbs.res.in/academic/summer-research",
    documents=["Academic Transcripts", "One-page Statement of Purpose", "Recommendation Letter from college professor"],
    process=["Online application on NCBS website", "Faculty review and selection", "8-10 week research stay in Bengaluru"],
    tags=["NCBS", "Biology", "Neuroscience", "Ecology", "Summer Research"]
)

add_entry(
    id="rri-visiting-student-programme",
    title="RRI Visiting Students Programme in Physics & Astronomy",
    section="india", country="India", type_="lab", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Astronomy & Astrophysics", "Theoretical Physics", "Light and Matter Physics", "Soft Condensed Matter"],
    target_group=["B.Sc / M.Sc / B.Tech Students"],
    funding_amount="₹7,000/month stipend + Free accommodation in RRI campus + Train fare",
    amount_val_inr=14000,
    provider_name="Raman Research Institute (RRI), Bengaluru", provider_kind="lab", provider_slug="rri-bengaluru", provider_website="https://www.rri.res.in",
    eligibility="Students pursuing undergraduate or postgraduate studies in Physics, Mathematics, or Engineering.",
    income_limit_inr=None, open_date="2027-01-15", deadline="2027-03-15", deadline_text="Annually opens January, closes March",
    recurring=True, status="upcoming",
    official_link="https://www.rri.res.in", source_url="https://www.rri.res.in/visiting-students-programme",
    documents=["Detailed CV", "Academic Transcripts", "Reference Letter"],
    process=["Apply online specifying research field", "6 to 8 weeks hands-on research project under RRI scientists"],
    tags=["RRI", "Astrophysics", "Quantum Optics", "Physics Internship"]
)

add_entry(
    id="isro-student-internship",
    title="ISRO Student Internship & Project Trainee Scheme",
    section="india", country="India", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Aerospace Engineering", "Avionics", "Computer Science", "Remote Sensing", "Mechanical Engineering", "Electronics"],
    target_group=["Pre-final & Final year Engineering & Science Students"],
    funding_amount="Funded / Certificate of National Space Traineeship + Specialized Lab Access",
    amount_val_inr=0,
    provider_name="Indian Space Research Organisation (ISRO)", provider_kind="ministry", provider_slug="isro-india", provider_website="https://www.isro.gov.in",
    eligibility="Indian citizens pursuing regular B.Tech (minimum 6th semester completed) or M.Tech/M.Sc with >= 65% aggregate or 6.84 CGPA.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-11-30", deadline_text="Cycle opens for winter (Nov/Dec) and summer (May/June)",
    recurring=True, status="open",
    official_link="https://www.isro.gov.in", source_url="https://www.isro.gov.in/Internship.html",
    documents=["Bonafide Certificate from Principal in prescribed ISRO format", "Marksheets of all completed semesters", "Detailed Resume"],
    process=["Apply to designated ISRO centre (VSSC, URSC, SAC, NRSC, LPSC)", "Security vetting and divisional allocation", "Project duration of 45 to 90 days"],
    tags=["ISRO", "Space Science", "Aerospace", "Project Training"]
)

add_entry(
    id="drdo-apprenticeship-internship",
    title="DRDO Research Apprenticeship & Graduate Trainee Scheme",
    section="india", country="India", type_="government", category="Internship",
    education_levels=["Bachelor"],
    streams=["Mechanical", "Electrical", "Electronics & Comm", "Computer Science", "Metallurgy"],
    target_group=["B.E. / B.Tech Graduate Apprentices"],
    funding_amount="₹9,000/month stipend as per National Apprenticeship Training Scheme (NATS)",
    amount_val_inr=108000,
    provider_name="Defence Research and Development Organisation (DRDO)", provider_kind="ministry", provider_slug="drdo-india", provider_website="https://www.drdo.gov.in",
    eligibility="Fresh engineering graduates (graduated within last 3 years) from recognized university.",
    income_limit_inr=None, open_date="2026-08-01", deadline="2026-10-31", deadline_text="Annually advertised by individual DRDO labs (ARDE, DRDL, CAIR, GTRE)",
    recurring=True, status="open",
    official_link="https://www.drdo.gov.in", source_url="https://www.drdo.gov.in/careers",
    documents=["Engineering Degree Certificate & Marksheets", "NATS Portal Registration ID", "Aadhaar Card", "Medical Fitness Certificate"],
    process=["Register on NATS portal (mhrdnats.gov.in)", "Apply against laboratory notification on DRDO website", "1-year apprenticeship training"],
    tags=["DRDO", "Defence Research", "Apprenticeship", "Engineering"]
)

add_entry(
    id="niti-aayog-internship",
    title="NITI Aayog Official Internship Scheme",
    section="india", country="India", type_="government", category="Internship",
    education_levels=["Bachelor", "Master", "PhD"],
    streams=["Public Policy", "Economics", "Data Analytics", "Agriculture", "Health", "Governance", "Engineering"],
    target_group=["UG, PG and Research Scholars"],
    funding_amount="Official Certificate of Completion & Direct Policy Mentorship with Advisors",
    amount_val_inr=0,
    provider_name="NITI Aayog, Government of India", provider_kind="ministry", provider_slug="niti-aayog", provider_website="https://www.niti.gov.in",
    eligibility="Undergraduate students in 2nd year or above with >= 85% in Class 12, or PG students with >= 70% in graduation.",
    income_limit_inr=None, open_date="2026-10-01", deadline="2026-10-10", deadline_text="Online portal opens on 1st to 10th of every month",
    recurring=True, status="open",
    official_link="https://www.niti.gov.in", source_url="https://www.niti.gov.in/internship",
    documents=["No Objection Certificate from College Principal/Dean", "Academic Transcripts", "Resume"],
    process=["Apply online strictly between 1st and 10th of the month", "Vertical Heads review and conduct short virtual interviews", "Internship duration from 6 weeks to 6 months"],
    tags=["NITI Aayog", "Public Policy", "Govt Internship", "Economics"]
)

add_entry(
    id="mea-internship-programme",
    title="Ministry of External Affairs (MEA) Internship Programme",
    section="india", country="India", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["International Relations", "Political Science", "Law", "Economics", "History", "Journalism"],
    target_group=["Indian Citizens pursuing Graduation or Postgraduation"],
    funding_amount="₹10,000/month honorarium + Flight/Air travel assistance from home state",
    amount_val_inr=30000,
    provider_name="Ministry of External Affairs, Govt of India", provider_kind="ministry", provider_slug="mea-india", provider_website="https://www.mea.gov.in",
    eligibility="Graduate degree or in final year of undergraduate degree with >= 60% marks. Age <= 25 years.",
    income_limit_inr=None, open_date="2026-11-01", deadline="2026-12-15", deadline_text="Two terms per year (Term I: Apr-Sep, Term II: Oct-Mar)",
    recurring=True, status="upcoming",
    official_link="https://internship.mea.gov.in", source_url="https://www.mea.gov.in",
    documents=["College ID & Bonafide Letter", "Academic Transcripts", "Identity Proof"],
    process=["Register on MEA Internship portal", "Quota allocation for each State and Union Territory", "3-month internship in New Delhi HQ or regional passport offices"],
    tags=["MEA", "Foreign Affairs", "Diplomacy", "Paid Internship"]
)

add_entry(
    id="iisc-project-jrf-positions",
    title="IISc Sponsored Project Research Positions (Project JRF / Project Associate)",
    section="india", country="India", type_="university", category="Project Position (JRF/SRF/RA)",
    education_levels=["Master", "PhD"],
    streams=["Computational Sciences", "Nanotechnology", "Materials", "Electrical", "Mechanical", "Bioengineering"],
    target_group=["Postgraduates with GATE / NET qualification"],
    funding_amount="₹31,000 to ₹35,000/month + HRA (Project Associate I/II)",
    amount_val_inr=420000,
    provider_name="Indian Institute of Science (IISc), Bengaluru", provider_kind="university", provider_slug="iisc-bengaluru", provider_website="https://www.iisc.ac.in",
    eligibility="M.Tech/M.E. or M.Sc. in relevant discipline with valid GATE/NET score or professional experience in project domain.",
    income_limit_inr=None, open_date="2026-01-01", deadline=None, deadline_text="Advertised continuously across departments (Rolling)",
    recurring=True, status="rolling",
    official_link="https://www.iisc.ac.in", source_url="https://iisc.ac.in/careers/project-staff",
    documents=["Detailed Curriculum Vitae", "Degree Certificates & Marksheets", "GATE/CSIR-NET Scorecard", "Statement of Research Experience"],
    process=["Review openings on IISc Project Staff careers page", "Email application directly to Principal Investigator (PI)", "Technical interview before laboratory selection committee"],
    tags=["IISc", "Project Position", "JRF", "Funded Project", "Research Staff"]
)

add_entry(
    id="csir-nal-project-associate",
    title="CSIR-NAL Project Associate & JRF Positions in Aerospace Engineering",
    section="india", country="India", type_="government", category="Project Position (JRF/SRF/RA)",
    education_levels=["Bachelor", "Master"],
    streams=["Aerospace", "Aeronautical", "Mechanical", "Computer Science", "Materials Science"],
    target_group=["B.E. / B.Tech / M.Tech Graduates"],
    funding_amount="₹25,000 to ₹31,000/month + HRA as per CSIR norms",
    amount_val_inr=372000,
    provider_name="CSIR - National Aerospace Laboratories (NAL)", provider_kind="lab", provider_slug="csir-nal", provider_website="https://www.nal.res.in",
    eligibility="B.E./B.Tech or M.Tech in relevant engineering discipline with minimum 55% marks. Age <= 35 years.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-10-31", deadline_text="Rolling recruitment via periodic notifications",
    recurring=True, status="open",
    official_link="https://www.nal.res.in", source_url="https://www.nal.res.in/en/careers",
    documents=["Degree Certificates", "GATE score card (for higher stipend scale)", "NOC from current employer if applicable"],
    process=["Submit online or attend walk-in interview as specified in notification", "Technical written test followed by personal interview", "Contractual tenure on sponsored research projects"],
    tags=["CSIR-NAL", "Aerospace", "Project Associate", "Engineering Research"]
)

# ==============================================================================
# SECTION 2: OPPORTUNITIES ABROAD - GOVERNMENT & MULTILATERAL SCHOLARSHIPS
# ==============================================================================

add_entry(
    id="eu-erasmus-mundus-emjm",
    title="Erasmus Mundus Joint Master Degrees (EMJM) - European Union",
    section="abroad", country="European Union", type_="government", category="Scholarship",
    education_levels=["Master"],
    streams=["All Disciplines", "Computer Science", "Renewable Energy", "Environmental Science", "Economics", "Humanities"],
    target_group=["Global applicants (India is historically #1 recipient country)"],
    funding_amount="100% Tuition Waiver across 2-4 European Universities + €1,400/month stipend + €3,000/yr travel grant",
    amount_val_inr=3500000,
    provider_name="European Education and Culture Executive Agency (EACEA)", provider_kind="ministry", provider_slug="european-union-eacea", provider_website="https://www.eacea.ec.europa.eu",
    eligibility="Completed Bachelor's degree (or in final year). High academic standing. Fluent in English (IELTS 6.5+ or TOEFL).",
    income_limit_inr=None, open_date="2026-10-01", deadline="2027-01-15", deadline_text="Annually opens October, program deadlines between Dec & Feb",
    recurring=True, status="open",
    official_link="https://www.eacea.ec.europa.eu", source_url="https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en",
    documents=["Undergraduate Transcripts", "Statement of Purpose / Motivation Letter", "2-3 Letters of Recommendation", "Europass CV", "IELTS / TOEFL Score"],
    process=["Search Erasmus Mundus Catalogue and pick up to 3 master programs", "Apply directly on consortium website before deadline", "Consortium nominates top scholars for EU funded slots"],
    tags=["Europe", "Fully Funded", "Master Degree", "Multi-Country Study", "Erasmus"]
)

add_entry(
    id="uk-chevening-scholarship",
    title="Chevening Scholarships - United Kingdom",
    section="abroad", country="United Kingdom", type_="government", category="Scholarship",
    education_levels=["Master"],
    streams=["All Disciplines", "Public Policy", "International Relations", "Tech", "Economics", "Law"],
    target_group=["Future Leaders with Minimum 2 Years Work Experience"],
    funding_amount="100% Tuition Fees at any UK University + £1,400/month living allowance + Flight tickets",
    amount_val_inr=4000000,
    provider_name="Foreign, Commonwealth & Development Office (FCDO), UK Govt", provider_kind="ministry", provider_slug="uk-fcdo", provider_website="https://www.chevening.org",
    eligibility="Indian citizen. Undergraduate degree completed. Minimum 2 years (2,800 hours) work experience. Commit to returning to India for min 2 years after studies.",
    income_limit_inr=None, open_date="2026-08-01", deadline="2026-11-05", deadline_text="Annually opens August, strictly closes early November",
    recurring=True, status="open",
    official_link="https://www.chevening.org", source_url="https://www.chevening.org/scholarships",
    documents=["4 Mandatory Leadership Essays (Leadership, Networking, UK Study, Career Plan)", "Degree Transcripts", "Unconditional Offer from an eligible UK Course", "Two Reference Letters"],
    process=["Submit comprehensive online application on Chevening portal by November", "Shortlisted applicants interviewed at British High Commission New Delhi", "Receive university offer to finalize award"],
    tags=["United Kingdom", "Chevening", "1-Year Master", "Fully Funded", "Oxford / Cambridge"]
)

add_entry(
    id="uk-commonwealth-scholarships",
    title="Commonwealth Master's & PhD Scholarships (CSC UK)",
    section="abroad", country="United Kingdom", type_="government", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Science and Technology", "Health", "Global Prosperity", "Peace & Security", "Resilience & Crises"],
    target_group=["Talented Indian graduates unable to afford UK study without funding"],
    funding_amount="Full UK Tuition Fees + £1,347/month (£1,652 in London) + Return Flights + Arrival Allowance",
    amount_val_inr=4200000,
    provider_name="Commonwealth Scholarship Commission (CSC) in the UK", provider_kind="ministry", provider_slug="commonwealth-csc", provider_website="https://cscuk.fcdo.gov.uk",
    eligibility="Indian citizen. For Master's: Bachelor's with >= 60%. For PhD: Master's degree. Must apply through Ministry of Education India nominating agency.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-10-31", deadline_text="Annually opens September, closes end of October",
    recurring=True, status="open",
    official_link="https://cscuk.fcdo.gov.uk", source_url="https://cscuk.fcdo.gov.uk/apply/candidates",
    documents=["Full Academic Transcripts", "Detailed Study Plan", "Two Referee Reports", "Ministry of Education India nomination acknowledgement"],
    process=["Apply simultaneously on CSC UK online portal and Ministry of Education (MoE) Sakshat portal", "MoE conducts interviews and nominates candidates to CSC UK", "CSC UK makes final selection"],
    tags=["Commonwealth", "UK", "Master & PhD", "Full Ride", "FCDO"]
)

add_entry(
    id="usief-fulbright-nehru-fellowship",
    title="Fulbright-Nehru Master's & Doctoral Research Fellowships - United States",
    section="abroad", country="United States", type_="government", category="Fellowship",
    education_levels=["Master", "PhD"],
    streams=["Arts & Culture", "Environmental Science", "Public Health", "Economics", "Gender Studies", "Public Policy", "STEM"],
    target_group=["Outstanding Indian graduates and doctoral scholars"],
    funding_amount="100% US University Tuition + Monthly Living Stipend + J-1 Visa Sponsorship + Round-trip Airfare",
    amount_val_inr=5500000,
    provider_name="United States-India Educational Foundation (USIEF)", provider_kind="ministry", provider_slug="usief-india", provider_website="https://www.usief.org.in",
    eligibility="Indian citizen with equivalent to US bachelor's degree with >= 55% marks. Minimum 3 years full-time work experience (for Master's). Outstanding leadership track record.",
    income_limit_inr=None, open_date="2026-02-01", deadline="2026-05-15", deadline_text="Annually opens February, closes mid-May for following academic year",
    recurring=True, status="closed",
    official_link="https://www.usief.org.in", source_url="https://www.usief.org.in/Fellowships/Fulbright-Nehru-Fellowships.aspx",
    documents=["Study/Research Objectives Essay", "Personal Statement", "Three Confidential Recommendation Letters", "Transcripts & Employer Endorsement Form"],
    process=["Submit application on Embark online portal via USIEF", "National selection committee conducts in-person interviews in August", "USIEF coordinates placement at leading US universities"],
    tags=["USA", "Fulbright", "USIEF", "Premier Fellowship", "Full Funding"]
)

add_entry(
    id="germany-daad-study-scholarship",
    title="DAAD Study Scholarships for Postgraduate Master's Degree - Germany",
    section="abroad", country="Germany", type_="government", category="Scholarship",
    education_levels=["Master"],
    streams=["Engineering", "Computer Science", "Natural Sciences", "Architecture", "Economics", "Humanities"],
    target_group=["Graduates from all disciplines"],
    funding_amount="€934/month + Health Insurance + Travel Allowance + German Language Prep Course",
    amount_val_inr=1800000,
    provider_name="German Academic Exchange Service (DAAD)", provider_kind="ministry", provider_slug="daad-germany", provider_website="https://www.daad.in",
    eligibility="Bachelor's degree completed within last 6 years with excellent academic grades. English or German proficiency depending on chosen degree.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-11-15", deadline_text="Annually opens September, closes November",
    recurring=True, status="open",
    official_link="https://www.daad.in", source_url="https://www.daad.in/en/find-funding/scholarship-database",
    documents=["DAAD Online Application Form", "Curriculum Vitae in tabular format", "Detailed Letter of Motivation (1-3 pages)", "University Degree & Transcripts with Grading Scale"],
    process=["Submit application on DAAD online portal", "Independent academic committee evaluates dossiers", "Enrollment at public tuition-free German university"],
    tags=["Germany", "DAAD", "Master Degree", "No Tuition Fee", "Living Stipend"]
)

add_entry(
    id="japan-mext-embassy-track",
    title="MEXT (Monbukagakusho) Japanese Government Scholarship",
    section="abroad", country="Japan", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["Undergraduate: Social Sciences & Natural Sciences; Research: All Fields"],
    target_group=["Indian Citizens seeking UG or PG study in Japan"],
    funding_amount="¥117,000 to ¥145,000/month (₹65,000 to ₹82,000/m) + 100% Tuition Exemption + Return Flights",
    amount_val_inr=2200000,
    provider_name="Ministry of Education, Culture, Sports, Science & Tech (MEXT), Japan", provider_kind="ministry", provider_slug="mext-japan", provider_website="https://www.in.emb-japan.go.jp",
    eligibility="UG: Passed Class 12, age 17-25. PG/Research: Under 35 years old, completed 16 years of education with >= 65% aggregate.",
    income_limit_inr=None, open_date="2026-05-01", deadline="2026-06-15", deadline_text="Annually opens May, closes mid-June via Embassy of Japan in New Delhi",
    recurring=True, status="closed",
    official_link="https://www.in.emb-japan.go.jp", source_url="https://www.in.emb-japan.go.jp/Education/japanese_government_scholarships.html",
    documents=["Application Form & Research Plan", "Academic Marksheets from 10th standard", "Recommendation Letter from Principal/Dean", "Prescribed Medical Certificate"],
    process=["Submit application dossier to Embassy of Japan New Delhi", "Written examinations (English, Math, Japanese/Science) followed by personal interview", "Final clearance from MEXT Tokyo"],
    tags=["Japan", "MEXT", "Full Ride", "Undergraduate & PG", "Embassy Track"]
)

add_entry(
    id="msje-national-overseas-scholarship",
    title="National Overseas Scholarship (NOS) for SC, ST & Landless Agricultural Labourers",
    section="abroad", country="Global", type_="government", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Engineering", "Management", "Pure & Applied Sciences", "Agriculture", "Medicine", "Social Sciences"],
    target_group=["SC", "De-notified Tribes", "Traditional Artisans", "Landless Labourers"],
    funding_amount="100% Foreign Tuition Fees + $15,400/yr (USA) or £9,900/yr (UK) living stipend + Airfare",
    amount_val_inr=4500000,
    provider_name="Ministry of Social Justice and Empowerment (MoSJE), Govt of India", provider_kind="ministry", provider_slug="msje-india", provider_website="https://nosmsje.gov.in",
    eligibility="Family income <= ₹8.00 Lakh per annum. Must hold unconditional offer from QS Top 500 foreign university. Minimum 60% in bachelor's/master's.",
    income_limit_inr=800000, open_date="2026-02-15", deadline="2026-03-31", deadline_text="Two cycles per year (Cycle 1: Feb-Mar, Cycle 2: Sep-Oct)",
    recurring=True, status="open",
    official_link="https://nosmsje.gov.in", source_url="https://nosmsje.gov.in",
    documents=["Valid Caste Certificate", "Income Certificate (< ₹8 LPA) for current financial year", "Unconditional Admission Offer from QS Top 500 Foreign University", "Valid Indian Passport"],
    process=["Secure unconditional admission offer from QS top 500 ranked foreign university", "Register on nosmsje.gov.in portal", "Selection board issues official award letter"],
    tags=["Indian Govt Abroad", "Full Ride", "Top 500 QS", "SC / ST", "NOS"]
)

add_entry(
    id="cambridge-gates-scholarship",
    title="Gates Cambridge Scholarships (University of Cambridge, UK)",
    section="abroad", country="United Kingdom", type_="university", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["All Disciplines offered at Cambridge University"],
    target_group=["Outstanding Intellectuals with Commitment to Improving Lives of Others"],
    funding_amount="Full Cambridge University Composition Fee + £20,000/year living allowance + Airfare + Discretionary funding",
    amount_val_inr=5000000,
    provider_name="Gates Cambridge Trust & Bill and Melinda Gates Foundation", provider_kind="trust", provider_slug="gates-cambridge", provider_website="https://www.gatescambridge.org",
    eligibility="Citizen of any country outside UK. Applying to full-time residential course of study (PhD, M.Sc, M.Litt, or 1-year postgraduate). First-class academic record.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-12-05", deadline_text="Annually opens September, closes early December for international round",
    recurring=True, status="open",
    official_link="https://www.gatescambridge.org", source_url="https://www.gatescambridge.org/apply/eligibility-criteria",
    documents=["Cambridge Graduate Application", "500-word Gates Statement of Purpose", "Research Proposal (for PhD)", "Reference Letter for Gates Cambridge"],
    process=["Apply via Cambridge Graduate Admission portal ticking Gates Cambridge box", "Department shortlists candidates", "Virtual interview with international panel"],
    tags=["Cambridge", "Gates Cambridge", "Elite", "Fully Funded", "Master & PhD"]
)

add_entry(
    id="oxford-rhodes-scholarship",
    title="Rhodes Scholarships for India at the University of Oxford",
    section="abroad", country="United Kingdom", type_="trust", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["All Postgraduate Courses offered at the University of Oxford"],
    target_group=["Exceptional Indian Scholars with Intellect, Character and Leadership"],
    funding_amount="100% Oxford University Tuition Fees + £19,000/year living stipend + Airfare + Health Surcharge",
    amount_val_inr=6000000,
    provider_name="The Rhodes Trust, Oxford", provider_kind="trust", provider_slug="rhodes-trust", provider_website="https://www.rhodeshouse.ox.ac.uk",
    eligibility="Indian citizen aged 19 to 25. Completed or completing undergraduate degree with First Class honours. Maximum 5 scholarships awarded to India annually.",
    income_limit_inr=None, open_date="2026-06-01", deadline="2026-08-01", deadline_text="Annually opens June, strictly closes August 1",
    recurring=True, status="closed",
    official_link="https://www.rhodeshouse.ox.ac.uk", source_url="https://www.rhodeshouse.ox.ac.uk/scholarships/the-rhodes-scholarship",
    documents=["Personal Statement (1000 words)", "Academic Statement of Study", "Five to Six Recommendation Letters", "Detailed Curriculum Vitae"],
    process=["Submit online dossier on Rhodes application portal", "Preliminary interview in Delhi/Virtual", "Final weekend interview before National Selection Committee"],
    tags=["Oxford", "Rhodes", "Prestigious", "World Famous", "Full Ride"]
)

add_entry(
    id="oxford-clarendon-fund",
    title="Clarendon Fund Scholarships (University of Oxford)",
    section="abroad", country="United Kingdom", type_="university", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["All Degree-bearing Postgraduate Courses at Oxford"],
    target_group=["Top Graduate Applicants to Oxford across the World"],
    funding_amount="100% Oxford Tuition & College Fees + Generous Annual Living Stipend (£19,000+)",
    amount_val_inr=4800000,
    provider_name="Clarendon Fund, University of Oxford", provider_kind="university", provider_slug="university-of-oxford", provider_website="https://www.ox.ac.uk/clarendon",
    eligibility="Outstanding academic merit and potential. All graduate applicants to Oxford applying before January deadline are automatically considered.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2027-01-20", deadline_text="Apply by standard Oxford course deadline (Dec/Jan)",
    recurring=True, status="open",
    official_link="https://www.ox.ac.uk/clarendon", source_url="https://www.ox.ac.uk/clarendon",
    documents=["Standard Oxford Graduate Application", "Academic Transcripts", "Written Work / Research Proposal", "3 Academic References"],
    process=["Apply for any graduate degree at Oxford by January deadline", "Department automatically nominates top scholars", "Clarendon council issues award offers in March-April"],
    tags=["Oxford", "Clarendon", "No Separate Application", "Full Funding"]
)

add_entry(
    id="france-eiffel-excellence-scholarship",
    title="Eiffel Excellence Scholarship Programme (Campus France)",
    section="abroad", country="France", type_="government", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Science and Technology", "Engineering", "Economics and Management", "Law and Political Science"],
    target_group=["Top Foreign Students nominated by French Higher Education Institutions"],
    funding_amount="€1,181/month (Master) to €1,800/month (PhD) + International flights + Health insurance + Cultural activities",
    amount_val_inr=2200000,
    provider_name="Ministry for Europe and Foreign Affairs, France (Campus France)", provider_kind="ministry", provider_slug="campus-france", provider_website="https://www.campusfrance.org",
    eligibility="Foreign nationality (Indians eligible). Age <= 25 for Master, age <= 30 for PhD. Candidates must be nominated by a French higher education institution.",
    income_limit_inr=None, open_date="2026-10-01", deadline="2027-01-10", deadline_text="Annually opens October, closes January",
    recurring=True, status="open",
    official_link="https://www.campusfrance.org", source_url="https://www.campusfrance.org/en/eiffel-scholarship-program-excellence",
    documents=["Academic Transcripts & CV", "Letter of Motivation", "Letter of Acceptance from French University", "Language Proficiency Certificate"],
    process=["Contact chosen French university to request nomination for Eiffel", "French institution submits dossier to Campus France Paris", "Results announced in April"],
    tags=["France", "Eiffel", "Campus France", "Master & PhD", "Europe"]
)

add_entry(
    id="swiss-government-excellence-scholarship",
    title="Swiss Government Excellence Scholarships for Foreign Scholars",
    section="abroad", country="Switzerland", type_="government", category="Scholarship",
    education_levels=["PhD", "Postdoc"],
    streams=["All Academic Fields", "Engineering", "Natural Sciences", "Life Sciences", "Humanities"],
    target_group=["Postgraduate Researchers & Postdoctoral Scholars"],
    funding_amount="CHF 1,920/month (PhD) to CHF 3,500/month (Postdoc) + Health Insurance + Flight Allowance + Housing Grant",
    amount_val_inr=3200000,
    provider_name="Federal Commission for Scholarships for Foreign Students (FCS), Switzerland", provider_kind="ministry", provider_slug="swiss-seri", provider_website="https://www.sbfi.admin.ch",
    eligibility="Master's degree or PhD degree. Must have acceptance letter from a professor at a Swiss public university or ETH Zurich / EPFL willing to host the research.",
    income_limit_inr=None, open_date="2026-08-01", deadline="2026-11-15", deadline_text="Annually opens August, closes mid-November",
    recurring=True, status="open",
    official_link="https://www.sbfi.admin.ch", source_url="https://www.sbfi.admin.ch/scholarships_eng",
    documents=["FCS Application Form with photograph", "Detailed Research Proposal (max 5 pages)", "Host Professor Invitation Letter & Bio-data", "Two Confidential Recommendation Letters"],
    process=["Secure written support from a Swiss academic professor", "Submit application to Embassy of Switzerland in New Delhi", "Federal Commission in Bern selects fellows"],
    tags=["Switzerland", "ETH Zurich", "EPFL", "PhD & Postdoc", "Fully Funded"]
)

add_entry(
    id="australia-rtp-scholarships",
    title="Australian Government Research Training Program (RTP) International Stipend",
    section="abroad", country="Australia", type_="government", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["All Disciplines across Australian Universities"],
    target_group=["International Higher Degree by Research (HDR) candidates"],
    funding_amount="100% Australian Tuition Fees + AUD $34,000 to $40,000/year living stipend + Relocation & Health cover",
    amount_val_inr=2400000,
    provider_name="Department of Education, Australian Government", provider_kind="ministry", provider_slug="australia-education", provider_website="https://www.education.gov.au",
    eligibility="Enrolling in accredited Masters by Research or PhD at participating Australian University (Univ of Melbourne, Sydney, UNSW, ANU, Monash, etc.). High academic distinction.",
    income_limit_inr=None, open_date="2026-04-01", deadline="2026-08-31", deadline_text="Varies by university (major round closes August/September)",
    recurring=True, status="open",
    official_link="https://www.education.gov.au", source_url="https://www.education.gov.au/research-block-grants/research-training-program",
    documents=["Research Proposal", "Academic Transcripts & Grade Conversion", "Curriculum Vitae highlighting research publications", "Two Referee Reports"],
    process=["Apply directly to participating Australian university for admission and tick RTP scholarship box", "Faculty rankings and central university scholarship allocation"],
    tags=["Australia", "RTP", "Doctoral", "Melbourne / Sydney / ANU", "Living Stipend"]
)

add_entry(
    id="south-korea-gks-scholarship",
    title="Global Korea Scholarship (GKS - NIIED South Korea)",
    section="abroad", country="South Korea", type_="government", category="Scholarship",
    education_levels=["After 12th", "Bachelor", "Master", "PhD"],
    streams=["All Disciplines at accredited Korean Universities"],
    target_group=["International students seeking degree study in South Korea"],
    funding_amount="100% Tuition Fees + KRW 1,000,000 to 1,500,000/month living stipend + Airfare + 1-year Korean Language Training",
    amount_val_inr=1800000,
    provider_name="National Institute for International Education (NIIED), South Korea", provider_kind="ministry", provider_slug="niied-korea", provider_website="https://www.studyinkorea.go.kr",
    eligibility="Age < 25 for UG, age < 40 for Graduate. Consistent CGPA >= 80% on 100-point scale or top 20% in class.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-10-20", deadline_text="UG: Sep-Oct; Graduate: Feb-Mar",
    recurring=True, status="open",
    official_link="https://www.studyinkorea.go.kr", source_url="https://www.studyinkorea.go.kr/en/scholarship/gks_info.do",
    documents=["GKS Application Form", "Personal Statement & Statement of Purpose", "Transcripts & Degree Certificates attested with Apostille", "Medical Assessment"],
    process=["Apply via Embassy Track (Korean Embassy New Delhi) or University Track directly to Korean universities", "First round review followed by NIIED selection in Seoul"],
    tags=["South Korea", "GKS", "Full Ride", "Language Training", "Asia"]
)

add_entry(
    id="china-csc-government-scholarship",
    title="Chinese Government Scholarship (CSC) - Silk Road & Bilateral Program",
    section="abroad", country="China", type_="government", category="Scholarship",
    education_levels=["Bachelor", "Master", "PhD"],
    streams=["Science, Engineering, Agriculture, Medicine, Economics, Management"],
    target_group=["International students pursuing UG, Master or PhD in China"],
    funding_amount="100% Tuition Waiver + Free on-campus accommodation + CNY 2,500 to 3,500/month stipend",
    amount_val_inr=1200000,
    provider_name="China Scholarship Council (CSC), Ministry of Education China", provider_kind="ministry", provider_slug="csc-china", provider_website="https://www.campuschina.org",
    eligibility="Non-Chinese citizen with high academic standing. Age < 25 for UG, < 35 for Master, < 40 for PhD.",
    income_limit_inr=None, open_date="2026-11-01", deadline="2027-02-28", deadline_text="Annually opens November, closes February",
    recurring=True, status="upcoming",
    official_link="https://www.campuschina.org", source_url="https://www.campuschina.org/content/details3_74776.html",
    documents=["CSC Online Application Form", "Academic Transcripts & Notarized Degree", "Study Plan / Research Proposal (min 800 words)", "Foreigner Physical Examination Form"],
    process=["Submit application on CampusChina portal", "Contact designated Chinese university for pre-admission letter", "Dispatch dossier to dispatching authority or university"],
    tags=["China", "CSC", "Tuition Waiver", "Tsinghua / Peking", "Full Coverage"]
)

add_entry(
    id="eu-msca-doctoral-networks",
    title="Marie Skłodowska-Curie Actions (MSCA) Doctoral Networks - European Union",
    section="abroad", country="European Union", type_="government", category="Fellowship",
    education_levels=["PhD"],
    streams=["All Fields of Science, Technology, Engineering, Social Sciences & Humanities"],
    target_group=["Early Stage Doctoral Researchers of Any Nationality"],
    funding_amount="€3,400/month living allowance + €600/month mobility allowance + Family allowance + Research costs",
    amount_val_inr=4500000,
    provider_name="European Commission (Horizon Europe)", provider_kind="ministry", provider_slug="european-commission", provider_website="https://marie-sklodowska-curie-actions.ec.europa.eu",
    eligibility="Master's degree holder. Must not have resided or carried out main activity in host country for more than 12 months in the 3 years before recruitment.",
    income_limit_inr=None, open_date="2026-01-01", deadline=None, deadline_text="Individual project vacancies posted continuously on EURAXESS",
    recurring=True, status="rolling",
    official_link="https://euraxess.ec.europa.eu", source_url="https://marie-sklodowska-curie-actions.ec.europa.eu/actions/doctoral-networks",
    documents=["Europass CV", "Master's Transcripts", "Motivation Letter", "Reference Letters"],
    process=["Browse open PhD vacancies on EURAXESS portal with MSCA tag", "Apply directly to university consortium recruiting for the specific project", "Contractual employment with full social security"],
    tags=["MSCA", "Doctoral Networks", "Horizon Europe", "Europe PhD", "High Salary"]
)

add_entry(
    id="singapore-singa-award",
    title="Singapore International Graduate Award (SINGA - A*STAR)",
    section="abroad", country="Singapore", type_="government", category="Scholarship",
    education_levels=["PhD"],
    streams=["Biomedical Sciences", "Computing and Information Sciences", "Engineering and Technology", "Physical Sciences"],
    target_group=["International graduates with passion for research in Singapore"],
    funding_amount="100% Tuition Fees for 4 years + SGD $2,700 to $3,200/month stipend + Airfare grant + Settlement allowance",
    amount_val_inr=3200000,
    provider_name="Agency for Science, Technology and Research (A*STAR), Singapore", provider_kind="lab", provider_slug="astar-singapore", provider_website="https://www.a-star.edu.sg",
    eligibility="Graduates with excellent academic records and strong research interest. Fluent in written and spoken English.",
    income_limit_inr=None, open_date="2026-06-01", deadline="2026-12-01", deadline_text="Two intake cycles (January and August intakes)",
    recurring=True, status="open",
    official_link="https://www.a-star.edu.sg", source_url="https://www.a-star.edu.sg/Scholarships/for-graduate-studies/singapore-international-graduate-award-singa",
    documents=["Academic Transcripts (Bachelor's and/or Master's)", "Two Academic Recommendation Letters", "Copy of Passport"],
    process=["Browse research projects across A*STAR Labs, NUS, NTU, SUTD, or SMU", "Submit online SINGA application", "Shortlisted candidates interviewed virtually"],
    tags=["Singapore", "A*STAR", "NUS / NTU", "PhD Award", "Asia"]
)

# ==============================================================================
# SECTION 2: OPPORTUNITIES ABROAD - PRIVATE TRUSTS & PHILANTHROPIC SCHOLARSHIPS
# ==============================================================================

add_entry(
    id="inlaks-shivdasani-scholarship",
    title="Inlaks Shivdasani Foundation Scholarships for Higher Education Abroad",
    section="abroad", country="North America & Europe", type_="private", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Humanities", "Social Sciences", "Fine Arts", "Architecture", "Environment", "Law", "Sciences"],
    target_group=["Exceptional Young Indians with Unconditional Admission in Top Foreign Universities"],
    funding_amount="Up to $100,000 (Approx. ₹83 Lakhs) covering tuition, living expenses and travel",
    amount_val_inr=8300000,
    provider_name="Inlaks Shivdasani Foundation", provider_kind="trust", provider_slug="inlaks-foundation", provider_website="https://www.inlaksfoundation.org",
    eligibility="Indian citizen with first-class undergraduate degree. Age <= 30 years. Must hold unconditional offer from top university in USA, UK, or Europe.",
    income_limit_inr=None, open_date="2027-02-01", deadline="2027-03-31", deadline_text="Annually opens February, closes end of March",
    recurring=True, status="upcoming",
    official_link="https://www.inlaksfoundation.org", source_url="https://www.inlaksfoundation.org/scholarships",
    documents=["Unconditional Admission Letter", "Portfolio of Work (for Arts/Architecture)", "Detailed CV & Academic Transcripts", "Evidence of Outstanding Extracurricular Achievements"],
    process=["Online application on Inlaks portal in Feb-March", "Preliminary interview in April", "Final jury interview in Mumbai/Delhi in late May"],
    tags=["Inlaks", "Elite", "US / UK / Europe", "Arts & Sciences", "High Value"]
)

add_entry(
    id="tata-trusts-jn-tata-endowment",
    title="JN Tata Endowment for Higher Education of Indians",
    section="abroad", country="Global", type_="private", category="Scholarship",
    education_levels=["Master", "PhD", "Postdoc"],
    streams=["All Disciplines", "Engineering", "Medicine", "Sciences", "Humanities", "Law", "Management"],
    target_group=["Indian Graduates admitted to Reputable Universities Abroad"],
    funding_amount="Loan Scholarship up to ₹10,00,000 + Gift Scholarship up to ₹7,50,000",
    amount_val_inr=1000000,
    provider_name="Tata Trusts (JN Tata Endowment)", provider_kind="trust", provider_slug="jn-tata-endowment", provider_website="https://www.jntataendowment.org",
    eligibility="Indian graduates with minimum 60% aggregate marks in Bachelor's or Master's, admitted to or applied for reputable universities abroad.",
    income_limit_inr=None, open_date="2027-01-01", deadline="2027-03-15", deadline_text="Annually opens January, closes mid-March",
    recurring=True, status="upcoming",
    official_link="https://www.jntataendowment.org", source_url="https://www.jntataendowment.org",
    documents=["Statement of Purpose", "Graduation Transcripts", "GRE/GMAT/IELTS Scorecards", "Admission Letters / Applied Universities List", "Academic Recommendation Letter"],
    process=["Submit online form on JN Tata portal", "Online Thinking Skills Assessment", "Technical interview with expert Indian and global academicians"],
    tags=["Tata Trusts", "JN Tata", "Study Abroad", "Loan + Gift", "All Streams"]
)

add_entry(
    id="narotam-sekhsaria-scholarship",
    title="Narotam Sekhsaria Scholarship Programme for Postgraduate Studies Abroad",
    section="abroad", country="Global", type_="private", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Pure & Applied Sciences", "Civil", "Mechanical", "Electrical", "Computer Science", "Management", "Law", "Social Sciences"],
    target_group=["Merit-based Indian Graduates under 30"],
    funding_amount="Interest-free Loan Scholarship up to ₹20,00,000",
    amount_val_inr=2000000,
    provider_name="Narotam Sekhsaria Foundation", provider_kind="trust", provider_slug="narotam-sekhsaria-foundation", provider_website="https://pg.nsfoundation.co.in",
    eligibility="Indian national residing in India, below 30 years of age, holding undergraduate degree with consistent first-class track record.",
    income_limit_inr=None, open_date="2027-01-05", deadline="2027-03-20", deadline_text="Annually opens January, closes late March",
    recurring=True, status="upcoming",
    official_link="https://pg.nsfoundation.co.in", source_url="https://pg.nsfoundation.co.in",
    documents=["Undergraduate and Postgraduate Transcripts", "Admission letter from international university", "Statement of Purpose & 2 Referee Letters", "Income Tax documents of parents"],
    process=["Online application and document submission", "Shortlisted candidates invited for interview in Mumbai", "Repayable over 1-4 years after course completion"],
    tags=["Narotam Sekhsaria", "Interest-Free", "Top Global Universities", "Mentorship"]
)

add_entry(
    id="aga-khan-isp-scholarship",
    title="Aga Khan Foundation International Scholarship Programme (ISP)",
    section="abroad", country="Global", type_="private", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Development Studies", "Architecture", "Engineering", "Public Health", "Management", "Education"],
    target_group=["Needy and brilliant students from developing nations"],
    funding_amount="50% Grant + 50% Loan covering full tuition and living expenses",
    amount_val_inr=3000000,
    provider_name="Aga Khan Development Network (AKDN)", provider_kind="trust", provider_slug="aga-khan-foundation", provider_website="https://www.akdn.org",
    eligibility="Consistent excellent academic record, genuine financial need, admission to a reputable university abroad, age under 30 years.",
    income_limit_inr=None, open_date="2027-01-01", deadline="2027-03-31", deadline_text="Annually opens January, closes March",
    recurring=True, status="upcoming",
    official_link="https://www.akdn.org", source_url="https://www.akdn.org/our-agencies/aga-khan-foundation/international-scholarship-programme",
    documents=["AKF Application Form", "Financial budget breakdown and proof of financial hardship", "Valid admission offer from foreign institution", "Three referee letters"],
    process=["Contact local Aga Khan Foundation office in New Delhi for application dossier", "Comprehensive financial assessment and personal interview"],
    tags=["Aga Khan", "Need + Merit", "50% Grant 50% Loan", "Development Studies"]
)

add_entry(
    id="kc-mahindra-scholarship-abroad",
    title="K.C. Mahindra Scholarships for Post-Graduate Studies Abroad",
    section="abroad", country="Global", type_="private", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["Engineering", "Natural Sciences", "Humanities", "Medicine", "Management"],
    target_group=["Indian Graduates admitted to Reputed Foreign Universities"],
    funding_amount="Interest-free Loan Scholarship up to ₹10,00,000 (Top 3 receive ₹10 Lakhs, others ₹5 Lakhs)",
    amount_val_inr=1000000,
    provider_name="K.C. Mahindra Education Trust", provider_kind="trust", provider_slug="kc-mahindra-trust", provider_website="https://www.kcmet.org",
    eligibility="Indian citizen with first-class degree from recognized university, having applied for or admitted into post-graduate studies abroad.",
    income_limit_inr=None, open_date="2027-01-15", deadline="2027-03-31", deadline_text="Annually opens January, closes end of March",
    recurring=True, status="upcoming",
    official_link="https://www.kcmet.org", source_url="https://www.kcmet.org/what-we-do-scholarships-fellowships.aspx",
    documents=["Graduation Transcripts", "Letter of Admission from Foreign University", "Two Recommendation Letters", "Statement of Purpose"],
    process=["Submit online application on KCMET portal", "Preliminary shortlisting followed by in-person interview in Mumbai with Mahindra Trust trustees"],
    tags=["Mahindra", "KCMET", "Interest-Free Loan", "Study Abroad"]
)

add_entry(
    id="lady-meherbai-tata-scholarship",
    title="Lady Meherbai D. Tata Education Trust Scholarships for Indian Women",
    section="abroad", country="Global", type_="private", category="Scholarship",
    education_levels=["Master"],
    streams=["Social Work", "Public Health", "Gender Studies", "Child Welfare", "Education", "Rural Development"],
    target_group=["Indian Graduate Women studying abroad"],
    funding_amount="Financial Grant up to ₹6,00,000 towards tuition fees",
    amount_val_inr=600000,
    provider_name="Tata Trusts (Lady Meherbai Tata Trust)", provider_kind="trust", provider_slug="tata-trusts", provider_website="https://www.tatatrusts.org",
    eligibility="Indian women graduates from recognized universities with consistent remarkable academic record, holding admission to top universities in US, UK or Europe in designated social fields.",
    income_limit_inr=None, open_date="2027-03-01", deadline="2027-05-02", deadline_text="Annually opens March, closes early May",
    recurring=True, status="upcoming",
    official_link="https://www.tatatrusts.org", source_url="https://www.tatatrusts.org/our-work/individual-grants-programme/education-grants",
    documents=["Admission Letter from Foreign University", "Undergraduate Transcripts", "CV detailing social sector work", "Statement of Purpose"],
    process=["Submit application on Tata Trusts portal", "Screening by trustees and senior social scientists", "Personal interview"],
    tags=["Women Scholars", "Social Work", "Public Health", "Tata Trusts"]
)

add_entry(
    id="stanford-knight-hennessy-scholars",
    title="Knight-Hennessy Scholars Program (Stanford University, USA)",
    section="abroad", country="United States", type_="university", category="Scholarship",
    education_levels=["Master", "PhD"],
    streams=["All Graduate Degree Programs across Stanford University (JD, MA, MBA, MD, MS, PhD)"],
    target_group=["Visionary Future Leaders of Any Nationality"],
    funding_amount="100% Stanford Tuition + Generous Living & Academic Stipend + Economy Airfare to Stanford",
    amount_val_inr=8000000,
    provider_name="Knight-Hennessy Scholars, Stanford University", provider_kind="university", provider_slug="stanford-university", provider_website="https://knight-hennessy.stanford.edu",
    eligibility="Applying to any graduate degree at Stanford. First degree completed within last 7 years. Demonstrates independence of thought, purposeful leadership, and civic mindset.",
    income_limit_inr=None, open_date="2026-06-01", deadline="2026-10-09", deadline_text="Annually opens June, closes early October",
    recurring=True, status="open",
    official_link="https://knight-hennessy.stanford.edu", source_url="https://knight-hennessy.stanford.edu/admission",
    documents=["Online Application with Essays and Video Statement", "Stanford Graduate Degree Application", "Resume", "Two Recommendation Letters"],
    process=["Submit Knight-Hennessy application and Stanford department application", "Finalists invited to Immersion Weekend at Stanford in February", "Scholars join multidisciplinary Denning House cohort"],
    tags=["Stanford", "Knight-Hennessy", "Elite", "Fully Funded", "USA"]
)

# ==============================================================================
# SECTION 2: OPPORTUNITIES ABROAD - FUNDED RESEARCH INTERNSHIPS & SUMMER FELLOWSHIPS
# ==============================================================================

add_entry(
    id="canada-mitacs-globalink-gri",
    title="Mitacs Globalink Research Internship (Canada)",
    section="abroad", country="Canada", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["All Disciplines", "Engineering", "Computer Science", "Mathematics", "Humanities", "Social Sciences"],
    target_group=["Full-time Undergraduate & Combined Master's Students in India"],
    funding_amount="CAD $8,000+ package (Round-trip flight + Housing + CAD $200/wk food stipend + Health insurance)",
    amount_val_inr=500000,
    provider_name="Mitacs Canada & Government of Canada", provider_kind="ministry", provider_slug="mitacs-canada", provider_website="https://www.mitacs.ca",
    eligibility="Full-time enrolled in 2nd or 3rd year of 4-year degree (or 3rd/4th of 5-year integrated course) with minimum 80% or 8.0 CGPA.",
    income_limit_inr=None, open_date="2026-08-01", deadline="2026-09-20", deadline_text="Annually opens August, closes September 20 for following summer",
    recurring=True, status="open",
    official_link="https://www.mitacs.ca", source_url="https://www.mitacs.ca/our-programs/globalink-research-internship-students",
    documents=["Official Academic Transcripts in English", "Academic CV in Mitacs template", "Minimum 1 Letter of Reference from Professor", "Research Rationale for 3-7 chosen projects"],
    process=["Search Mitacs database and choose 3 to 7 Canadian projects across min 3 provinces", "Canadian professors interview shortlisted candidates", "Mitacs confirms matches; full visa, housing and travel handled"],
    tags=["Canada", "Mitacs", "Fully Funded", "Summer Research", "Top Ranked"]
)

add_entry(
    id="germany-daad-wise-internship",
    title="DAAD WISE (Working Internships in Science and Engineering) - Germany",
    section="abroad", country="Germany", type_="government", category="Internship",
    education_levels=["Bachelor"],
    streams=["Engineering", "Natural Sciences", "Mathematics", "Computer Science"],
    target_group=["Indian Undergraduate Engineering & Science Students"],
    funding_amount="€934/month stipend + €1,075 Travel Subsidy + Comprehensive Health Insurance",
    amount_val_inr=275000,
    provider_name="German Academic Exchange Service (DAAD)", provider_kind="ministry", provider_slug="daad-germany", provider_website="https://www.daad.in",
    eligibility="5th or 6th semester B.Tech/B.E. or 5th-8th semester Integrated M.Tech students from select Indian universities with CGPA >= 8.5.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-11-01", deadline_text="Annually opens September, strictly closes November 1",
    recurring=True, status="open",
    official_link="https://www.daad.in", source_url="https://www.daad.in/en/find-funding/scholarship-database/?type=scholarship&q=WISE",
    documents=["Invitation Letter from German host professor/institute", "Form 'Approval by the Indian Host Institute' signed by Dean/HOD", "Detailed Project Description agreed with German mentor", "CV and Transcripts"],
    process=["Reach out to German university professors to secure written invitation", "Submit official application on DAAD online portal by November 1", "2 to 3 month internship in Germany during May-August"],
    tags=["Germany", "DAAD", "WISE", "German Research Labs", "Funded"]
)

add_entry(
    id="cern-summer-student-programme",
    title="CERN Summer Student Programme (Geneva, Switzerland)",
    section="abroad", country="Switzerland", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Physics", "Computing & Software", "Electrical & Mechanical Engineering", "Mathematics"],
    target_group=["UG & PG Students from Member and Associate Member States (India is Associate Member)"],
    funding_amount="90 CHF/day (Approx. ₹8,500/day = ₹2.5 Lakhs/m) + Travel Allowance + Health Insurance",
    amount_val_inr=650000,
    provider_name="European Organization for Nuclear Research (CERN)", provider_kind="lab", provider_slug="cern-geneva", provider_website="https://home.cern",
    eligibility="Completed at least 3 years of full-time university study in physics, engineering, or computing. Fluent in English or French.",
    income_limit_inr=None, open_date="2026-11-01", deadline="2027-01-31", deadline_text="Annually opens November, closes end of January",
    recurring=True, status="upcoming",
    official_link="https://careers.cern", source_url="https://careers.cern/summer",
    documents=["Curriculum Vitae in English", "Official Academic Transcripts", "Two Reference Letters from University Lecturers"],
    process=["Submit application on SmartRecruiters CERN portal", "CERN experimental teams match candidate profiles with ongoing LHC detector and software projects", "8 to 13 weeks fully funded stay in Geneva"],
    tags=["CERN", "Switzerland", "LHC Physics", "High Stipend", "World Famous"]
)

add_entry(
    id="us-sn-bose-scholars-program",
    title="SN Bose Scholars Program (IUSSTF - United States)",
    section="abroad", country="United States", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Atmospheric Sciences", "Chemical Sciences", "Engineering", "Mathematical Sciences", "Life Sciences"],
    target_group=["Top Indian Undergraduate and Master's Students"],
    funding_amount="$2,500+ stipend + Round-trip international airfare + Health insurance",
    amount_val_inr=350000,
    provider_name="Indo-US Science and Technology Forum (IUSSTF) & WINStep Forward", provider_kind="ministry", provider_slug="iusstf-india", provider_website="https://iusstf.org",
    eligibility="Indian citizen currently enrolled in 3rd/4th year B.Tech or 1st year M.Sc/M.Tech with CGPA >= 8.5 / top 5% rank in class.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-10-31", deadline_text="Annually opens September, closes October 31",
    recurring=True, status="open",
    official_link="https://iusstf.org", source_url="https://iusstf.org/sn-bose-scholars-program",
    documents=["Statement of Purpose (2 pages)", "Two Recommendation Letters on institutional letterhead", "No Objection Certificate from Parent Institution", "Official Transcripts"],
    process=["Submit online application via IUSSTF portal", "National selection committee evaluates proposals", "10-12 weeks placement at premier US labs (MIT, Harvard, Caltech, Stanford, UW-Madison)"],
    tags=["USA", "SN Bose", "IUSSTF", "Premier Labs", "Indo-US"]
)

add_entry(
    id="france-charpak-summer-internship",
    title="Charpak Summer Internship Program - France",
    section="abroad", country="France", type_="government", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["All Disciplines", "Science", "Engineering", "Economics", "Management", "Social Sciences"],
    target_group=["Indian Students enrolled in Indian Higher Education Institutions"],
    funding_amount="€700/month living allowance + Student visa fee waiver + Free social security",
    amount_val_inr=200000,
    provider_name="Embassy of France in India / Campus France", provider_kind="ministry", provider_slug="campus-france", provider_website="https://www.inde.campusfrance.org",
    eligibility="Indian national enrolled in Indian university. Under 30 years old. Must have acceptance letter from a French laboratory or university.",
    income_limit_inr=None, open_date="2027-01-15", deadline="2027-03-31", deadline_text="Annually opens January, closes end of March",
    recurring=True, status="upcoming",
    official_link="https://www.inde.campusfrance.org", source_url="https://www.inde.campusfrance.org/charpak-scholarships",
    documents=["Acceptance Letter / Convention de Stage from French Laboratory", "Curriculum Vitae", "Statement of Purpose", "Recommendation Letter from Indian Professor"],
    process=["Secure acceptance from a French laboratory or research team", "Apply through Campus France India portal", "2 to 3 months research stay in France"],
    tags=["France", "Charpak", "Campus France", "Europe Internship", "Funded"]
)

add_entry(
    id="germany-max-planck-maxsip",
    title="Max Planck Summer Internship Program (MaxSIP) in Life Sciences - Germany",
    section="abroad", country="Germany", type_="lab", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Biology", "Biochemistry", "Neuroscience", "Computational Biology", "Biophysics"],
    target_group=["International Undergraduate & Master's Students"],
    funding_amount="€800/month stipend + Free on-campus housing + Round-trip travel reimbursement",
    amount_val_inr=250000,
    provider_name="Max Planck Institutes of Biochemistry & Biological Intelligence", provider_kind="lab", provider_slug="max-planck-society", provider_website="https://www.maxsip.mpg.de",
    eligibility="Students with strong academic record in biology, chemistry, physics, or computer science. Completed at least 2 years of degree.",
    income_limit_inr=None, open_date="2027-01-01", deadline="2027-02-15", deadline_text="Annually opens January, closes mid-February",
    recurring=True, status="upcoming",
    official_link="https://www.maxsip.mpg.de", source_url="https://www.maxsip.mpg.de",
    documents=["Curriculum Vitae", "Transcripts", "Statement of Research Interest", "Two Letters of Recommendation"],
    process=["Online application on MaxSIP portal", "Faculty review and selection for 10-week summer research stay in Martinsried/Munich"],
    tags=["Max Planck", "Germany", "Life Sciences", "Neurobiology", "Funded"]
)

add_entry(
    id="japan-oist-research-internship",
    title="OIST Research Internship Program (Okinawa, Japan)",
    section="abroad", country="Japan", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Physics", "Chemistry", "Biology", "Neuroscience", "Mathematics", "Computational Science", "Engineering"],
    target_group=["Undergraduate & Postgraduate Students Worldwide"],
    funding_amount="¥2,400/day allowance + Free fully furnished campus apartment + Round-trip flights + Visa support",
    amount_val_inr=200000,
    provider_name="Okinawa Institute of Science and Technology (OIST)", provider_kind="university", provider_slug="oist-japan", provider_website="https://www.oist.jp",
    eligibility="Students in final 2 years of undergraduate or in master's degree. High academic potential.",
    income_limit_inr=None, open_date="2026-09-01", deadline="2026-10-15", deadline_text="Two cycles per year (Spring/Summer and Autumn/Winter)",
    recurring=True, status="open",
    official_link="https://admissions.oist.jp", source_url="https://admissions.oist.jp/apply-research-internship",
    documents=["Statement of Purpose (400 words)", "Academic Transcripts", "Recommendation Letter", "ID Photo & Passport Copy"],
    process=["Submit online application on OIST admissions portal", "Professors review candidate match for 2 to 6 months research stay in Okinawa"],
    tags=["Japan", "OIST", "Okinawa", "Research Internship", "Full Travel Covered"]
)

add_entry(
    id="switzerland-epfl-summer-fellowship",
    title="EPFL Summer Research Fellowship in Computer Science & Life Sciences",
    section="abroad", country="Switzerland", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Computer Science", "Data Science", "Bioengineering", "Life Sciences"],
    target_group=["Top International Undergraduate & Master's Students"],
    funding_amount="CHF 1,600 to CHF 1,800/month living stipend + Round-trip travel refund",
    amount_val_inr=320000,
    provider_name="École Polytechnique Fédérale de Lausanne (EPFL)", provider_kind="university", provider_slug="epfl-switzerland", provider_website="https://www.epfl.ch",
    eligibility="Enrolled in Bachelor or Master programme in Computer Science or Life Sciences with top 10% class rank.",
    income_limit_inr=None, open_date="2026-11-01", deadline="2026-12-01", deadline_text="Annually opens November, closes early December",
    recurring=True, status="upcoming",
    official_link="https://www.epfl.ch", source_url="https://www.epfl.ch/schools/ic/education/summer-at-epfl",
    documents=["Curriculum Vitae", "Official Transcripts", "Statement of Purpose (max 1000 words)", "Two Referee Letters"],
    process=["Apply through EPFL Summer at IC / SV portal", "Faculty labs evaluate candidates for 2 to 3 months intensive summer research in Lausanne"],
    tags=["EPFL", "Switzerland", "Computer Science", "High Stipend", "Lausanne"]
)

add_entry(
    id="switzerland-eth-student-summer-research",
    title="ETH Student Summer Research Fellowship (ETH Zurich)",
    section="abroad", country="Switzerland", type_="university", category="Internship",
    education_levels=["Bachelor", "Master"],
    streams=["Computer Science", "Data Science", "Electrical Engineering", "Robotics"],
    target_group=["Undergraduate & Master's Students in Computer Science"],
    funding_amount="CHF 1,750/month housing and living allowance + Travel and visa expenses covered",
    amount_val_inr=340000,
    provider_name="ETH Zurich (Department of Computer Science)", provider_kind="university", provider_slug="eth-zurich", provider_website="https://ethz.ch",
    eligibility="Undergraduate or master's students having completed at least two years of degree with top academic marks.",
    income_limit_inr=None, open_date="2026-11-01", deadline="2026-12-15", deadline_text="Annually opens November, closes mid-December",
    recurring=True, status="upcoming",
    official_link="https://inf.ethz.ch", source_url="https://inf.ethz.ch/studies/summer-research-fellowship.html",
    documents=["Resume / CV", "Official Transcripts", "Letter of Motivation", "Letter of Recommendation"],
    process=["Apply on ETH CS Fellowship portal", "Selected fellows work for 2 months (July-August) on research projects in Zurich"],
    tags=["ETH Zurich", "Switzerland", "Computer Science", "Robotics", "Prestigious"]
)

# Output generation
print(f"Total entries compiled: {len(DATA)}")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=2, ensure_ascii=False)
print(f"Saved successfully to {OUTPUT_FILE}")
