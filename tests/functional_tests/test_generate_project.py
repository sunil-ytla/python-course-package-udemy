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

from tests.utils.project import generate_project


def test_can_generate_project(project_dir: Path) -> None:
    """Test that the project can be generated successfully."""
    
    assert project_dir.exists(), (
        "Generated project directory does not exist."
    )
