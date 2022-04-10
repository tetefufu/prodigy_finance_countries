from flask import Flask
from flask_restful import Api
from resources import CountriesResource, CountryResource

app = Flask(__name__)
api = Api(app)


api.add_resource(CountriesResource, "/countries")
api.add_resource(CountryResource, "/country/<string:code>")


if __name__ == "__main__":
    app.run(debug=True)
