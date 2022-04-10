import json
from app import app


def test_client_get(url: str):
    with app.test_client() as test_client:
        response = test_client.get(url)
        response_data = json.loads(response.data.decode("utf-8"))
        return response_data, response.status_code


def test_client_delete(url: str):
    with app.test_client() as test_client:
        response = test_client.delete(url)
        response_data = json.loads(response.data.decode("utf-8"))
        return response_data, response.status_code
