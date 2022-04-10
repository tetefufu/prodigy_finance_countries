from testing_utils import test_client_get, test_client_delete


def test_get_all_countries_returns_countries():
    data, status_code = test_client_get("/countries")
    usa = data[0]

    assert status_code == 200
    assert len(data) == 4
    assert usa["name"] == "United States of America"
    assert usa["alpha_2_code"] == "US"
    assert usa["alpha_3_code"] == "USA"
    assert usa["currencies"][0] == "USD"


def test_get_country_returns_correct_countries_given_currency():
    data, status_code = test_client_get("/countries?currency=USD")
    usa = data[0]

    assert status_code == 200
    assert len(data) == 1
    assert usa["name"] == "United States of America"
    assert usa["alpha_2_code"] == "US"
    assert usa["alpha_3_code"] == "USA"
    assert usa["currencies"][0] == "USD"


def test_get_country_returns_correct_country_given_alpha_3_code():
    data, status_code = test_client_get("/country/USA")

    assert status_code == 200
    assert data["name"] == "United States of America"


def test_get_country_returns_correct_country_given_alpha_2_code():
    data, status_code = test_client_get("/country/US")

    assert status_code == 200
    assert data["name"] == "United States of America"


def test_get_country_by_alpha_2_code__then_returns_404_given_invalid_code():
    data, status_code = test_client_get("/country/INVALID")

    assert status_code == 404
    assert data["message"] == "country with code INVALID not found"


def test_delete_country_by_alpha_2_code_then_country_removed_from_list():
    data, status_code = test_client_delete("/country/US")

    assert status_code == 200

    data, status_code = test_client_get("/countries")

    assert status_code == 200
    assert len(data) == 3


def test_delete_country_by_alpha_3_code_then_country_removed_from_list():
    data, status_code = test_client_delete("/country/USA")

    assert status_code == 200

    data, status_code = test_client_get("/countries")

    assert status_code == 200
    assert len(data) == 3
