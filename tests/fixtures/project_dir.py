import pytest
from pathlib import Path
from typing import Generator
import shutil
from tests.utils.project import generate_project

@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "cookiecutter-test",
    }
    generated_repo_dir: Path = generate_project(template_values)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)