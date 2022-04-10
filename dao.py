from flask_restful import fields


country_dao_fields = {
    "name": fields.String,
    "alpha_2_code": fields.String,
    "alpha_3_code": fields.String,
    "currencies": fields.Raw,
}


class CountryDao:
    def __init__(
        self, name: str, alpha_2_code: str, alpha_3_code: str, currencies: list
    ):
        self.name = name
        self.alpha_2_code = alpha_2_code
        self.alpha_3_code = alpha_3_code
        self.currencies = currencies
        self.active = True


COUNTRIES = [
    CountryDao("United States of America", "US", "USA", ["USD"]),
    CountryDao("United Kingdom", "GB", "GBR", ["GBP"]),
    CountryDao("Ukraine", "UA", "UKR", ["UAH"]),
    CountryDao("Brunei", "BN", "BRN", ["BND", "SGD"]),
]
