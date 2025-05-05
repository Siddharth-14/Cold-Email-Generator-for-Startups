# Product Requirements Document (PRD)

## Product Name

Cold Email Generator for B2C Startups

## Overview

This tool automates personalized cold email creation for B2C startup lead generation, specifically tailored for luxury travel experiences. The system ingests a CSV of lead names, infers contextual and lifestyle data, and generates customized marketing emails using Google's Gemini LLM with an agent-based architecture.

## Goals

* Automatically generate cold emails based on minimal input (Name)
* Include subject line and call-to-action (CTA)
* Maintain tone aligned with luxury brand image (Inspirato)
* Enable revision loop for quality control
* Deploy as a web-based interface (Streamlit)

## Key Features

* **Multi-Agent Workflow**

  * Research Agent: finds context on name
  * Interests & Travel Agent: infers preferences
  * Persona Builder: creates customer persona
  * Writer Agent: generates email
  * Editor Agent: reviews and loops for feedback
* **Retry Loop**: 5 iterations max until email is approved
* **Structured Email Output**: with Subject, Body, and CTA
* **Rate Limit Compliance**: waits 4 seconds per Gemini call
* **Streamlit Interface**: for uploading and downloading lead CSVs

## User Stories

1. As a marketer, I want to upload a list of leads and get tailored emails.
2. As a growth strategist, I want emails to reflect personal context.
3. As a product manager, I want emails to be high quality and brand-consistent.
4. As a startup founder, I want this to run easily with just a CSV file.

## Input Format

* CSV with column: `Name`

## Output Format

* Same CSV with additional column `Email`
* Email body structured:

  ```
  ----------
  Subject: [line here]

  [email body]

  CTA: [link or sentence]
  ----------
  ```

## Tech Stack

* **Python**
* **Google Generative AI SDK** (Gemini / chat-bison-001)
* **Streamlit**
* **pandas**
* **dotenv** for secrets

## Success Criteria

* [ ] At least 95% of generated emails pass editor approval in 1–3 retries
* [ ] Emails consistently follow structure and style
* [ ] Users can upload/download with no manual formatting
* [ ] Deployment on Streamlit Cloud with working API key support

## Future Enhancements

* Add Subject and CTA as separate columns
* Integrate LinkedIn search API for deeper context
* Enable team-level email review workflow
* Add analytics on open/click rate prediction

---

Owner: Siddharth Goradia
Date: May 2025