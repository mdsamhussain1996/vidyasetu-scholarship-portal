# VidyaSetu Design System: The Indian Student's Ruled Notebook

VidyaSetu is designed to feel written, structured, and maintained by a real teacher for real Indian students: plain, calm, respectful of low-bandwidth devices, and personal.

---

## 1. Visual Idea: The Ruled Notebook

Every Indian student who went to school recognizes the ruled notebook:
- **Blue ruled lines** (`#DCE4F2`) keep answers neat and calm.
- **Red margin line** (`#D2453C`) on the left reserves space for teacher notes and key demarcations.
- **Blue ink** (`#1E3A9E`) fills in the answers, links, and buttons.
- **Yellow highlighter** (`#FBE88A`) draws the eye only to urgent deadline dates.

We use this metaphor quietly:
1. **The Hero** sits on ruled lines with the red margin line on the left.
2. **The "Closing Soon" note** is pinned beside the hero, tilted slightly (~0.6°) with a soft shadow like a reminder slip clipped to a notebook page.
3. **The rest of the site** is clean paper (`#FAFBFD` / `#FFFFFF`), letting students read and scan without visual clutter.

---

## 2. Color Palette

All colors are stored as CSS variables in `css/style.css`.

| Token | Light Mode | Dark Mode | Role |
| :--- | :--- | :--- | :--- |
| `--paper` | `#FAFBFD` | `#151821` | Page background |
| `--white` | `#FFFFFF` | `#1C212D` | Card and sheet background |
| `--ruled-line` | `#DCE4F2` | `#2A3245` | Ruled lines & soft borders |
| `--ink-blue` | `#1E3A9E` | `#70A2FD` | Primary buttons, links, filled-in text |
| `--margin-red` | `#D2453C` | `#F87171` | Hero vertical margin, scam warning |
| `--text-main` | `#22252B` | `#F1F5F9` | High-contrast body text & titles |
| `--text-muted` | `#5A6070` | `#94A3B8` | Explanatory metadata & secondary labels |
| `--highlighter`| `#FBE88A` | `#544400` | Yellow marker behind critical deadline dates |

---

## 3. Typography & Shapes

- **Mukta** (`400`, `500`, `600`, `700`, `800`): Used for all headings, body text, tables, and buttons. Mukta was developed for Devanagari and Latin scripts, ensuring smooth bilingual rendering (Hindi and English).
- **Kalam** (`700`): Used **strictly** for handwritten accents:
  - Filled-in answers in the hero sentence.
  - Large milestone numbers in live counts.
  - Founder's personal signature.
  - *Rule: Never use Kalam for body paragraphs or general UI controls.*
- **Base Font Size**: `17px`–`18px`, with `line-height: 1.6` for effortless reading on cheap mobile screens.
- **Shapes**:
  - Buttons: Pill-shaped (`border-radius: 9999px`) with generous touch targets (minimum `44px × 44px`).
  - Containers: Subtle `6px` radius with `1.5px` border.
  - No glassmorphism, no gradient washes, no glowing card shadows.

---

## 4. Writing Rules (The Teacher's Voice)

1. **Speak like a good teacher talking to a Class 12 student**:
   - Short sentences. Everyday language. Use "you" and "we".
   - Avoid bureaucratic jargon without explanation. The first time a term appears, explain what it means in plain Hindi or English:
     - *DBT*: Direct Benefit Transfer to bank account.
     - *OTR*: One-Time Registration number.
     - *Bonafide certificate*: A letter signed by your college principal confirming you study there.
2. **Never invent or exaggerate**:
   - If a deadline is not published on the official circular, store `null` and show `"Expected: Usually Aug–Oct"`. Never display a fake exact date or an inaccurate "Open" badge.
   - Closed schemes clearly state: `"Closed. Next round expected May"`.
3. **No marketing hype**:
   - Prohibited words: *"Empowering"*, *"Comprehensive"*, *"Seamless"*, *"Unlock"*, *"Gateway"*, *"100% claim success"*, *"Premier"*.
   - Replace with plain facts: *"Scholarships, fellowships and research jobs for Indian students"*.
4. **Action-oriented buttons**:
   - State exactly what happens: `"Show me all 38"`, `"Apply on the official site"`, `"Save"`, `"Saved"`.
   - Avoid generic labels like `"Learn More"` or `"Click Here"`.

---

## 5. Performance & Mobile Standard

- Total page bundle under 300 KB before dataset loading.
- High accessibility: Color contrast exceeds 4.5:1 everywhere.
- Visible ink blue focus outline (`3px solid var(--ink-blue)`) for keyboard navigation.
- Tested across `360px`, `768px`, and `1280px` viewports.
