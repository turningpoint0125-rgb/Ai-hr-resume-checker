# 🤖 AI Recruitment Assistant (AI HR Resume Checker)

An LLM-powered Streamlit app that screens and ranks multiple resumes against a single job
description, producing per-candidate scores, skill gap analysis, hiring recommendations, and
ready-to-ask interview questions.

**🔗 Live app:** https://ai-hr-resume-checker-6pzfb9ydvv46k9gurvepze.streamlit.app/

## Features

- **Bulk resume screening** — upload one Job Description PDF and any number of resume PDFs.
- **Per-candidate AI analysis**, powered by Google's Gemini via LangChain, including:
  - A candidate summary
  - A percentage **match score** (color-coded: Excellent / Average / Poor)
  - **Matching**, **missing**, and **extra** skills relative to the JD
  - A **Hire / Interview / Reject** recommendation with justification
  - Suggested **interview questions** tailored to the resume
- **Ranking dashboard** — average score, highest score, candidate count, and a bar chart comparing
  all candidates.
- **Exportable results** — download the full candidate ranking as a CSV.

## Tech Stack

- **Frontend:** Streamlit
- **LLM orchestration:** LangChain + `langchain-google-genai` (Gemini)
- **PDF parsing:** pypdf
- **Data / export:** Pandas, openpyxl, XlsxWriter

## Project Structure

```
Ai-hr-resume-checker/
├── app.py                     # Main Streamlit app — upload, analyze, rank
├── ai/
│   ├── llm.py                   # Gemini LLM client setup
│   ├── chains.py                 # Orchestrates the analysis chain
│   ├── score_chain.py             # Match-score generation
│   ├── skill_match_chain.py        # Matching/missing/extra skill extraction
│   └── summary_chain.py            # Candidate summary generation
├── prompts/
│   ├── score_prompt.py
│   ├── skill_prompt.py
│   └── summary_prompt.py
├── components/
│   ├── sidebar.py               # Sidebar instructions
│   ├── ranking.py                 # Ranking table/UI
│   ├── dashboard.py                # Stats dashboard
│   └── uploader.py                  # File upload widgets
├── utils/
│   ├── pdf_reader.py             # PDF text extraction
│   ├── parser.py                   # Text/JSON parsing helpers
│   ├── prompts.py                   # Shared prompt utilities
│   ├── text_cleaner.py               # Text normalization
│   └── export.py                      # CSV/Excel export helpers
└── requirements.txt
```

## Getting Started

### 1. Clone and install

```bash
git clone https://github.com/turningpoint0125-rgb/Ai-hr-resume-checker.git
cd Ai-hr-resume-checker
pip install -r requirements.txt
```

### 2. Add your Google API key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_api_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/).

### 3. Run the app

```bash
streamlit run app.py
```

## Usage

1. Upload the **Job Description** as a PDF.
2. Upload one or more **Resumes** (PDF).
3. Click **Analyze Resume**.
4. Review each candidate's summary, score, skill gaps, and recommendation, then check the
   ranking dashboard and download the CSV if needed.

## Disclaimer

AI-generated scores and recommendations are meant to assist, not replace, human judgment in
hiring decisions.
