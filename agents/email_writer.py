import time

def writer_agent(persona, model, feedback=None):
    if feedback:
        prompt = f"""
        Revise the following email to address the feedback provided by the editor. Return ONLY the email content. Wrap the final email between lines of dashes ("----------") for extraction.

        Include the following format:
        Subject: <subject line>
        CTA: <call-to-action link or text>

        Feedback: {feedback}

        Persona:
        {persona}
        """
    else:
        prompt = f"""
        Write a personalized cold outreach email promoting Inspirato luxury travel experiences to the following persona:
        {persona}

        Return ONLY the email in this format and wrap it between dashes ("----------"):

        Subject: <subject line>

        <email body>

        CTA: <call-to-action>
        """
    response = model.generate_content(prompt).text
    time.sleep(4)
    return response