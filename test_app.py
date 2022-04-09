import json
from app import app


def test_get_all_countries():
    with app.test_client() as test_client:
        response = test_client.get("/countries")
        res = json.loads(response.data.decode("utf-8"))
        assert len(res) == 3
        usa = res[0]
        assert usa["name"] == "United States of America"
        assert usa["alpha_2_code"] == "US"
        assert usa["alpha_3_code"] == "USA"
        assert usa["currencies"][0] == "USD"


def test_get_country_by_alpha_3_code():
    with app.test_client() as test_client:
        response = test_client.get("/country/USA")
        res = json.loads(response.data.decode("utf-8"))
        assert res["name"] == "United States of America"


def test_get_country_by_alpha_2_code():
    with app.test_client() as test_client:
        response = test_client.get("/country/US")
        res = json.loads(response.data.decode("utf-8"))
        assert res["name"] == "United States of America"
