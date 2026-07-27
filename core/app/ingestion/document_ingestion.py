from pathlib import Path
from langchain_core.documents import Document

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".go",
    ".rs",
    ".html",
    ".css",
    ".json",
    ".yaml",
    ".yml",
    ".md",
    ".txt",
}

IGNORE_FILES = {
    "requirements.txt",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "poetry.lock",
    ".gitignore",
    ".env",
}

IGNORE_DIRS = {
    ".git",
    ".github",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    ".idea",
    ".vscode",
    "dist",
    "build",
    ".next",
    ".turbo",
    "coverage",
    ".pytest_cache",
    "faiss_index",
}


class DocumentIngestion:

    def __init__(self):
        self.documents = []

    def ingest_directory(self, directory: str):

        self.documents = []

        root = Path(directory)

        if not root.exists():
            raise FileNotFoundError(f"Directory not found: {root}")

        files = []

        for file in root.rglob("*"):

            # Skip ignored directories
            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            # Skip ignored files
            if file.name in IGNORE_FILES:
                continue

            # Skip unsupported files
            if not file.is_file():
                continue

            if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            files.append(file)

        # Prioritize README
        files.sort(
            key=lambda f: (
                f.name.lower() != "readme.md",
                str(f)
            )
        )

        for file in files:

            try:
                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                if not text.strip():
                    continue

                self.documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": str(file.relative_to(root)),
                            "filename": file.name,
                            "extension": file.suffix,
                        },
                    )
                )

            except Exception as e:
                print(f"Failed to read {file}: {e}")

        print(f"Ingested {len(self.documents)} documents.")

        return self.documents