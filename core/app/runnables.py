from langchain_core.runnables import RunnableLambda

def format_docs(docs):

    return "\n\n".join(
        f"""
File:
{doc.metadata['source']}

{doc.page_content}
"""
        for doc in docs
    )

formatter = RunnableLambda(format_docs)