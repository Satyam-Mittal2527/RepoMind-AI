from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class TextSplitter:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )

    def split(self, documents: list[Document]) -> list[Document]:
        """
        Split LangChain Document objects into smaller chunks.
        """
        chunks = self.splitter.split_documents(documents)

        # Add chunk_id to metadata
        for index, chunk in enumerate(chunks):
            chunk.metadata["chunk_id"] = index

        return chunks