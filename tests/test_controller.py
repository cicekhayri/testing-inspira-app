import pytest
from inspira.testclient import TestClient

from main import app


client = TestClient(app)


@pytest.mark.asyncio
async def test_index_returns_valid_json_response():
    response = await client.get("/greetings")
    expected = {"variable": "value"}

    assert response.json() == expected


@pytest.mark.asyncio
async def test_index_returns_200_status_code():
    response = await client.get("/greetings")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_nonexistent_endpoint_returns_404():
    response = await client.get("/nonexistent")

    assert response.status_code == 404