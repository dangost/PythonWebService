import json
import sqlite3
from application.app import restrictedinfo_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.restrictedinfo.schema import get_json_schema
from application.entities.restrictedinfo.model import RestrictedInfo
restrictedinfo_controller_api = Blueprint('restrictedinfo_controller_api', __name__)
restrictedinfo_api = Blueprint('restrictedinfo_api', __name__)
@restrictedinfo_controller_api.route("/api/RestrictedInfo", methods=['GET'])

def get_restrictedinfo():
    obj = restrictedinfo_db.get()
    return jsonify(obj), HTTPStatus.OK

@restrictedinfo_controller_api.route("/api/RestrictedInfo/<int:id>", methods=['GET'])
def get_restrictedinfo_id(id):
    obj = restrictedinfo_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@restrictedinfo_controller_api.route("/api/RestrictedInfo", methods=['POST'])
def post_restrictedinfo():
    obj = RestrictedInfo()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.DateOfBirth = req_data["DateOfBirth"]
        obj.DateOfDeath = req_data["DateOfDeath"]
        obj.GovernmentId = req_data["GovernmentId"]
        obj.PassportId = req_data["PassportId"]
        obj.HireDire = req_data["HireDire"]
        obj.SeniorityCode = req_data["SeniorityCode"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        restrictedinfo_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@restrictedinfo_controller_api.route("/api/RestrictedInfo/<int:id>", methods=['DELETE'])
def delete_restrictedinfo(id):
    try:
        restrictedinfo_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@restrictedinfo_controller_api.route("/api/RestrictedInfo/<int:id>", methods=['PUT'])
def put_restrictedinfo(id):
    obj = RestrictedInfo()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.DateOfBirth = req_data["DateOfBirth"]
        obj.DateOfDeath = req_data["DateOfDeath"]
        obj.GovernmentId = req_data["GovernmentId"]
        obj.PassportId = req_data["PassportId"]
        obj.HireDire = req_data["HireDire"]
        obj.SeniorityCode = req_data["SeniorityCode"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        restrictedinfo_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    