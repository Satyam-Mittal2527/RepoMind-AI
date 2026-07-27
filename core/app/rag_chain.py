from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from core.app.llm import llm
from core.app.prompt import RAG_PROMPT
from core.app.runnables import formatter


def build_chain(vector_store):

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":8,
            "fetch_k":20
        }
    )

    chain = (
        {
            "context": retriever | formatter,
            "question": RunnablePassthrough(),
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain