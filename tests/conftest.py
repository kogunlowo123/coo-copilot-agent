"""Test configuration for COO Copilot Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "coo-copilot-agent", "category": "Executive"}
