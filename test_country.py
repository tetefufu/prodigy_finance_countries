from testing_utils import client_get, client_delete


def test_get_country_returns_correct_country_given_alpha_3_code():
    data, status_code = client_get("/country/USA")

    assert status_code == 200
    assert data["name"] == "United States of America"


def test_get_country_returns_correct_country_given_alpha_2_code():
    data, status_code = client_get("/country/US")

    assert status_code == 200
    assert data["name"] == "United States of America"


def test_get_country_by_alpha_2_code__then_returns_404_given_invalid_code():
    data, status_code = client_get("/country/INVALID")

    assert status_code == 404
    assert data["message"] == "country with code INVALID not found"


def test_delete_country_by_alpha_2_code_then_country_removed_from_list():
    data, status_code = client_delete("/country/US")

    assert status_code == 200

    data, status_code = client_get("/countries")

    assert status_code == 200
    assert len(data) == 3


def test_delete_country_by_alpha_3_code_then_country_removed_from_list():
    data, status_code = client_delete("/country/USA")

    assert status_code == 200

    data, status_code = client_get("/countries")

    assert status_code == 200
    assert len(data) == 3
