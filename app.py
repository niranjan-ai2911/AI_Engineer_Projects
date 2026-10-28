import os
from typing import TypedDict, List

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

load_dotenv()


class AgentState(TypedDict):
    question: str
    steps: List[str]
    answer: str


def plan_step(state: AgentState) -> AgentState:
    question = state["question"]
    steps = [
        "Understand the user request",
        f"Generate a helpful answer for: {question}",
        "Return the final response in a structured way",
    ]
    return {"question": question, "steps": steps, "answer": ""}


def answer_step(state: AgentState) -> AgentState:
    question = state["question"]
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        try:
            from langchain_openai import ChatOpenAI
            from langchain_core.messages import HumanMessage

            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
            response = llm.invoke([
                HumanMessage(content=f"Answer this question clearly and briefly: {question}")
            ])
            answer = response.content
        except Exception:
            answer = (
                "OpenAI is configured, but the request failed. "
                "The app is still working in fallback mode."
            )
    else:
        answer = (
            f"This is a LangGraph demo response. Your question was: '{question}'. "
            "Add an OPENAI_API_KEY to connect this graph to a real LLM."
        )

    return {
        "question": question,
        "steps": state["steps"],
        "answer": answer,
    }


workflow = StateGraph(AgentState)
workflow.add_node("plan", plan_step)
workflow.add_node("answer", answer_step)
workflow.add_edge(START, "plan")
workflow.add_edge("plan", "answer")
workflow.add_edge("answer", END)

app = workflow.compile()


if __name__ == "__main__":
    sample_question = "How can I use LangGraph to build a small AI workflow?"
    result = app.invoke({"question": sample_question, "steps": [], "answer": ""})
    print("\n=== LangGraph POC ===")
    print(f"Question: {result['question']}")
    print(f"Steps: {result['steps']}")
    print(f"Answer: {result['answer']}")
