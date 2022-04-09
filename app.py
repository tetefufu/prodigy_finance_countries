from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse
import jsonify

app = Flask(__name__)
api = Api(app)


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


class CountriesResource(Resource):
    @marshal_with(country_dao_fields)
    def get(self):
        currency = request.args.get("currency", default=None, type=str)
        if currency == None:
            return COUNTRIES
        return [x for x in COUNTRIES if currency in x.currencies]


class CountryResource(Resource):
    @marshal_with(country_dao_fields)
    def get(self, code):
        countries = [
            x for x in COUNTRIES if x.alpha_2_code == code or x.alpha_3_code == code
        ]

        return countries[0]


api.add_resource(CountriesResource, "/countries")
api.add_resource(CountryResource, "/country/<string:code>")

if __name__ == "__main__":
    app.run(debug=True)
