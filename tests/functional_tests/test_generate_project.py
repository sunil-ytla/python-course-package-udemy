"""Test that the cookiecutter template is valid."""

from pathlib import Path


def test_can_generate_project(project_dir: Path) -> None:
    """Test that the project can be generated successfully."""
    assert project_dir.exists(), "Generated project directory does not exist."
