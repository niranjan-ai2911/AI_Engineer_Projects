def classify_intent(user_input: str) -> str:
    text = user_input.lower()
    if "python" in text or "code" in text:
        return "coding"
    if "resume" in text or "job" in text or "interview" in text:
        return "career"
    if "rag" in text or "llm" in text or "ai" in text:
        return "genai"
    return "general"


def generate_response(user_input: str) -> str:
    intent = classify_intent(user_input)
    if intent == "coding":
        return "A strong AI engineer should focus on clean Python code, debugging, model evaluation, and practical system design."
    if intent == "career":
        return "For interviews, explain your projects clearly, show trade-offs, and connect technical decisions to business impact."
    if intent == "genai":
        return "GenAI systems combine prompting, retrieval, orchestration, and evaluation to build reliable end-to-end AI products."
    return "A good answer should be concise, clear, and grounded in real project experience and measurable outcomes."


def format_final_output(user_input: str) -> str:
    intent = classify_intent(user_input)
    answer = generate_response(user_input)
    return {
        "intent": intent,
        "user_input": user_input,
        "final_answer": answer,
    }


if __name__ == "__main__":
    sample_input = "How should I explain my AI projects in an interview?"
    output = format_final_output(sample_input)
    print("\n=== Prompt Pipeline Demo ===")
    print(f"Intent: {output['intent']}")
    print(f"Input: {output['user_input']}")
    print(f"Final answer: {output['final_answer']}")
