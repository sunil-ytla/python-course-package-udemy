import pytest

@pytest.fixture(scope="session")
def project():
    print("setting up project fixture")
    yield
    print("tearing down project fixture")




def test_linting_passes(project):
    assert False


def test_tests_pass():
    ...


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