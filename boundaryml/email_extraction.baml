function ExtractNewsletterDetails(email_body: string) -> NewsletterDetails {
    client "openai/gpt-4o"
    prompt #"
        Extract the following fields from this newsletter email body:
        - source (newsletter name)
        - date (YYYY-MM-DD)
        - story_count (number of stories)
        - stories: list of objects with title, summary, url, and category
        - notes (if present)

        Email body:
        {{ email_body }}

        Output JSON:
    "#
}

class NewsletterDetails {
    source string
    date string
    story_count int
    stories Story[]
    notes string
}

class Story {
    title string
    summary string
    url string
    category string
}
