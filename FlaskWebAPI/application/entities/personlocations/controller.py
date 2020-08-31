import json
import sqlite3
from application.app import personlocations_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.personlocations.schema import get_json_schema
from application.entities.personlocations.model import PersonLocation
personlocations_controller_api = Blueprint('personlocations_controller_api', __name__)
personlocations_api = Blueprint('personlocations_api', __name__)
@personlocations_controller_api.route("/api/PersonLocations", methods=['GET'])

def get_personlocations():
    obj = personlocations_db.get()
    return jsonify(obj), HTTPStatus.OK

@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['GET'])
def get_personlocations_id(id):
    obj = personlocations_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@personlocations_controller_api.route("/api/PersonLocations", methods=['POST'])
def post_personlocation():
    obj = PersonLocation()
    req_data = request.get_json()
    schema = Schemes.personlocation_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.LocationsLocationsId = req_data["LocationsLocationsId"]
        obj.SubAdress = req_data["SubAdress"]
        obj.LocationUsage = req_data["LocationUsage"]
        obj.Notes = req_data["Notes"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        personlocations_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['DELETE'])
def delete_personlocation(id):
    try:
        personlocations_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['PUT'])
def put_personlocation(id):
    obj = PersonLocation()
    req_data = request.get_json()
    schema = Schemes.personlocation_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.LocationsLocationsId = req_data["LocationsLocationsId"]
        obj.SubAdress = req_data["SubAdress"]
        obj.LocationUsage = req_data["LocationUsage"]
        obj.Notes = req_data["Notes"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        personlocations_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    