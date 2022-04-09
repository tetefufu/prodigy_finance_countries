import json
from main import app


def test_get_all_books():
    response = app.test_client().get("/")
    res = json.loads(response.data.decode("utf-8"))
    assert res["books"] == "it works"
