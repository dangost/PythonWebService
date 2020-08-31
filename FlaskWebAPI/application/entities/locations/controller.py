import json
import sqlite3
from application.app import locations_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.locations.schema import get_json_schema
from application.entities.locations.model import Location
locations_controller_api = Blueprint('locations_controller_api', __name__)
locations_api = Blueprint('locations_api', __name__)
@locations_controller_api.route("/api/Locations", methods=['GET'])

def get_locations():
    obj = locations_db.get()
    return jsonify(obj), HTTPStatus.OK

@locations_controller_api.route("/api/Locations/<int:id>", methods=['GET'])
def get_locations_id(id):
    obj = locations_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@locations_controller_api.route("/api/Locations", methods=['POST'])
def post_location():
    obj = Location()
    req_data = request.get_json()
    schema = Schemes.location_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CountryId = req_data["CountryId"]
        obj.AdressLine1 = req_data["AdressLine1"]
        obj.AdressLine2 = req_data["AdressLine2"]
        obj.City = req_data["City"]
        obj.State = req_data["State"]
        obj.District = req_data["District"]
        obj.PostalCode = req_data["PostalCode"]
        obj.LocationTypeCode = req_data["LocationTypeCode"]
        obj.Description = req_data["Description"]
        obj.ShippingNotes = req_data["ShippingNotes"]
        obj.CountriesCountryId = req_data["CountriesCountryId"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        locations_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@locations_controller_api.route("/api/Locations/<int:id>", methods=['DELETE'])
def delete_location(id):
    try:
        locations_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@locations_controller_api.route("/api/Locations/<int:id>", methods=['PUT'])
def put_location(id):
    obj = Location()
    req_data = request.get_json()
    schema = Schemes.location_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CountryId = req_data["CountryId"]
        obj.AdressLine1 = req_data["AdressLine1"]
        obj.AdressLine2 = req_data["AdressLine2"]
        obj.City = req_data["City"]
        obj.State = req_data["State"]
        obj.District = req_data["District"]
        obj.PostalCode = req_data["PostalCode"]
        obj.LocationTypeCode = req_data["LocationTypeCode"]
        obj.Description = req_data["Description"]
        obj.ShippingNotes = req_data["ShippingNotes"]
        obj.CountriesCountryId = req_data["CountriesCountryId"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        locations_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    