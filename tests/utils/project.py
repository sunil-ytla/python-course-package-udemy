"""Functions for creating a cookiecut project to be used in tests."""

import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import (
    Dict,
)

from tests.consts import PROJECT_DIR


def initialize_git_repo(repo_dir: Path) -> None:
    """Run git commands to make a directory into a valid git repository."""
    # git init
    subprocess.run(
        ["git", "init", str(repo_dir)],
        check=True,
        cwd=repo_dir,
    )

    # commit the contents to main branch
    subprocess.run(
        ["git", "branch", "-M", "main"],
        check=True,
        cwd=repo_dir,
    )
    subprocess.run(
        ["git", "add", "--all"],
        check=True,
        cwd=repo_dir,
    )
    subprocess.run(
        ["git", "commit", "-m", "feat: Initial commit by pytest"],
        check=True,
        cwd=repo_dir,
    )


def generate_project(template_values: Dict[str, str], test_session_id: str) -> Path:
    """
    Generate a boilerplate project that we can use to test the template.

    :param template_values: jinja context used when populating template
    :param test_session_id: potentially randomly generated string used to
        ensure uniqueness of generated file names.

    """
    template_values = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}

    cookiecutter_config_file = PROJECT_DIR / f"cookiecutter-{test_session_id}.json"
    cookiecutter_config_file.write_text(json.dumps(cookiecutter_config, indent=2))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_file),
    ]
    print(f"Running command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    generated_repo_dir = (
        PROJECT_DIR / "sample" / cookiecutter_config["default_context"]["repo_name"]
    )
    return generated_repo_dir
