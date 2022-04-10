import json
from app import app


def test_get_all_countries():
    with app.test_client() as test_client:
        response = test_client.get("/countries")
        response_data = json.loads(response.data.decode("utf-8"))
        usa = response_data[0]

        assert len(response_data) == 4
        assert usa["name"] == "United States of America"
        assert usa["alpha_2_code"] == "US"
        assert usa["alpha_3_code"] == "USA"
        assert usa["currencies"][0] == "USD"


def test_get_country_given_currency():
    with app.test_client() as test_client:
        response = test_client.get("/countries?currency=USD")
        response_data = json.loads(response.data.decode("utf-8"))
        usa = response_data[0]

        assert len(response_data) == 1
        assert usa["name"] == "United States of America"
        assert usa["alpha_2_code"] == "US"
        assert usa["alpha_3_code"] == "USA"
        assert usa["currencies"][0] == "USD"


def test_get_country_by_alpha_3_code():
    with app.test_client() as test_client:
        response = test_client.get("/country/USA")
        response_data = json.loads(response.data.decode("utf-8"))

        assert response_data["name"] == "United States of America"


def test_get_country_by_alpha_2_code():
    with app.test_client() as test_client:
        response = test_client.get("/country/US")
        response_data = json.loads(response.data.decode("utf-8"))

        assert response_data["name"] == "United States of America"


def test_get_country_by_alpha_2_code_returns_404_given_invalid_code():
    with app.test_client() as test_client:
        response = test_client.get("/country/INVALID")

        response_data = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 404
        assert response_data["message"] == "country with code INVALID not found"


def test_delete_country_by_alpha_2_code():
    with app.test_client() as test_client:
        test_client.delete("/country/US")

        response = test_client.get("/countries")
        response_data = json.loads(response.data.decode("utf-8"))

        assert len(response_data) == 3


def test_delete_country_by_alpha_3_code():
    with app.test_client() as test_client:
        test_client.delete("/country/USA")

        response = test_client.get("/countries")
        response_data = json.loads(response.data.decode("utf-8"))

        assert len(response_data) == 3
