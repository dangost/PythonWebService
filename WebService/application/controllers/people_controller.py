import json
import sqlite3
from application.app import people_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.valid.json_schemes import Schemes
from application.models.person import Person


people_controller_api = Blueprint('people_controller_api', __name__)
people_api = Blueprint('people_api', __name__)


@people_controller_api.route("/api/People", methods=['GET'])
def get_people():
    obj = people_db.get()
    return jsonify(obj), HTTPStatus.OK
    
@people_controller_api.route("/api/People/<int:id>", methods=['GET'])
def get_people_id(id):
    obj = people_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK
    
@people_controller_api.route("/api/People", methods=['POST'])
def post_person():
    obj = Person()
    req_data = request.get_json()

    schema = Schemes.person_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        obj.FirstName = req_data["FirstName"]
        obj.LastName = req_data["LastName"]
        obj.MiddleName = req_data["MiddleName"]
        obj.Nickname = req_data["Nickname"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CultureCode = req_data["CultureCode"]
        obj.Gender = req_data["Gender"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        people_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@people_controller_api.route("/api/People/<int:id>", methods=['DELETE'])
def delete_person(id):
    try:
        people_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@people_controller_api.route("/api/People/<int:id>", methods=['PUT'])
def put_person(id):
    obj = Person()
    req_data = request.get_json()

    schema = Schemes.person_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        obj.FirstName = req_data["FirstName"]
        obj.LastName = req_data["LastName"]
        obj.MiddleName = req_data["MiddleName"]
        obj.Nickname = req_data["Nickname"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CultureCode = req_data["CultureCode"]
        obj.Gender = req_data["Gender"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        people_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    