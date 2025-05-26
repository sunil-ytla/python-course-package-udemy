"""Test that generated makefile works."""

import subprocess


def test_linting_passes(project_dir):
    """Validate that the templatized project has no auto-fixable linting issues."""
    subprocess.run(
        ["make", "lint-ci"],
        cwd=project_dir,  # Change working directory to the project directory for this command
        check=True,  # Ensure the command raises an error if linting fails
    )


def test_tests_pass(project_dir):
    """Validate the the templatized tests pass when executed against a templatized project."""
    subprocess.run(
        ["make", "install"],
        cwd=project_dir,
        check=True,
    )
    subprocess.run(
        ["make", "test-wheel-locally"],
        cwd=project_dir,
        check=True,
    )
