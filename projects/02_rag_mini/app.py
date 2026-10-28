from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


KNOWLEDGE_BASE = [
    {
        "title": "Python for AI",
        "content": "Python is widely used in AI because it has a simple syntax, strong libraries, and broad community support for ML, NLP, and data pipelines.",
    },
    {
        "title": "LLM Basics",
        "content": "Large language models are trained on massive text corpora and can generate, summarize, and reason over language using transformer-based architectures.",
    },
    {
        "title": "RAG Systems",
        "content": "Retrieval augmented generation combines a vector search or keyword retriever with an LLM to ground responses in external knowledge before generating a final answer.",
    },
    {
        "title": "Prompt Engineering",
        "content": "Prompt engineering is the practice of designing input instructions so a language model follows the required format, tone, and task behavior.",
    },
    {
        "title": "Model Evaluation",
        "content": "Model evaluation uses metrics such as accuracy, precision, recall, latency, and cost to compare systems and track quality across experiments.",
    },
]


def answer_question(question: str):
    docs = [item["content"] for item in KNOWLEDGE_BASE]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs + [question])
    similarities = cosine_similarity(matrix[-1], matrix[:-1])[0]
    best_idx = similarities.argmax()
    best_match = KNOWLEDGE_BASE[best_idx]

    return {
        "question": question,
        "best_match": best_match["title"],
        "score": round(float(similarities[best_idx]), 4),
        "answer": best_match["content"],
    }


if __name__ == "__main__":
    sample_question = "How does RAG improve LLM answers with retrieved knowledge?"
    result = answer_question(sample_question)
    print("\n=== Mini RAG Demo ===")
    print(f"Question: {result['question']}")
    print(f"Best match: {result['best_match']}")
    print(f"Similarity score: {result['score']}")
    print(f"Answer: {result['answer']}")
