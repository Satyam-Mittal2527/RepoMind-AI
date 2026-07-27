from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self):
        self.vector_store = None

    def create(self, chunks, embedding_model):
        """
        Creates a FAISS vector store from documents.
        """

        self.vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=embedding_model,
        )

        return self.vector_store

    def save(self, path: str):
        """
        Saves the vector store locally.
        """

        if self.vector_store is None:
            raise ValueError("Vector store has not been created.")

        self.vector_store.save_local(path)

    def load(self, path: str, embedding_model):
        """
        Loads a saved vector store.
        """

        self.vector_store = FAISS.load_local(
            folder_path=path,
            embeddings=embedding_model,
            allow_dangerous_deserialization=True,
        )

        return self.vector_store

    def as_retriever(self, k: int = 4):
        """
        Returns a retriever.
        """

        return self.vector_store.as_retriever(
            search_kwargs={"k": k}
        )