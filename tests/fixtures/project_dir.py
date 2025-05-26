import subprocess
import pytest
from pathlib import Path
from typing import Generator
import shutil
from tests.utils.project import generate_project, initialize_git_repo

@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "cookiecutter-test",
    }
    generated_repo_dir: Path = generate_project(template_values)
    try:
        initialize_git_repo(repo_dir=generated_repo_dir)
        subprocess.run(
            ["make", "lint-ci"],
            cwd=generated_repo_dir,
            check=False,  # we want to fix all automatic fixes by this
        )
        yield generated_repo_dir
    finally:
        shutil.rmtree(generated_repo_dir)