from core.app.ingestion.document_ingestion import DocumentIngestion
from  core.app.ingestion.text_splitter import TextSplitter
from core.app.ingestion.github_loader import GitHubLoader
from pathlib import Path
import shutil
from core.app.embeddings import embedding_model
from core.app.vector_store import VectorStore
from core.app.rag_chain import build_chain


REPOSITORY_PATH = "https://github.com/Satyam-Mittal2527/GenAI"
VECTOR_DB_PATH = "faiss_index"


def build_vector_store(repository_url: str):

    store = VectorStore()

    if Path(VECTOR_DB_PATH).exists():
        shutil.rmtree(VECTOR_DB_PATH)
        print("Loading existing FAISS index...")
        return store.load(
            VECTOR_DB_PATH,
            embedding_model,
        )

    print("Creating FAISS index...")

    loader = GitHubLoader()

    repo_path = loader.clone_repo(repository_url)

    document_loader = DocumentIngestion()

    documents = document_loader.ingest_directory(repo_path)

    splitter = TextSplitter()
    chunks = splitter.split(documents)

    vector_db = store.create(
        chunks,
        embedding_model,
    )

    store.save(VECTOR_DB_PATH)

    return vector_db


# def main():

#     vector_db = build_vector_store()

#     rag_chain = build_chain(vector_db)

#     print("=" * 60)
#     print("🤖 RepoMind AI")
#     print("Ask questions about the repository.")
#     print("Type 'exit' to quit.")
#     print("=" * 60)

#     while True:

#         question = input("\nYou: ")

#         if question.lower() in ["exit", "quit"]:
#             break

#         try:

#             answer = rag_chain.invoke(question)

#             print("\nRepoMind AI:\n")
#             print(answer)

#         except Exception as e:
#             print(e)


# if __name__ == "__main__":
#     main()