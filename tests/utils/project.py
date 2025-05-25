
import json
import re
import subprocess
from pathlib import Path
from tempfile import template
from typing import Dict
from copy import deepcopy
import pytest
from typing import Generator
import shutil

from tests.consts import PROJECT_DIR


def generate_project(template_values: Dict[str, str]) -> Path:

    template_values = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}

    cookiecutter_config_file = PROJECT_DIR / "cookiecutter-test-config.json"
    cookiecutter_config_file.write_text(
        json.dumps(cookiecutter_config, indent=2)
    )

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
        PROJECT_DIR
        / "sample"
        / cookiecutter_config["default_context"]["repo_name"]
    )
    return generated_repo_dir