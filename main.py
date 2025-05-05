from agents.researcher import research_agent
from agents.interests_and_trips import infer_interests_agent
from agents.persona_builder import persona_agent
from agents.email_writer import writer_agent
from agents.editor import editor_agent
from utils.lead_loader import load_leads, save_emails
import os
import sys
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel
import re
import streamlit as st
from streamlit.logger import get_logger

logger = get_logger(__name__)

load_dotenv()
configure(api_key=os.getenv("GEMINI_API_KEY"))
model = GenerativeModel(model_name="gemini-2.0-flash-lite")

def extract_email_body(text):
    match = re.search(r"-+\n(.+?)\n-+", text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()

def run_pipeline(input_file):
    leads = load_leads(input_file)
    emails = []

    for _, row in leads.iterrows():
        print(f"Processing lead: {row['Name']}")
        logger.info(f"Processing lead: {row['Name']}")
        profile_context = research_agent(row['Name'], model)
        print(f"Profile context: {row['Name']}")
        logger.info(f"Profile context: {row['Name']}")
        insights = infer_interests_agent(profile_context, model)
        print(f"Insights: {row['Name']}")
        logger.info(f"Insights: {row['Name']}")
        persona = persona_agent(insights, model)
        print(f"Persona: {row['Name']}")
        logger.info(f"Persona: {row['Name']}")

        email = writer_agent(persona, model)
        print(f"Initial email: {row['Name']}")
        logger.info(f"Initial email: {row['Name']}")
        retry_count = 0
        while retry_count < 5:
            review = editor_agent(email, model)
            print(f"Editor review: {row['Name']}")
            logger.info(f"Editor review: {row['Name']}")
            if review.upper().startswith("RESPONSE: APPROVED"):
                final_email = email
                break
            elif review.upper().startswith("RESPONSE:"):
                feedback = review[len("RESPONSE:"):].strip()
                email = writer_agent(persona, model, feedback=feedback)
                retry_count += 1
            else:
                break  # unknown response format, stop the loop
        else:
            final_email = extract_email_body(email)
            logger.info(f"Final email: {row['Name']}")
            
        emails.append(final_email)

    leads['Email'] = emails
    save_emails(leads, input_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Please provide the path to the leads CSV file as a command-line argument.")
    run_pipeline(sys.argv[1])