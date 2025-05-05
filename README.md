# Cold Email Generator for B2C Startups

This project generates personalized cold outreach emails for B2C startups using Google's Gemini (via Generative AI) and a multi-agent architecture. It is specifically designed for luxury travel experiences.

## 🚀 Features

* Google Gemini API (chat-bison-001) powered content generation
* Multi-agent architecture for research, interest inference, persona creation, email writing, and editing
* Editor feedback loop until email is approved
* Extracted email in structured format with Subject and CTA
* CSV-based input/output
* Streamlit UI for file upload and download

## 📁 Project Structure

```
├── agents/
│   ├── researcher.py          # Finds context from name
│   ├── interests_and_trips.py# Infers interests and travel history
│   ├── persona_builder.py    # Builds a customer persona
│   ├── email_writer.py       # Writes and revises email
│   └── editor.py             # Reviews and approves email
├── utils/
│   └── lead_loader.py        # CSV input/output
├── main.py                   # Pipeline logic with retry loop
├── frontend.py               # Streamlit UI
├── requirements.txt          # Dependencies
└── .env                      # GEMINI_API_KEY
```

## 🧪 Run Locally

1. Clone the repo
2. Add your API key in `.env`:

   ```bash
   GEMINI_API_KEY=your-google-api-key
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Launch the Streamlit app:

   ```bash
   streamlit run frontend.py
   ```

## 📝 Input Format

* CSV file with a column named `Name`

## 📤 Output Format

* Same CSV with an added column `Email`
* Email is structured like:

  ```
  ----------
  Subject: Explore the Amalfi Coast in Style

  Hi John, based on your love for fine dining and Mediterranean getaways, [Company] invites you...

  CTA: Book Your Luxury Escape → [Company Link]
  ----------
  ```

## 📦 Deployment

This project is ready to be deployed to [Streamlit Cloud](https://streamlit.io/cloud). You’ll need to set the GEMINI\_API\_KEY in the secret manager.

---