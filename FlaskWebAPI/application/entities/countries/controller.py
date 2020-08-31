import json
import sqlite3
from application.app import countries_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.countries.schema import get_json_schema
from application.entities.countries.model import Country
countries_controller_api = Blueprint('countries_controller_api', __name__)
countries_api = Blueprint('countries_api', __name__)

@countries_controller_api.route("/api/Countries", methods=['GET'])

def get_countries():
    obj = countries_db.get()
    return jsonify(obj), HTTPStatus.OK

@countries_controller_api.route("/api/Countries/<int:id>", methods=['GET'])
def get_countries_id(id):
    obj = countries_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@countries_controller_api.route("/api/Countries", methods=['POST'])
def post_country():
    obj = Country()
    req_data = request.get_json()
    schema = get_json_schema()
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CountryName = req_data["CountryName"]
        obj.CountryCode = req_data["CountryCode"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CurrencyCode = req_data["CurrencyCode"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        countries_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@countries_controller_api.route("/api/Countries/<int:id>", methods=['DELETE'])
def delete_country(id):
    try:
        countries_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@countries_controller_api.route("/api/Countries/<int:id>", methods=['PUT'])
def put_country(id):
    obj = Country()
    req_data = request.get_json()
    schema = get_json_schema()
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CountryName = req_data["CountryName"]
        obj.CountryCode = req_data["CountryCode"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CurrencyCode = req_data["CurrencyCode"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        countries_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    