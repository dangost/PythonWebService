import json
import sqlite3
from application.app import phonenumbers_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.phonenumbers.schema import get_json_schema
from application.entities.phonenumbers.model import PhoneNumber
phonenumbers_controller_api = Blueprint('phonenumbers_controller_api', __name__)
phonenumbers_api = Blueprint('phonenumbers_api', __name__)
@phonenumbers_controller_api.route("/api/PhoneNumbers", methods=['GET'])

def get_phonenumbers():
    obj = phonenumbers_db.get()
    return jsonify(obj), HTTPStatus.OK

@phonenumbers_controller_api.route("/api/PhoneNumbers/<int:id>", methods=['GET'])
def get_phonenumbers_id(id):
    obj = phonenumbers_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@phonenumbers_controller_api.route("/api/PhoneNumbers", methods=['POST'])
def post_phonenumber():
    obj = PhoneNumber()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.PeoplePersonId = req_data["PeoplePersonId"]
        obj.LocationLocationId = req_data["LocationLocationId"]
        obj.Phonenumber = req_data["Phonenumber"]
        obj.CountryCode = req_data["CountryCode"]
        obj.PhoneType = req_data["PhoneType"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        phonenumbers_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@phonenumbers_controller_api.route("/api/PhoneNumbers/<int:id>", methods=['DELETE'])
def delete_phonenumber(id):
    try:
        phonenumbers_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@phonenumbers_controller_api.route("/api/PhoneNumbers/<int:id>", methods=['PUT'])
def put_phonenumber(id):
    obj = PhoneNumber()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.PeoplePersonId = req_data["PeoplePersonId"]
        obj.LocationLocationId = req_data["LocationLocationId"]
        obj.Phonenumber = req_data["Phonenumber"]
        obj.CountryCode = req_data["CountryCode"]
        obj.PhoneType = req_data["PhoneType"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        phonenumbers_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    