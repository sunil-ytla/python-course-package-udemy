import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(
    scope="session"
)  # we want to generate the project only once per session
def project_dir() -> Generator[Path, None, None]:
    test_session_id: str = generate_test_session_id()
    template_values = {
        "repo_name": f"cookiecutter-test-{test_session_id}",
    }
    generated_repo_dir: Path = generate_project(template_values, test_session_id)
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


def generate_test_session_id() -> str:
    """Generate a random UUID."""
    return str(uuid4())[:6]
