# VidyaSetu - National & International Opportunities Portal 🎓

VidyaSetu is a modern web portal designed specifically for **Indian students** across all educational levels (**After 12th, Bachelor's, Master's, and PhD**) to discover:
- 🏛️ **Government Schemes & Funds** (Central & State Govt, DBT compliant, MoE, DST, AICTE, CSIR)
- 💼 **Private Philanthropic & CSR Funds** (Tata Trusts, Reliance Foundation, Aditya Birla, HDFC Parivartan, L'Oréal)
- 🌍 **Fully Funded Study Abroad Opportunities** (Erasmus Mundus, Chevening, Fulbright-Nehru, DAAD, MEXT, Inlaks, NOS)
- 🔬 **Funded Research Projects & Summer Internships** (IASc-INSA-NASI SRFP, IIT Fellowships, TIFR VSRP, Mitacs Globalink, CERN, DAAD WISE)

---

## 🌟 Key Features

1. **Two Dedicated Core Sections**:
   - 🇮🇳 **Section 1: Opportunities in India**
   - 🌍 **Section 2: Opportunities Abroad**
2. **Interactive Student Profile Matcher ("Match My Profile")**:
   - 4-step quick quiz (Level → Stream → Category/Income → Destination) to generate personalized matches.
3. **Detail Modal with Document Checklist**:
   - Benefits and stipend breakdown.
   - Strict eligibility requirements.
   - Interactive checklist for required documents (Income certificate, Caste certificate, Marksheets, Bonafide).
   - Step-by-step application walkthrough.
   - Verified official portal direct links.
4. **Side-by-Side Comparison Tool**:
   - Compare up to 3 schemes simultaneously.
5. **Annual Deadline Calendar**:
   - Breakdown of opening and closing windows across Q1, Q2, Q3, and Q4.
6. **Bookmarking / Saved Schemes**:
   - Persisted locally via `localStorage`.
7. **Dark / Light Theme Toggle**:
   - High-contrast, glassmorphic modern UI.

---

## 🚀 Getting Started

Simply open `index.html` in any modern web browser or serve it with Python:

```bash
# Serve locally
python3 -m http.server 8089
```

Then visit [http://localhost:8089](http://localhost:8089).

---

## 📁 Project Structure

```text
scholarship-portal/
├── index.html        # Main HTML5 application structure
├── css/
│   └── style.css     # Design system, glassmorphism, responsive grid & themes
├── js/
│   ├── data.js       # Curated database of 40+ national & global schemes
│   └── app.js        # Search, filters, wizard, comparison, modals & bookmark engine
└── README.md         # Documentation
```

---

## 📜 License
MIT License
