// Comprehensive database of National & International Scholarships, Fellowships, Funds & Internships
// Curated specifically for Indian students (After 12th, Bachelor, Master, PhD)

const OPPORTUNITIES_DATA = [
  // ==========================================
  // SECTION 1: OPPORTUNITIES IN INDIA
  // ==========================================
  
  // --- GOVERNMENT FUNDS (INDIA) ---
  {
    id: "ind-gov-01",
    title: "National Scholarship Portal (NSP) - Central Sector Scheme for College and University Students (PM-USP)",
    section: "india",
    type: "government",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor", "Master"],
    streams: ["All Disciplines", "STEM", "Commerce", "Arts & Humanities", "Medical"],
    targetGroup: ["Merit-cum-Means", "General", "OBC", "SC", "ST", "EWS"],
    fundingAmount: "₹12,000/yr (UG) to ₹20,000/yr (PG)",
    amountVal: 20000,
    coverage: "Annual maintenance allowance directly transferred via DBT",
    fundingAgency: "Ministry of Education (MoE), Government of India",
    eligibility: "Top 20th percentile in respective Class 12 Board Exams. Family annual gross income <= ₹4.5 Lakhs. Regular full-time course.",
    deadline: "October - December (Annual)",
    deadlineMonth: "December",
    officialLink: "https://scholarships.gov.in",
    documentsRequired: [
      "Class 12th Marksheet",
      "Income Certificate (< ₹4.5 LPA) issued by competent authority",
      "Aadhaar Card linked to Bank Account",
      "Bonafide Student Certificate from College/Institute",
      "College Admission Fee Receipt"
    ],
    applicationProcess: [
      "Register with One-Time Registration (OTR) on scholarships.gov.in using Aadhaar",
      "Fill scholarship application selecting Department of Higher Education",
      "Upload verified documents and submit for Institute Level Verification",
      "Funds disbursed directly through Aadhaar Payment Bridge (APB)"
    ],
    tags: ["Central Govt", "Post-12th", "College Degree", "DBT"]
  },
  {
    id: "ind-gov-02",
    title: "INSPIRE Scholarship for Higher Education (SHE)",
    section: "india",
    type: "government",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor", "Master"],
    streams: ["Basic & Natural Sciences", "STEM"],
    targetGroup: ["Merit-based", "Top 1% Board Rankers", "KVPY / JEE / NEET Top Rankers"],
    fundingAmount: "₹80,000 per year (₹60,000 stipend + ₹20,000 summer project mentorship)",
    amountVal: 80000,
    coverage: "Annual scholarship for 5 years or until completion of M.Sc / MS in Natural & Basic Sciences",
    fundingAgency: "Department of Science and Technology (DST), Govt. of India",
    eligibility: "Top 1% of respective Class 12 board or ranks within top 10,000 in JEE Advanced or NEET, enrolled in B.Sc., B.S., or Int. M.Sc. in Natural & Basic Sciences.",
    deadline: "November - January (Annual)",
    deadlineMonth: "January",
    officialLink: "https://online-inspire.gov.in",
    documentsRequired: [
      "Class 12 & 10 Marksheet & Board Advisory Note",
      "Endorsement Certificate signed by Head of University/College",
      "Aadhaar Card and SBI Bank Account details",
      "Eligibility Proof (Cutoff letter / JEE / NEET rank card)"
    ],
    applicationProcess: [
      "Register on DST INSPIRE Web Portal",
      "Upload Endorsement Certificate & Academic Transcripts",
      "Maintain >= 60% marks or 7.0 CGPA each year to renew funding for 5 years"
    ],
    tags: ["DST", "Science Research", "Pure Science", "High Stipend"]
  },
  {
    id: "ind-gov-03",
    title: "Prime Minister's Research Fellowship (PMRF)",
    section: "india",
    type: "government",
    category: "Fellowship",
    educationLevel: ["PhD"],
    streams: ["STEM", "Engineering", "Science", "Technology"],
    targetGroup: ["Merit-based", "Top Researchers"],
    fundingAmount: "₹70,000 to ₹80,000/month + ₹2,00,000/year Research Contingency Grant",
    amountVal: 960000,
    coverage: "₹70k/m (Year 1-2), ₹75k/m (Year 3), ₹80k/m (Year 4-5) plus ₹2 Lakh annual research grant for 5 years",
    fundingAgency: "Ministry of Education (MoE), Implemented via IITs / IISc",
    eligibility: "Eligible for candidates admitted to PhD programs at PMRF granting institutes (IISc, IITs, IISERs, select Central Universities) with CGPA >= 8.0 or qualifying GATE score.",
    deadline: "Cycle opens twice a year (May & December)",
    deadlineMonth: "May",
    officialLink: "https://www.pmrf.in",
    documentsRequired: [
      "Comprehensive Research Proposal (Abstract, Methodology, Expected Impact)",
      "B.Tech / M.Tech / M.Sc transcripts and degree certificates",
      "GATE score card (if applicable)",
      "Recommendation Letters by nominated PhD advisor"
    ],
    applicationProcess: [
      "Gain admission to PhD at a PMRF granting institution",
      "Institute nominates candidates via Direct Entry or Lateral Entry channel",
      "National Apex Committee reviews research proposal and conducts interviews"
    ],
    tags: ["Prestigious", "Doctoral", "IIT/IISc", "Highest Govt Stipend"]
  },
  {
    id: "ind-gov-04",
    title: "AICTE Pragati Scholarship Scheme for Girl Students",
    section: "india",
    type: "government",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor"],
    streams: ["Engineering & Technology", "Technical Degrees & Diplomas"],
    targetGroup: ["Women / Girls Only", "Means-based (< ₹8 LPA)"],
    fundingAmount: "₹50,000 per year for every year of study",
    amountVal: 50000,
    coverage: "₹50,000 per annum towards college fee, books, equipment, laptops and software",
    fundingAgency: "All India Council for Technical Education (AICTE)",
    eligibility: "Female students admitted to 1st year of Degree/Diploma course in AICTE approved institution. Maximum 2 girls per family. Family income <= ₹8 Lakhs/year.",
    deadline: "October - December (Annual via NSP)",
    deadlineMonth: "December",
    officialLink: "https://www.aicte-india.org/schemes/students-development-schemes/pragati",
    documentsRequired: [
      "Class 10 & 12 Marksheet",
      "Allotment letter through Centralized Admission Process",
      "Annual Income Certificate (< ₹8 LPA)",
      "Bank Account details linked with Aadhaar",
      "Tuition Fee receipt"
    ],
    applicationProcess: [
      "Apply via National Scholarship Portal (NSP)",
      "Select AICTE Schemes -> Pragati Scholarship Scheme",
      "Verify at Institute and State Directorate level"
    ],
    tags: ["Women in Tech", "AICTE", "Engineering", "Girls Empowerment"]
  },
  {
    id: "ind-gov-05",
    title: "CSIR-UGC Junior Research Fellowship (JRF) & NET",
    section: "india",
    type: "government",
    category: "Fellowship",
    educationLevel: ["Master", "PhD"],
    streams: ["Physical Sciences", "Chemical Sciences", "Life Sciences", "Mathematical Sciences", "Earth Sciences"],
    targetGroup: ["National Competitive Exam Rankers"],
    fundingAmount: "₹37,000/month (JRF) + HRA -> ₹42,000/month (SRF) + ₹20,000/yr Contingency",
    amountVal: 444000,
    coverage: "Monthly fellowship + House Rent Allowance (8%-27%) + Annual contingency for 5 years",
    fundingAgency: "Council of Scientific and Industrial Research (CSIR) & UGC",
    eligibility: "M.Sc. or equivalent degree with minimum 55% marks (50% for SC/ST/PwD). Age limit <= 30 years (relaxable for reserved/women).",
    deadline: "Exam held twice a year (June & December cycles)",
    deadlineMonth: "June",
    officialLink: "https://csirnet.nta.ac.in",
    documentsRequired: [
      "M.Sc./Integrated Master's Marksheets",
      "Category Certificate (OBC-NCL/SC/ST/EWS)",
      "Identity Proof (Aadhaar/Passport)"
    ],
    applicationProcess: [
      "Register for Joint CSIR-UGC NET exam conducted by NTA",
      "Qualify for Junior Research Fellowship cutoff",
      "Activate fellowship upon registering for PhD at any Indian University or CSIR Lab"
    ],
    tags: ["Doctoral", "CSIR", "Science Research", "Full Funding"]
  },
  {
    id: "ind-gov-06",
    title: "Post-Matric Scholarship Scheme for SC / ST / OBC / Minorities",
    section: "india",
    type: "government",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor", "Master", "PhD"],
    streams: ["All Disciplines"],
    targetGroup: ["SC", "ST", "OBC", "Minority Communities", "EWS"],
    fundingAmount: "100% Tuition Fee Waiver + ₹4,000 to ₹13,500/year living allowance",
    amountVal: 60000,
    coverage: "Complete non-refundable college compulsory fees reimbursement plus maintenance allowance",
    fundingAgency: "Ministry of Social Justice & Empowerment / Ministry of Tribal Affairs",
    eligibility: "Students belonging to SC/ST/OBC/Minority studying at post-matric level (UG/PG/Doctoral). Income ceiling ₹2.5 LPA for SC/ST, ₹1.5 - ₹2.5 LPA for OBC.",
    deadline: "August - November (Annual via State & NSP portals)",
    deadlineMonth: "November",
    officialLink: "https://scholarships.gov.in",
    documentsRequired: [
      "Valid Caste / Community Certificate",
      "Tehsildar issued Income Certificate",
      "Hostel fee receipt (if hosteller)",
      "College fee structure and receipt",
      "Bank passbook with IFSC code"
    ],
    applicationProcess: [
      "Apply through National Scholarship Portal or respective State e-Kalyan/MahaDBT portals",
      "Submit physical verification to college nodal scholarship officer"
    ],
    tags: ["Tuition Waiver", "Reserved Category", "State & Central", "High Impact"]
  },
  {
    id: "ind-gov-07",
    title: "SERB - National Post Doctoral Fellowship (N-PDF)",
    section: "india",
    type: "government",
    category: "Fellowship",
    educationLevel: ["PhD"],
    streams: ["STEM", "Life Sciences", "Physical Sciences", "Engineering"],
    targetGroup: ["Early Career Researchers"],
    fundingAmount: "₹55,000/month + HRA + ₹2,00,000/year Research Grant",
    amountVal: 660000,
    coverage: "Two-year postdoctoral fellowship with overheads of ₹35,000/year to host institute",
    fundingAgency: "Science and Engineering Research Board (SERB - ANRF)",
    eligibility: "Indian citizens with PhD/MD/MS degree in science or engineering. Age limit <= 35 years (relaxable by 5 years for SC/ST/OBC/Women/PwD).",
    deadline: "May - July (Annual)",
    deadlineMonth: "July",
    officialLink: "https://serbonline.in",
    documentsRequired: [
      "Project Proposal in prescribed format",
      "Host Institute Endorsement Letter",
      "Mentor Consent Letter & Bio-data",
      "PhD Degree Certificate or Provisional Certificate"
    ],
    applicationProcess: [
      "Identify a mentor at an accredited academic institution/national lab",
      "Submit joint research proposal online via SERB portal"
    ],
    tags: ["Postdoctoral", "ANRF", "Advanced Research", "STEM"]
  },

  // --- PRIVATE & CSR FUNDS (INDIA) ---
  {
    id: "ind-pvt-01",
    title: "Tata Trusts Means, Merit & Medical/Engineering Scholarships",
    section: "india",
    type: "private",
    category: "Scholarship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Engineering", "Medicine", "Special Education", "Social Sciences"],
    targetGroup: ["Merit-cum-Means", "Economically Weaker Section"],
    fundingAmount: "30% to 80% of College Tuition Fees (Up to ₹1,50,000/yr)",
    amountVal: 150000,
    coverage: "Direct tuition fee grant paid to the institute or student for academic year",
    fundingAgency: "Sir Ratan Tata Trust & Allied Trusts",
    eligibility: "Undergraduate or Postgraduate students studying in recognized institutions in India with minimum 60% marks and family income <= ₹4.5 Lakhs.",
    deadline: "October - January (Annual)",
    deadlineMonth: "December",
    officialLink: "https://www.tatatrusts.org",
    documentsRequired: [
      "Mark sheets of all previous semesters / 12th board",
      "Original fee receipt for current academic year",
      "Income tax returns (ITR) or Tehsildar income certificate",
      "Cancelled cheque / Bank passbook"
    ],
    applicationProcess: [
      "Fill online scholarship application on Tata Trusts portal",
      "Shortlisted candidates undergo telephonic/in-person verification interview"
    ],
    tags: ["Tata Trusts", "CSR", "Tuition Fee Grant", "Engineering & Medical"]
  },
  {
    id: "ind-pvt-02",
    title: "Reliance Foundation Undergraduate & Postgraduate Scholarships",
    section: "india",
    type: "private",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor", "Master"],
    streams: ["All Streams (UG)", "Artificial Intelligence", "Computer Science", "Mathematics", "Renewable Energy (PG)"],
    targetGroup: ["Merit-cum-Means", "High Potential Youth"],
    fundingAmount: "Up to ₹2,00,000 (UG) and Up to ₹6,00,000 (PG) over degree duration",
    amountVal: 200000,
    coverage: "Tuition and living support plus leadership development workshops and mentorship network",
    fundingAgency: "Reliance Foundation",
    eligibility: "UG: 1st year students enrolled in any stream with >= 60% in 12th & family income < ₹15 LPA (priority < ₹2.5 LPA). PG: 1st year PG in computer science, AI, data science, renewable energy.",
    deadline: "August - October (Annual)",
    deadlineMonth: "October",
    officialLink: "https://www.scholarships.reliancefoundation.org",
    documentsRequired: [
      "Class 10 and 12 mark sheets",
      "Current college bonafide certificate & fee receipt",
      "Family income proof (Salary slip, Form 16, Income Certificate)",
      "Statement of Purpose (for PG)"
    ],
    applicationProcess: [
      "Online eligibility questionnaire and registration",
      "Take mandatory online aptitude test (60 mins)",
      "Final selection based on aptitude score and socioeconomic criteria"
    ],
    tags: ["Reliance", "Large Cohort (5000 UG awards)", "Aptitude Test", "Prestigious"]
  },
  {
    id: "ind-pvt-03",
    title: "Aditya Birla Group Scholarships",
    section: "india",
    type: "private",
    category: "Scholarship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Engineering (IITs/BITS)", "Management (IIMs/XLRI)", "Law (National Law Universities)"],
    targetGroup: ["Top Rankers in Premier Institutes"],
    fundingAmount: "₹1,00,000 to ₹1,80,000 per year or entire tuition fee",
    amountVal: 180000,
    coverage: "Covers academic tuition and hostel fees, renewable based on annual top-tier performance",
    fundingAgency: "Aditya Birla Group",
    eligibility: "Top 20 rankers admitted to select premier institutes (IITs - Bombay, Delhi, Madras, Kanpur, Kharagpur; BITS Pilani; IIMs; NLSIU, NALSAR, etc.).",
    deadline: "July - September (Beginning of academic session)",
    deadlineMonth: "September",
    officialLink: "https://www.adityabirlascholars.net",
    documentsRequired: [
      "Institute admission rank / entrance rank letter",
      "Essays on leadership, ethics, and life goals",
      "Dean / Director endorsement form"
    ],
    applicationProcess: [
      "Dean's office at participating premier institutes nominates top candidates",
      "Shortlisted candidates write essays and appear before national selection jury in Mumbai"
    ],
    tags: ["Premier Institutes", "IIT / IIM / NLU", "Leadership", "Merit"]
  },
  {
    id: "ind-pvt-04",
    title: "HDFC Badhte Kadam / HDFC Bank Parivartan's ECSS Programme",
    section: "india",
    type: "private",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor", "Master"],
    streams: ["General UG/PG", "Professional Courses (Engineering, MBBS, Law, CA)"],
    targetGroup: ["Need-based", "Crisis Support", "Disadvantaged Families"],
    fundingAmount: "Up to ₹75,000 per year",
    amountVal: 75000,
    coverage: "Cash support directly into bank account to prevent student dropouts due to financial crisis",
    fundingAgency: "HDFC Bank CSR (Parivartan)",
    eligibility: "Students who have faced family crisis / income loss or family annual income <= ₹2.5 Lakhs with >= 55% in qualifying examination.",
    deadline: "August - November (Annual)",
    deadlineMonth: "November",
    officialLink: "https://www.hdfcbank.com",
    documentsRequired: [
      "Previous year marksheet (min 55%)",
      "Government issued ID and address proof",
      "Income proof / Crisis proof certificate (e.g. death certificate of earning member, job loss document)",
      "Admission proof (College ID / Fee slip)"
    ],
    applicationProcess: [
      "Submit application through Buddy4Study / HDFC Parivartan portal",
      "Telephonic verification and document scrutiny",
      "Direct fund transfer to beneficiary account"
    ],
    tags: ["Crisis Support", "HDFC Bank", "Financial Aid", "All Streams"]
  },
  {
    id: "ind-pvt-05",
    title: "L'Oréal India For Young Women in Science Scholarship",
    section: "india",
    type: "private",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor"],
    streams: ["Science", "Pure Sciences", "Applied Sciences", "Engineering", "Medicine", "Biotech"],
    targetGroup: ["Women / Girls Only", "Post-12th Passed"],
    fundingAmount: "₹2,50,000 disbursed over graduation period",
    amountVal: 250000,
    coverage: "Covers college fees and academic expenses throughout graduation",
    fundingAgency: "L'Oréal India CSR",
    eligibility: "Female students who passed Class 12 with >= 85% in PCB/PCM in the current academic year, enrolled in scientific graduation, family income <= ₹6 LPA.",
    deadline: "November - January (Annual)",
    deadlineMonth: "January",
    officialLink: "https://www.loreal.com/en/india",
    documentsRequired: [
      "Attested copy of 12th Marksheet (min 85%)",
      "Age proof (10th marksheet or Birth certificate)",
      "Income certificate (< ₹6 LPA)",
      "College admission letter & fee receipt"
    ],
    applicationProcess: [
      "Online application with essays on why the applicant chose science",
      "Shortlisting followed by personal/video interview by an expert panel of scientists"
    ],
    tags: ["Women in Science", "Post-12th", "L'Oréal", "STEM Girls"]
  },

  // --- FUNDED INTERNSHIPS & RESEARCH PROJECTS (INDIA) ---
  {
    id: "ind-int-01",
    title: "Summer Research Fellowship Programme (SRFP) - IASc, INSA & NASI",
    section: "india",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Science", "Mathematics", "Engineering", "Life Sciences", "Earth Sciences"],
    targetGroup: ["UG & PG Students across India"],
    fundingAmount: "₹12,000/month stipend + Round-trip train fare + Free accommodation",
    amountVal: 24000,
    coverage: "Full fellowship for 8 weeks (May - July) working with fellows of the National Science Academies",
    fundingAgency: "Indian Academy of Sciences (IASc), INSA & NASI",
    eligibility: "Students studying in 2nd/3rd year of B.Sc/B.Tech or 1st year of M.Sc/M.Tech with consistent >= 65% aggregate throughout schooling.",
    deadline: "October - November 30 (Annual)",
    deadlineMonth: "November",
    officialLink: "https://web-japps.ias.ac.in",
    documentsRequired: [
      "Comprehensive write-up / brief research interest statement (150-250 words)",
      "Scanned mark sheets from 10th standard onwards",
      "Teacher recommendation letter submitted directly online by referee"
    ],
    applicationProcess: [
      "Complete online application and select preferred academy guides/scientists",
      "Teacher uploads confidential recommendation letter using unique token",
      "Results announced in February-March; summer placement in May-July"
    ],
    tags: ["Premier Research", "National Academies", "Summer Fellowship", "IISc/IIT Labs"]
  },
  {
    id: "ind-int-02",
    title: "IIT Madras Summer Fellowship Programme / IIT Bombay Summer Internship (SURGE / SPARK)",
    section: "india",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Engineering", "Computer Science", "Data Science", "Humanities", "Sciences"],
    targetGroup: ["Non-IIT Undergraduate Students"],
    fundingAmount: "₹6,000 to ₹10,000/month stipend + subsidized campus hostel",
    amountVal: 18000,
    coverage: "2-month summer research experience under world-class IIT professors",
    fundingAgency: "Indian Institutes of Technology (IIT Madras, IIT Kanpur SURGE, IIT Roorkee SPARK)",
    eligibility: "3rd year B.Tech/B.E. or Integrated M.Tech students or 1st year M.Sc./MA students with top 10% class rank / CGPA >= 8.0.",
    deadline: "January - March (Annual)",
    deadlineMonth: "March",
    officialLink: "https://sfp.iitm.ac.in",
    documentsRequired: [
      "No Objection Certificate (NOC) from parent institution",
      "Rank certificate / Bonafide certificate from HOD",
      "Academic Transcripts",
      "Statement of Purpose"
    ],
    applicationProcess: [
      "Apply through respective IIT fellowship portal choosing department & faculty mentors",
      "Faculty review shortlisted resumes and conduct short virtual interviews"
    ],
    tags: ["IIT Research", "Summer Project", "Hands-on Tech", "Funded"]
  },
  {
    id: "ind-int-03",
    title: "TIFR Visiting Students' Research Programme (VSRP)",
    section: "india",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Physics", "Chemistry", "Biology", "Mathematics", "Computer & Systems Sciences"],
    targetGroup: ["Pre-final year UG and 1st year PG students"],
    fundingAmount: "₹7,000/month stipend + Free on-campus accommodation + Travel allowance",
    amountVal: 14000,
    coverage: "Intensive 7-week research internship at Tata Institute of Fundamental Research, Mumbai",
    fundingAgency: "Tata Institute of Fundamental Research (TIFR), DAE",
    eligibility: "Pre-final year students of B.Sc./B.E./B.Tech or 1st year M.Sc./M.E./M.Tech with high academic standing.",
    deadline: "January - February (Annual)",
    deadlineMonth: "February",
    officialLink: "https://www.tifr.res.in/~vsrp",
    documentsRequired: [
      "Academic Transcripts from 10th standard",
      "Two referee recommendation letters",
      "Statement of Research Interest"
    ],
    applicationProcess: [
      "Apply online at TIFR VSRP portal",
      "Selected fellows conduct project under leading experimental/theoretical physicists and mathematicians"
    ],
    tags: ["Fundamental Science", "TIFR", "High Prestige", "Summer Project"]
  },

  // ==========================================
  // SECTION 2: OPPORTUNITIES IN ABROAD
  // ==========================================

  // --- GOVERNMENT & MULTILATERAL SCHOLARSHIPS (ABROAD) ---
  {
    id: "abr-gov-01",
    title: "Erasmus Mundus Joint Master Degrees (EMJM) - European Union",
    section: "abroad",
    type: "government",
    category: "Scholarship",
    educationLevel: ["Master"],
    streams: ["All Disciplines", "STEM", "Humanities", "Environmental Science", "Economics"],
    targetGroup: ["Global applicants, Indians are historically #1 recipients"],
    fundingAmount: "€1,400/month (₹1.25 Lakh/m) + 100% Tuition Waiver + €3,000/yr Travel Grant",
    amountVal: 3500000,
    coverage: "Fully funded: Full tuition at 2 to 4 European universities, monthly living stipend for 24 months, visa, travel and health insurance",
    fundingAgency: "European Commission, European Union",
    eligibility: "Bachelor's degree or in final year of UG. High academic standing. No nationality restrictions. English proficiency (IELTS/TOEFL).",
    deadline: "October - January (Programme-specific deadlines)",
    deadlineMonth: "January",
    officialLink: "https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en",
    documentsRequired: [
      "Undergraduate Degree / Transcripts",
      "Statement of Purpose / Motivation Letter customized for each program",
      "2-3 Letters of Recommendation",
      "Europass format CV",
      "English Proficiency score (IELTS 6.5-7.5 / TOEFL)"
    ],
    applicationProcess: [
      "Browse Erasmus Mundus Catalogue and pick up to 3 master programs",
      "Apply directly to the consortium website before deadline",
      "Consortium selects top candidates for EU funded scholarship slots"
    ],
    tags: ["Europe", "Fully Funded", "Master Degree", "Multi-Country Study"]
  },
  {
    id: "abr-gov-02",
    title: "Chevening Scholarships - United Kingdom",
    section: "abroad",
    type: "government",
    category: "Scholarship",
    educationLevel: ["Master"],
    streams: ["All Disciplines", "Public Policy", "International Relations", "Tech", "Economics", "Law"],
    targetGroup: ["Future leaders with 2+ years work experience"],
    fundingAmount: "100% UK University Tuition Fees + £1,400/month living stipend + Flights",
    amountVal: 4000000,
    coverage: "Fully funded 1-year Master's degree at any UK university (Oxford, Cambridge, LSE, UCL, Imperial, etc.)",
    fundingAgency: "Foreign, Commonwealth & Development Office (FCDO), UK Government",
    eligibility: "Indian citizen. Completed UG degree. Minimum 2 years of work experience (2,800 hours - full-time, part-time or internships). Return to India for min 2 years after study.",
    deadline: "August - Early November (Annual)",
    deadlineMonth: "November",
    officialLink: "https://www.chevening.org/scholarships",
    documentsRequired: [
      "4 mandatory essays: Leadership, Networking, Studying in the UK, Career Plan",
      "Degree transcripts",
      "Unconditional offer from at least one eligible UK Master's course",
      "Two professional/academic references"
    ],
    applicationProcess: [
      "Submit comprehensive online application with 4 leadership essays by November",
      "Shortlisted candidates invited for interview at British High Commission, New Delhi in March-April",
      "Secure university offer by July to confirm scholarship"
    ],
    tags: ["United Kingdom", "Prestigious", "1-Year Master", "Full Tuition + Stipend"]
  },
  {
    id: "abr-gov-03",
    title: "Fulbright-Nehru Master's & Doctoral Fellowships - United States",
    section: "abroad",
    type: "government",
    category: "Fellowship",
    educationLevel: ["Master", "PhD"],
    streams: ["Arts & Culture", "Environmental Science", "Public Health", "Economics", "Gender Studies", "Public Policy"],
    targetGroup: ["Outstanding Indian graduates and PhD scholars"],
    fundingAmount: "100% Tuition Fees + J-1 Visa sponsorship + Monthly living stipend + Airfare",
    amountVal: 5500000,
    coverage: "Complete coverage of US university tuition, health insurance, living allowance, and enrichment activities",
    fundingAgency: "United States-India Educational Foundation (USIEF)",
    eligibility: "Completed equivalent to US bachelor's degree with >= 55% marks. Minimum 3 years full-time work experience. Substantial community leadership.",
    deadline: "February - May (Annual for next year's entry)",
    deadlineMonth: "May",
    officialLink: "https://www.usief.org.in",
    documentsRequired: [
      "Detailed Study/Research Objective essay",
      "Personal Statement",
      "Three confidential letters of recommendation",
      "Transcripts & Employer Endorsement (if applicable)"
    ],
    applicationProcess: [
      "Apply through the Embark online portal via USIEF",
      "National selection committee interviews in August",
      "USIEF coordinates university placement and J-1 visa processing"
    ],
    tags: ["USA", "USIEF", "Premier Fellowship", "Fully Funded"]
  },
  {
    id: "abr-gov-04",
    title: "DAAD Study Scholarships & Research Grants - Germany",
    section: "abroad",
    type: "government",
    category: "Scholarship",
    educationLevel: ["Master", "PhD"],
    streams: ["Engineering", "Informatics", "Natural Sciences", "Humanities", "Architecture", "Economics"],
    targetGroup: ["Graduates and Doctoral candidates"],
    fundingAmount: "€934 to €1,300/month + Health Insurance + Travel Subsidy + Language Course",
    amountVal: 1800000,
    coverage: "Monthly allowance for living expenses, travel grant, German language preparation course",
    fundingAgency: "German Academic Exchange Service (DAAD)",
    eligibility: "Completed Bachelor's degree within last 6 years with excellent grades. English or German proficiency depending on course.",
    deadline: "October - November (For winter semester entry)",
    deadlineMonth: "November",
    officialLink: "https://www.daad.in",
    documentsRequired: [
      "DAAD online application form",
      "Curriculum Vitae (tabular format)",
      "Detailed Letter of Motivation (1-3 pages)",
      "University degree certificates and transcripts with grading scale",
      "Proof of language skills (IELTS / TestDaF)"
    ],
    applicationProcess: [
      "Submit application through DAAD portal",
      "Evaluation by an independent academic committee",
      "Enrollment at public tuition-free German university"
    ],
    tags: ["Germany", "No Tuition Fee", "DAAD", "Master & PhD"]
  },
  {
    id: "abr-gov-05",
    title: "MEXT (Monbukagakusho) Japanese Government Scholarship",
    section: "abroad",
    type: "government",
    category: "Scholarship",
    educationLevel: ["After 12th", "Bachelor", "Master", "PhD"],
    streams: ["Undergraduate: Social Sciences, Humanities, Natural Sciences; Research: All fields"],
    targetGroup: ["Indian citizens seeking UG or PG study in Japan"],
    fundingAmount: "¥117,000 to ¥145,000/month (₹65,000 - ₹80,000/m) + 100% Tuition Waiver + Return Flight",
    amountVal: 2200000,
    coverage: "Exemption from entrance examination and tuition fees at national universities, monthly stipend, travel to Japan",
    fundingAgency: "Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan",
    eligibility: "UG: Passed Class 12, age 17-25. PG/Research: Under 35 years old, completed 16 years of education with >= 65% aggregate.",
    deadline: "May - June (Annual via Embassy Recommendation Track)",
    deadlineMonth: "June",
    officialLink: "https://www.in.emb-japan.go.jp",
    documentsRequired: [
      "Application Form & Field of Study/Research Plan",
      "Academic Marksheets from Class 10 onward",
      "Recommendation Letter from Principal/Dean",
      "Medical Certificate in MEXT format"
    ],
    applicationProcess: [
      "Submit application to Embassy of Japan in New Delhi",
      "Written examination (English, Math, Japanese/Science) and personal interview",
      "Final approval from MEXT Tokyo"
    ],
    tags: ["Japan", "Undergraduate & PG", "Embassy Track", "Full Ride"]
  },
  {
    id: "abr-gov-06",
    title: "National Overseas Scholarship (NOS) for SC, ST & Landless Agricultural Labourers",
    section: "abroad",
    type: "government",
    category: "Scholarship",
    educationLevel: ["Master", "PhD"],
    streams: ["Engineering", "Management", "Pure & Applied Sciences", "Agriculture", "Medicine", "Social Sciences"],
    targetGroup: ["SC", "De-notified Nomadic Tribes", "Traditional Artisans", "Landless Labourers"],
    fundingAmount: "100% Foreign Tuition Fees + $15,400/yr (USA) or £9,900/yr (UK) living allowance + Airfare",
    amountVal: 4500000,
    coverage: "Full tuition, maintenance allowance, contingency allowance, visa fee, health insurance, economy class airfare",
    fundingAgency: "Ministry of Social Justice and Empowerment, Govt. of India",
    eligibility: "Total family income <= ₹8.00 Lakh per annum. Candidates must have unconditional admission in top 500 QS ranked foreign university. Minimum 60% in bachelor's/master's.",
    deadline: "February - March (Cycle 1) & September - October (Cycle 2)",
    deadlineMonth: "March",
    officialLink: "https://nosmsje.gov.in",
    documentsRequired: [
      "Valid Caste Certificate",
      "Income Certificate (< ₹8 LPA) for current financial year",
      "Unconditional Admission Letter from QS Top 500 Foreign University",
      "Valid Indian Passport",
      "Class 10, 12, UG/PG marksheets"
    ],
    applicationProcess: [
      "Secure unconditional offer letter from top 500 foreign university",
      "Register and upload documents on nosmsje.gov.in portal",
      "Selection board verifies credentials and issues award letter"
    ],
    tags: ["Indian Govt Funded Abroad", "Top 500 Global Universities", "Full Ride", "Empowerment"]
  },

  // --- PRIVATE TRUSTS & PHILANTHROPIC SCHOLARSHIPS (ABROAD) ---
  {
    id: "abr-pvt-01",
    title: "JN Tata Endowment for the Higher Education of Indians",
    section: "abroad",
    type: "private",
    category: "Scholarship",
    educationLevel: ["Master", "PhD"],
    streams: ["All Disciplines", "Engineering", "Medicine", "Sciences", "Humanities", "Law"],
    targetGroup: ["Indian graduates going abroad for Master / PhD"],
    fundingAmount: "Loan Scholarship up to ₹10,00,000 + Gift Scholarship up to ₹7,50,000",
    amountVal: 1000000,
    coverage: "Repayable loan scholarship with nominal interest (2% rebate on timely repayment) plus non-repayable gift grants for top scholars",
    fundingAgency: "Tata Trusts (JN Tata Endowment)",
    eligibility: "Indian graduates with minimum 60% aggregate marks in Bachelor's or Master's, having applied to or admitted in reputable universities abroad.",
    deadline: "January - March (Annual)",
    deadlineMonth: "March",
    officialLink: "https://www.jntataendowment.org",
    documentsRequired: [
      "Statement of Purpose",
      "Graduation Marksheets & Transcripts",
      "GRE / GMAT / IELTS / TOEFL score cards",
      "Admission letters / applied universities list",
      "One Academic / Professional Letter of Recommendation"
    ],
    applicationProcess: [
      "Fill online application on JN Tata Endowment portal",
      "Online thinking skills assessment test",
      "Technical interview with a panel of Indian & international experts"
    ],
    tags: ["Tata Trusts", "Study Abroad", "Loan + Gift Grant", "All Streams"]
  },
  {
    id: "abr-pvt-02",
    title: "Inlaks Shivdasani Foundation Scholarships",
    section: "abroad",
    type: "private",
    category: "Scholarship",
    educationLevel: ["Master", "PhD"],
    streams: ["Humanities", "Social Sciences", "Fine Arts", "Architecture", "Environment", "Law", "Sciences"],
    targetGroup: ["Outstanding Indian youth with exceptional talent"],
    fundingAmount: "Up to $100,000 (Approx. ₹83 Lakhs) for tuition, living expenses and travel",
    amountVal: 8300000,
    coverage: "Covers tuition fees, adequate living expenses, one-way flight and health insurance for North America & Europe top institutions",
    fundingAgency: "Inlaks Shivdasani Foundation",
    eligibility: "Indian citizen holding a first-class degree from a recognized university. Age <= 30 years. Must hold unconditional offer from top university in USA, UK, or Europe.",
    deadline: "February - March (Annual)",
    deadlineMonth: "March",
    officialLink: "https://www.inlaksfoundation.org",
    documentsRequired: [
      "Unconditional Admission Letter",
      "Portfolio of work (for Arts, Film, Design, Architecture)",
      "Detailed CV & Academic Transcripts",
      "Evidence of outstanding extracurricular or academic distinction"
    ],
    applicationProcess: [
      "Online portal submission in February-March",
      "Preliminary interview round in April-May",
      "Final high-level jury interview in Mumbai / Delhi in late May"
    ],
    tags: ["Elite", "US / UK / Europe", "Arts & Sciences", "Full Coverage"]
  },
  {
    id: "abr-pvt-03",
    title: "Narotam Sekhsaria Scholarship Programme",
    section: "abroad",
    type: "private",
    category: "Scholarship",
    educationLevel: ["Master", "PhD"],
    streams: ["Engineering", "Management", "Natural Sciences", "Law", "Architecture", "Social Sciences"],
    targetGroup: ["Merit-based Indian graduates"],
    fundingAmount: "Interest-free Loan Scholarship up to ₹20,00,000",
    amountVal: 2000000,
    coverage: "Pure interest-free loan scholarship repayable over 1 to 4 years post completion of degree abroad",
    fundingAgency: "Narotam Sekhsaria Foundation",
    eligibility: "Indian nationals residing in India, below 30 years of age, holding an undergraduate degree from an accredited university with consistent first-class track record.",
    deadline: "January - March (Annual)",
    deadlineMonth: "March",
    officialLink: "https://pg.nsfoundation.co.in",
    documentsRequired: [
      "Undergraduate and Post-graduate Marksheets",
      "GRE / GMAT / IELTS score cards",
      "Letter of admission from international institution",
      "Statement of Purpose and 2 Letters of Recommendation"
    ],
    applicationProcess: [
      "Submit online application form with application fee",
      "Shortlisted candidates called for in-person interview in Mumbai by expert academicians"
    ],
    tags: ["Interest-Free", "Top Global Universities", "Mentorship Network"]
  },
  {
    id: "abr-pvt-04",
    title: "Aga Khan Foundation International Scholarship Programme (ISP)",
    section: "abroad",
    type: "private",
    category: "Scholarship",
    educationLevel: ["Master", "PhD"],
    streams: ["All Disciplines", "Development Studies", "Architecture", "Engineering", "Public Health", "Management"],
    targetGroup: ["Needy and brilliant students from developing countries"],
    fundingAmount: "50% Grant + 50% Loan covering full tuition and living expenses",
    amountVal: 3000000,
    coverage: "Covers tuition fees and living expenses throughout the degree program",
    fundingAgency: "Aga Khan Development Network (AKDN)",
    eligibility: "Consistent excellent academic records, genuine financial need, admission to a highly reputable university abroad, under 30 years of age.",
    deadline: "January - March (Annual)",
    deadlineMonth: "March",
    officialLink: "https://www.akdn.org/our-agencies/aga-khan-foundation/international-scholarship-programme",
    documentsRequired: [
      "AKF Application form",
      "Financial budget breakdown and proof of inability to finance degree",
      "Valid admission offer from foreign university",
      "Comprehensive transcripts and 3 referee letters"
    ],
    applicationProcess: [
      "Contact local Aga Khan Foundation office in New Delhi for application packet",
      "Complete extensive financial evaluation and personal interview"
    ],
    tags: ["Need + Merit", "50% Grant 50% Loan", "Master & PhD"]
  },

  // --- FUNDED INTERNSHIPS & SUMMER RESEARCH (ABROAD) ---
  {
    id: "abr-int-01",
    title: "Mitacs Globalink Research Internship (Canada)",
    section: "abroad",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["All Disciplines", "Engineering", "Science", "Math", "Humanities", "Social Sciences"],
    targetGroup: ["Full-time UG & Combined Master's students in India"],
    fundingAmount: "CAD $8,000+ (Full flight + Housing + CAD $200/wk food stipend + Health insurance)",
    amountVal: 500000,
    coverage: "Fully funded 12-week summer research internship at top Canadian universities (Toronto, UBC, McGill, Waterloo, etc.)",
    fundingAgency: "Mitacs Canada & Govt. of Canada",
    eligibility: "Full-time enrolled undergraduate student in 2nd or 3rd year of 4-year degree (or 3rd/4th of 5-year integrated), minimum 80% or 8.0 CGPA.",
    deadline: "August - September 20 (Annual for next summer)",
    deadlineMonth: "September",
    officialLink: "https://www.mitacs.ca/our-programs/globalink-research-internship-students",
    documentsRequired: [
      "Official academic transcripts in English",
      "Academic CV in Mitacs template",
      "Minimum 1 Letter of Reference from professor",
      "Research rationale for 3-7 chosen Canadian research projects"
    ],
    applicationProcess: [
      "Search project database and select 3 to 7 projects across min 3 Canadian provinces",
      "Canadian professors interview shortlisted Indian candidates via Skype/Teams",
      "Mitacs matches candidate to project; full visa and flight handled"
    ],
    tags: ["Canada", "Fully Funded", "Summer Research", "Mitacs", "Top Ranked"]
  },
  {
    id: "abr-int-02",
    title: "DAAD WISE (Working Internships in Science and Engineering) - Germany",
    section: "abroad",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor"],
    streams: ["Engineering", "Natural Sciences", "Mathematics", "Computer Science"],
    targetGroup: ["Indian undergraduate engineering & science students"],
    fundingAmount: "€934/month stipend + €1,075 Travel Subsidy + Health Insurance",
    amountVal: 275000,
    coverage: "2 to 3 months research stay at a German public university or research institute (Max Planck, Fraunhofer, Helmholtz)",
    fundingAgency: "German Academic Exchange Service (DAAD)",
    eligibility: "5th or 6th semester B.Tech/B.E. or 5th-8th semester Integrated M.Tech students from select Indian universities with CGPA >= 8.5.",
    deadline: "September - November 1 (Annual)",
    deadlineMonth: "November",
    officialLink: "https://www.daad.in/en/find-funding/scholarship-database/?type=scholarship&q=WISE",
    documentsRequired: [
      "Invitation letter from German host professor / institute",
      "Form 'Approval by the Indian Host Institute' signed by Dean/HOD",
      "Detailed project description (Agreed upon with German mentor)",
      "Curriculum Vitae and academic transcripts"
    ],
    applicationProcess: [
      "Reach out to German university professors and secure written invitation letter",
      "Submit official DAAD WISE application on DAAD online portal by November 1"
    ],
    tags: ["Germany", "WISE", "German Labs", "Funded Internship"]
  },
  {
    id: "abr-int-03",
    title: "CERN Summer Student Programme (Geneva, Switzerland)",
    section: "abroad",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Physics", "Computing & Software", "Electrical & Mechanical Engineering", "Mathematics"],
    targetGroup: ["UG & PG Students from member & associate member states (India is Associate Member)"],
    fundingAmount: "90 CHF/day (Approx. ₹8,500/day = ₹2.5 Lakhs/m) + Travel Allowance + Health Insurance",
    amountVal: 650000,
    coverage: "8 to 13 weeks fully funded stay in Geneva, working on Large Hadron Collider (LHC) experiments + comprehensive lecture series",
    fundingAgency: "European Organization for Nuclear Research (CERN)",
    eligibility: "Completed at least 3 years of full-time university study in physics, engineering or computing. Fluent in English or French.",
    deadline: "November - January (Annual)",
    deadlineMonth: "January",
    officialLink: "https://careers.cern/summer",
    documentsRequired: [
      "Curriculum Vitae in English",
      "Official academic transcripts",
      "Two reference letters from university lecturers"
    ],
    applicationProcess: [
      "Submit application via SmartRecruiters CERN portal",
      "Selection board matches candidate profiles with ongoing CERN detector & computing projects"
    ],
    tags: ["CERN", "Switzerland", "LHC Physics", "World Famous", "High Stipend"]
  },
  {
    id: "abr-int-04",
    title: "SN Bose Scholars Program (United States)",
    section: "abroad",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["Atmospheric Sciences", "Chemical Sciences", "Engineering", "Mathematical Sciences", "Life Sciences"],
    targetGroup: ["Top Indian undergraduate and master's students"],
    fundingAmount: "$2,500+ stipend + Round-trip international airfare + Health insurance",
    amountVal: 350000,
    coverage: "10-12 weeks summer research placement at top US universities (MIT, Harvard, Caltech, Stanford, Wisconsin-Madison, etc.)",
    fundingAgency: "IUSSTF (Indo-US Science and Technology Forum) & WINStep Forward",
    eligibility: "Indian citizen currently enrolled in 3rd/4th year B.Tech or 1st year M.Sc./M.Tech with CGPA >= 8.5 / top 5% rank in class.",
    deadline: "September - October (Annual)",
    deadlineMonth: "October",
    officialLink: "https://iusstf.org/sn-bose-scholars-program",
    documentsRequired: [
      "Statement of Purpose (2 pages)",
      "Two letters of recommendation on institutional letterhead",
      "No Objection Certificate from parent institution",
      "Official transcripts"
    ],
    applicationProcess: [
      "Submit online application via IUSSTF portal",
      "IUSSTF coordinates institutional placement across premier US research labs"
    ],
    tags: ["USA", "IUSSTF", "Premier Labs", "Indo-US Exchange"]
  },
  {
    id: "abr-int-05",
    title: "Charpak Summer Internship Program - France",
    section: "abroad",
    type: "government",
    category: "Internship",
    educationLevel: ["Bachelor", "Master"],
    streams: ["All Disciplines", "Science", "Engineering", "Economics", "Management", "Social Sciences"],
    targetGroup: ["Indian students enrolled in Indian higher education institutions"],
    fundingAmount: "€700/month living allowance + Student visa fee waiver + Free social security",
    amountVal: 200000,
    coverage: "2 to 3 months research internship at a French laboratory or university",
    fundingAgency: "Embassy of France in India / Campus France",
    eligibility: "Indian national enrolled in Indian university. Under 30 years old. Must have acceptance letter from a French lab/institution.",
    deadline: "January - March (Annual)",
    deadlineMonth: "March",
    officialLink: "https://www.inde.campusfrance.org/charpak-scholarships",
    documentsRequired: [
      "Acceptance letter / convention de stage from French laboratory",
      "Curriculum Vitae",
      "Statement of Purpose",
      "Recommendation letter from Indian professor"
    ],
    applicationProcess: [
      "Secure acceptance from a French laboratory or university",
      "Apply through Campus France India Charpak portal"
    ],
    tags: ["France", "Campus France", "Europe Internship", "Funded"]
  }
];

// Helper functions for metadata summaries
const GET_METRICS = () => {
  const indiaCount = OPPORTUNITIES_DATA.filter(o => o.section === "india").length;
  const abroadCount = OPPORTUNITIES_DATA.filter(o => o.section === "abroad").length;
  const govCount = OPPORTUNITIES_DATA.filter(o => o.type === "government").length;
  const pvtCount = OPPORTUNITIES_DATA.filter(o => o.type === "private").length;
  const internCount = OPPORTUNITIES_DATA.filter(o => o.category === "Internship").length;
  return {
    total: OPPORTUNITIES_DATA.length,
    india: indiaCount,
    abroad: abroadCount,
    government: govCount,
    private: pvtCount,
    internships: internCount
  };
};
