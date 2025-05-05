MAX_CHARS = 5000  # You can adjust this number as needed

from boundaryml.email_extraction import BoundaryML

def extract_newsletter_details(email_body):
    """
    Uses the BoundaryML class to extract newsletter details including stories.
    Truncates the email body to avoid exceeding LLM token limits.
    """
    # Truncate the email body if it's too long
    if len(email_body) > MAX_CHARS:
        print(f"Email body is {len(email_body)} characters; truncating to {MAX_CHARS} characters.")
        email_body = email_body[:MAX_CHARS]

    boundary_ml = BoundaryML()
    prompt = f"""Extract the following fields from this newsletter email body:
    - source (newsletter name)
    - date (YYYY-MM-DD)
    - story_count (number of stories)
    - stories: list of objects with title, summary, url, and category
    - notes (if present)

    Email body:
    {email_body}

    Output JSON:"""
    result = boundary_ml.run(prompt)
    return result
