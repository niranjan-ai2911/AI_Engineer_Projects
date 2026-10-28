# AI Projects Learning Repo

This repository contains a few small AI and GenAI experiments I built while learning and exploring practical workflows in LLMs, LangGraph, and retrieval-based systems.

## Included projects

1. LangGraph workflow demo
   - A basic multi-step workflow using LangGraph state transitions
   - Helps understand how tasks can be orchestrated in a structured way

2. Mini RAG search demo
   - Uses TF-IDF and cosine similarity to find the most relevant document from a knowledge base
   - Demonstrates the core idea behind retrieval-augmented generation

3. Prompt chaining exercise
   - A simple pipeline that classifies input intent, generates a response, and formats the output
   - Useful for learning prompt-based task decomposition

## Project structure

```text
.
├── app.py                              # LangGraph basic workflow
├── projects/
│   ├── 02_rag_mini/
│   │   └── app.py
│   └── 03_prompt_pipeline/
│       └── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── INTERVIEW_NOTES.md
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

## Notes

These are learning-focused experiments and small proof-of-concept projects created to practice core AI concepts, workflow design, and practical implementation patterns.

