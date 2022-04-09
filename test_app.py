import json
from app import app


def test_get_all_countries():
    with app.test_client() as test_client:
        response = test_client.get("/countries")
        res = json.loads(response.data.decode("utf-8"))
        assert len(res) == 3
        assert res[0]["name"] == "United States of America"

def test_get_country_by_code():
    with app.test_client() as test_client:
        response = test_client.get("/country/USA")
        res = json.loads(response.data.decode("utf-8"))
        assert res["name"] == "United States of America"