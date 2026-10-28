# AI Engineer Learning Portfolio

This repository contains small, recruiter-friendly AI/ML proof-of-concept projects designed for an AI engineer interview portfolio.

## Included projects

1. LangGraph workflow demo
   - A minimal agent-style workflow using LangGraph state transitions
   - Great for showing graph-based orchestration fundamentals

2. Mini RAG search demo
   - Uses TF-IDF and cosine similarity to retrieve the best match from a knowledge base
   - Demonstrates retrieval logic used in RAG systems

3. Prompt chaining exercise
   - Shows how a simple AI pipeline can classify an input, generate a structured answer, and format the final response

## Project structure

```text
.
├── app.py                              # LangGraph basic workflow
├── projects/
│   ├── 01_langgraph_basic/
│   │   └── app.py
│   ├── 02_rag_mini/
│   │   └── app.py
│   └── 03_prompt_pipeline/
│       └── app.py
├── README.md
├── requirements.txt
├── INTERVIEW_NOTES.md
└── .gitignore
```

## Setup

```bash
cd langgraph-poc
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run each project

```bash
python app.py
python projects/02_rag_mini/app.py
python projects/03_prompt_pipeline/app.py
```

## Why this helps for interviews

These examples show practical understanding of:
- workflow orchestration
- prompt design and chaining
- retrieval and similarity matching
- structured problem-solving for GenAI applications

They are intentionally simple, readable, and easy to explain in an interview.

