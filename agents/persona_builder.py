import time

def persona_agent(insights, model):
    prompt = f"""
    Based on the following lead insights, create a concise luxury travel customer persona:
    {insights}
    """
    response = model.generate_content(prompt).text
    time.sleep(4)
    return response