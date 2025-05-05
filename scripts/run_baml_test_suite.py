import os
import sys
import json
from email import policy
from email.parser import BytesParser

# Ensure the parent directory is in sys.path for absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from boundaryml.email_extractor import extract_newsletter_details

def extract_html_from_eml(eml_path):
    """Extracts the HTML content from an .eml file."""
    with open(eml_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            return part.get_content()
    return None

def main():
    input_folder = os.path.join("data", "emails")
    output_folder = os.path.join("evals", "tool_outputs")
    os.makedirs(output_folder, exist_ok=True)

    # Process all .eml files in the input folder
    for filename in os.listdir(input_folder):
        if not filename.endswith(".eml"):
            continue

        eml_path = os.path.join(input_folder, filename)
        email_html = extract_html_from_eml(eml_path)

        if not email_html:
            print(f"❌ No HTML found in {filename}")
            continue

        # Use the extract_newsletter_details function from email_extractor
        result = extract_newsletter_details(email_html)

        out_path = os.path.join(output_folder, f"boundaryml_output_{filename.replace('.eml', '.json')}")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        print(f"✅ Saved output: {out_path}")

if __name__ == "__main__":
    main()
