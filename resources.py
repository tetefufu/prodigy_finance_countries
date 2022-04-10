from flask import request
from flask_restful import Resource, marshal_with
from dao import country_dao_fields, COUNTRIES


class CountriesResource(Resource):
    @marshal_with(country_dao_fields)
    def get(self):
        currency = request.args.get("currency", default=None, type=str)
        if currency == None:
            return [x for x in COUNTRIES if x.active]
        return [x for x in COUNTRIES if currency in x.currencies and x.active]


class CountryResource(Resource):
    @marshal_with(country_dao_fields)
    def get(self, code):
        countries = [
            x for x in COUNTRIES if x.alpha_2_code == code or x.alpha_3_code == code
        ]

        return countries[0]

    def delete(self, code):
        countries = [
            x for x in COUNTRIES if x.alpha_2_code == code or x.alpha_3_code == code
        ]

        for country in countries:
            country.active = False
