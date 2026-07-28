import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    """Provide an isolated TestClient with fresh in-memory activities per test."""
    snapshot = copy.deepcopy(app_module.activities)

    try:
        app_module.activities = snapshot
        yield TestClient(app_module.app)
    finally:
        app_module.activities = snapshot