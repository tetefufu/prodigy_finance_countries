from testing_utils import client_get, client_delete


def test_get_countries_returns_all_countries():
    data, status_code = client_get("/countries")
    usa = data[0]

    assert status_code == 200
    assert len(data) == 4
    assert usa["name"] == "United States of America"
    assert usa["alpha_2_code"] == "US"
    assert usa["alpha_3_code"] == "USA"
    assert usa["currencies"][0] == "USD"


def test_get_countries_returns_correct_countries_given_currency():
    data, status_code = client_get("/countries?currency=USD")
    usa = data[0]

    assert status_code == 200
    assert len(data) == 1
    assert usa["name"] == "United States of America"
    assert usa["alpha_2_code"] == "US"
    assert usa["alpha_3_code"] == "USA"
    assert usa["currencies"][0] == "USD"
