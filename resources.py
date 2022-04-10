from flask import request, abort
from flask_restful import Resource, marshal_with
from dao import country_dao_fields, COUNTRIES


class CountriesResource(Resource):
    @marshal_with(country_dao_fields)
    def get(self):
        currency = request.args.get("currency", default=None, type=str)

        countries = [x for x in COUNTRIES if x.active]
        if currency != None:
            countries = [x for x in countries if currency in x.currencies]

        return countries


class CountryResource(Resource):
    @marshal_with(country_dao_fields)
    def get(self, code):
        countries = [
            x for x in COUNTRIES if x.alpha_2_code == code or x.alpha_3_code == code
        ]

        if countries:
            return countries[0]
        else:
            abort(404, f"country with code {code} not found")

    def delete(self, code):
        countries = [
            x for x in COUNTRIES if x.alpha_2_code == code or x.alpha_3_code == code
        ]

        for country in countries:
            country.active = False
