import json
from app import app


def test_get_all_books():
    with app.test_client() as test_client:
        response = test_client.get("/countries")
        res = json.loads(response.data.decode("utf-8"))
        assert len(res) == 3

def test_get_all_todos():
    with app.test_client() as test_client:
        response = test_client.get("/todos")
        res = json.loads(response.data.decode("utf-8"))
        assert len(res) == 2
        assert res[0]["task"] == "laundry"
