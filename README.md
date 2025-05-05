# Cold Email Generator for Startups - Product Requirements Document (PRD)

## 📝 Overview

The Cold Email Generator is a web-based tool for startups to automate the creation of personalized sales outreach emails. It uses CrewAI to orchestrate multi-agent workflows that research leads, analyze their company, and generate custom cold emails with optional follow-ups.

## 🎯 Goals

- Help startups speed up cold outreach campaigns.
- Increase personalization to boost reply rates.
- Automate lead research and email writing with AI agents.

## 📦 Key Features

- Upload CSV with `Name`, `Company`, and optionally `Job Title`.
- Automatically research company background (via SerpAPI / Google Search).
- Generate a personalized cold email + follow-up.
- View and export generated emails to updated CSV.
- Optional: Basic job dashboard to view generation status.

## 🧠 Agent Roles (CrewAI)

1. **Lead Research Agent**
   - Searches for recent news or descriptions of the company.
   - Gathers social or business context (e.g. hiring, funding, product launch).

2. **Company Analyzer Agent**
   - Summarizes company focus and identifies outreach opportunities.

3. **Email Generator Agent**
   - Crafts the first personalized email.

4. **Refiner Agent**
   - Enhances tone, grammar, and structure for higher conversion.

5. **Follow-Up Agent** (Optional)
   - Generates a follow-up email in case there’s no reply.

## ⚙️ Tech Stack

- **Frontend:** Streamlit (for MVP), or React (for production)
- **Backend:** Python (FastAPI or Flask)
- **Multi-Agent Framework:** [CrewAI](https://github.com/joaomdmoura/crewAI)
- **Search API:** SerpAPI, Google Programmable Search
- **Deployment:** Docker + GitHub Actions + Render/Heroku

## 🧪 Testing

- Unit tests for:
  - CSV parsing
  - Agent prompts and outputs
- Integration tests for:
  - End-to-end email generation pipeline
- Manual QA for UI/UX

## 🚀 Deployment Plan

1. Containerize app with Docker
2. Set up GitHub Actions for CI/CD
3. Deploy on Render or Railway for MVP

## 📁 File Structure

cold-email-generator/
├── backend/
│ ├── main.py
│ ├── agents/
│ ├── utils/
│ └── tests/
├── frontend/
│ ├── streamlit_app.py
│ ├── components/
├── data/
│ └── sample_input.csv
├── .github/workflows/
│ └── ci.yml
├── Dockerfile
├── README.md
└── requirements.txt

## 🧱 MVP Scope

- Upload CSV
- Generate first cold email
- Export results

## 📈 Future Enhancements

- Email tracking integration (SendGrid, Mailchimp API)
- Team collaboration features
- Lead scoring based on company potential

## 👤 Target Users

- Startup founders
- Sales development reps (SDRs)
- Growth marketers

## 📌 Assumptions

- Each agent runs sequentially per lead
- Lead enrichment relies on open web data
- Users manage email sending separately

---