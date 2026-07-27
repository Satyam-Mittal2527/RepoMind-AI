from git import Repo
from pathlib import Path
import shutil


class GitHubLoader:

    def clone_repo(self, repo_url: str, destination: str = "repositories/repo"):

        destination = Path(destination)

        if destination.exists():
            shutil.rmtree(destination)

        Repo.clone_from(repo_url, destination)

        return str(destination)