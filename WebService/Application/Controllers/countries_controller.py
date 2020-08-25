from Application.DI import countries_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.countries_repository import CountriesRepository
from Application.Models.country import Country

countries_controller_api = Blueprint('countries_controller_api', __name__)

countries_api = Blueprint('countries_api', __name__)


@countries_controller_api.route("/api/Countries", methods=['GET'])
def get_countries():
    return jsonify(countries_db.get())


@countries_controller_api.route("/api/Countries/<int:id>", methods=['GET'])
def get_countries_id(id):
    return jsonify(countries_db.get_id(id))


@countries_controller_api.route("/api/Countries", methods=['POST'])
def post_country():
    obj = Country()
    req_data = request.get_json()
    try:
        obj.CountryName = req_data["CountryName"]
        obj.CountryCode = req_data["CountryCode"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CurrencyCode = req_data["CurrencyCode"]

    except BaseException:
        return "Invalid data"
    ls = [obj.CountryName, obj.CountryCode, obj.NatLangCode, obj.CurrencyCode]
    if not validation(ls): return "Invalid data"


    try:
        countries_db.add(obj)
    except BaseException:
        return "Bad Request!"

    return "OK"


@countries_controller_api.route("/api/Countries/<int:id>", methods=['DELETE'])
def delete_country(id):
    try:
        countries_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@countries_controller_api.route("/api/Countries/<int:id>", methods=['PUT'])
def put_country(id):
    obj = Country()
    req_data = request.get_json()
    try:
        obj.CountryName = req_data["CountryName"]
        obj.CountryCode = req_data["CountryCode"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CurrencyCode = req_data["CurrencyCode"]

    except BaseException:
        return "Invalid data"
    ls = [obj.CountryName, obj.CountryCode, obj.NatLangCode, obj.CurrencyCode]
    if not validation(ls): return "Invalid data"
    try:
        countries_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    