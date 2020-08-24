from flask import Blueprint, request
from Application.Repositories.countries_repository import CountriesRepository
from Application.Models.country import Country

countries_controller_api = Blueprint('countries_controller_api', __name__)

countries_api = Blueprint('countries_api', __name__)
db = CountriesRepository()


@countries_controller_api.route("/api/Countries", methods=['GET'])
def get_countries():
    return db.get()


@countries_controller_api.route("/api/Countries/<int:id>", methods=['GET'])
def get_countries_id(id):
    return db.get_id(id)


@countries_controller_api.route("/api/Countries", methods=['POST'])
def post_country():
    obj = Country()
    req_data = request.get_json()
    obj.CountryName = req_data["CountryName"]
    obj.CountryCode = req_data["CountryCode"]
    obj.NatLangCode = req_data["NatLangCode"]
    obj.CurrencyCode = req_data["CurrencyCode"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@countries_controller_api.route("/api/Countries/<int:id>", methods=['DELETE'])
def delete_country(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@countries_controller_api.route("/api/Countries/<int:id>", methods=['PUT'])
def put_country(id):
    obj = Country()
    req_data = request.get_json()
    obj.CountryName = req_data["CountryName"]
    obj.CountryCode = req_data["CountryCode"]
    obj.NatLangCode = req_data["NatLangCode"]
    obj.CurrencyCode = req_data["CurrencyCode"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    