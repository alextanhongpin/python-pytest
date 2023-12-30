import pytest


@pytest.fixture
def example_user():
    return {"name": "john", "age": 13}


# Prevent requests from making HTTP requests
# https://docs.pytest.org/en/latest/how-to/monkeypatch.html#global-patch-example-preventing-requests-from-remote-operations
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")
