import time

def editor_agent(email, model):
    prompt = f"""
    You are a senior editor at a luxury travel company. Review the following email:

    {email}

    Reply ONLY in this format:
    RESPONSE: APPROVED
    or
    RESPONSE: <feedback text>
    """
    response = model.generate_content(prompt).text
    time.sleep(4)
    return response.strip()