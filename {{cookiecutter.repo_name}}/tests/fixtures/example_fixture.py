"""Example pytest fixture."""

import pytest
from uuid import uuid4

from tests.consts import PROJECT_DIR

@pytest.fixture(scope="session") 
def test_session_id() -> str:
    """Demonstrate how pytest fixtures are used."""
    return str(PROJECT_DIR) + str(uuid4())[:6]