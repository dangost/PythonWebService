from flask import Blueprint, request
from flask import json
from Application.Repositories.countries_repository import CountriesRepository
from Application.Models.country import Country

countries_controller_api = Blueprint('countries_controller_api', __name__)


class CountriesController:
    countries_api = Blueprint('countries_api', __name__)
    db = CountriesRepository()

    @staticmethod
    @countries_controller_api.route("/api/Countries", methods=['GET'])
    def get_countries():
        return CountriesController.db.get()

    @staticmethod
    @countries_controller_api.route("/api/Countries/<int:id>", methods=['GET'])
    def get_countries_id(id):
        return CountriesController.db.get_id(id)

    @staticmethod
    @countries_controller_api.route("/api/Countries", methods=['POST'])
    def post_country():
        country = Country()
        req_data = request.get_json()
        country.CountryName = req_data["CountryName"]
        country.CountryCode = req_data["CountryCode"]
        country.NatLangCode = req_data["NatLangCode"]
        country.CurrencyCode = req_data["CurrencyCode"]
        try:
            CountriesController.db.add(country)

        except BaseException:
            return "Bad Request!"
        return "OK"

    @staticmethod
    @countries_controller_api.route("/api/Countries/<int:id>", methods=['DELETE'])
    def delete_country(id):
        try:
            CountriesController.db.delete(id)

        except BaseException:
            return "Bad Request!"
        return "OK"

    @staticmethod
    @countries_controller_api.route("/api/Countries/<int:id>", methods=['PUT'])
    def put_country(id):
        country = Country()
        req_data = request.get_json()
        country.CountryName = req_data["CountryName"]
        country.CountryCode = req_data["CountryCode"]
        country.NatLangCode = req_data["NatLangCode"]
        country.CurrencyCode = req_data["CurrencyCode"]
        try:
            CountriesController.db.edit(id, country)

        except BaseException:
            return "Bad Request!"
        return "OK"







