import subprocess



def test_linting_passes(project_dir):
    subprocess.run(
        ["make", "lint-ci"],
        cwd=project_dir, # Change working directory to the project directory for this command
        check=True, # Ensure the command raises an error if linting fails
    )

def test_tests_pass(project_dir):
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


def test_install_suceeds():
    ...


"""
Setup:
1. Generate project using cookiecutter.
2. create virtual environment and install the project dependencies.

Tests:
3. Run linting checks.
4. Run tests.

cleanup/teardown:
5. Remove the virtual environment.
6. Remove the generated project directory
"""
