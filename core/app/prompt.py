from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
"""
You are RepoMind AI.

Answer only from the repository context.

Context:
{context}

Question:
{question}
"""
)