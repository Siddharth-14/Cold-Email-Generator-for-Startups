import time

def research_agent(name, model):
    prompt = f"""
    You are a Lead Researcher at a B2C luxury travel company.
    Given the lead's name, find or infer publicly available lifestyle and profile data to support personalization.

    Lead Name: {name}

    Return any useful context (job, location, age, online footprint, etc.).
    """
    response = model.generate_content(prompt).text
    time.sleep(4)
    return response