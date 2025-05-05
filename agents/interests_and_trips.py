import time

def infer_interests_agent(profile_context, model):
    prompt = f"""
    Based on this person's profile context, infer:
    1. Interests (as a comma-separated list)
    2. Past luxury travel destinations (as a comma-separated list)

    Context:
    {profile_context}

    Format:
    Interests: <comma-separated>
    PastTrips: <comma-separated>
    """
    response = model.generate_content(prompt).text
    time.sleep(4)
    return response