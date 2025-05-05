# AI Newsletter Extraction-Project
Extract and structure information from newsletter emails using LLMs and traditional NLP tools.
This project enables automated extraction of key details (like stories, summaries, and categories) from .eml newsletter files, with a focus on accuracy and reproducibility.

📦 Project Structure
text
AI-News-Extraction-Projec/
├── boundaryml/                # Extraction logic (BoundaryML, LLM prompts)
│   ├── __init__.py
│   ├── email_extraction.py
│   └── email_extractor.py
├── data/
│   └── emails/                # Raw .eml newsletter files
├── evals/
│   └── tool_outputs/          # Extracted JSON outputs from tools
├── labels/                    # Manual ground-truth labels for evaluation
│   ├── email_01.json
│   ├── email_02.json
│   └── email_03.json
├── scripts/                   # Runner and test scripts
│   ├── run_baml_test_suite.py
│   ├── test_baml.py
│   └── test_newspaper.py
├── tests/                     # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
🚀 Features
LLM Extraction: Uses GPT-4o (via OpenAI API) to extract structured data from newsletter emails.

Manual Labeling: Supports ground-truth JSON labels for benchmarking.

Prompt Engineering: Easily modify and optimize LLM prompts.

Evaluation Suite: Compare tool outputs to manual labels for accuracy assessment.

Extensible: Add new extraction tools or schemas as needed.

🛠️ Installation
Clone the repository:

bash
git clone https://github.com/yourusername/AI-News-Extraction-Projec.git
cd AI-News-Extraction-Projec
Install dependencies:

bash
pip install -r requirements.txt
Set up your OpenAI API key:

Create a .env file in the project root:

text
OPENAI_API_KEY=sk-...your-key-here...
📥 Usage
Add your .eml newsletter files to data/emails/.

(Optional) Create manual labels in labels/ for evaluation.

Run the extraction pipeline:

bash
python -m scripts.run_baml_test_suite
Check extracted outputs in evals/tool_outputs/.

🧪 Evaluation
Compare the extracted JSON outputs to your manual labels in labels/.

Use the provided scripts to measure field-level accuracy and assess extraction quality.

📝 Example Label Schema
json
{
  "source": "Axios PM",
  "date": "2024-04-24",
  "story_count": 4,
  "stories": [
    {
      "title": "1 big thing: Courts hammer Trump",
      "summary": "The Trump administration had an exceptionally bad day in court today, with a string of losses on multiple issues.",
      "url": "No url related",
      "category": "Politics"
    }
  ],
  "notes": "This newsletter focused on politics and finance news."
}
📊 Results & Reporting
Outputs are stored in evals/tool_outputs/.

Accuracy metrics and prompt optimization experiments are documented in project markdown files.

Use results for further NLP research or downstream analytics.

🤖 Technologies
Python 3.10+

OpenAI GPT-4o (via openai Python SDK)

python-dotenv for secure API key management

Standard libraries: email, json, re, etc.

📚 License
MIT License.
See LICENSE for details.

🙋‍♂️ Contributing
Pull requests and suggestions are welcome!
Open an issue to discuss improvements or new features.

⭐ Acknowledgments
OpenAI for LLM APIs

newspaper3k for traditional extraction (if used)

All contributors and testers
