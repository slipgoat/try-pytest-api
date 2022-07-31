import pytest

from core.clients.api.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    return ApiClient()
