import openai
import json
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env at project root
load_dotenv()

class BoundaryML:
    def __init__(self):
        self.client = openai.OpenAI()  # Uses OPENAI_API_KEY from environment

    def run(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured newsletter data as JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        content = response.choices[0].message.content.strip()

        # --- Robustly extract JSON from LLM output ---
        # 1. Try to find JSON inside a code block (``````)
        code_block = re.search(r"``````", content, re.DOTALL)
        if code_block:
            json_str = code_block.group(1)
        else:
            # 2. Fallback: Try to find the first {...} block in the response
            brace_block = re.search(r"(\{.*\})", content, re.DOTALL)
            if brace_block:
                json_str = brace_block.group(1)
            else:
                # 3. Fallback: Use the whole content (may fail)
                json_str = content

        try:
            return json.loads(json_str)
        except Exception as e:
            print("Error parsing LLM output:", e)
            return {"error": "Failed to parse LLM output", "raw": content}
