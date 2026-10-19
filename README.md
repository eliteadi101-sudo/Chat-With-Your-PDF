# Chat With Your PDF

Upload a PDF and search its extracted text with a simple keyword-based answer finder (no paid AI API required).

## Tech stack
Python, Streamlit, pypdf

## Features
- A working core implementation with a simple, usable interface or CLI.
- Input validation and basic error handling where appropriate.
- Source code organized for learning and extension.

## Getting started

Choose the instructions for this project's stack.

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   ```
3. Install dependencies and run:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Project structure

The source files are kept in the root directory or in `public/`, `templates/`, or the conventional language-specific folders. Generated local databases, secrets, and dependency folders are excluded with `.gitignore` where applicable.

## Notes
- These are intermediate-level starter repositories intended for learning and customization. Review, test, and personalize them before presenting them as your own work.
- Never commit API keys, passwords, tokens, or private user data.
- Some projects use external APIs and therefore require an internet connection.
