import json
import sqlite3
from application.app import employments_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.employments.schema import get_json_schema
from application.entities.employments.model import Employment
employments_controller_api = Blueprint('employments_controller_api', __name__)
employments_api = Blueprint('employments_api', __name__)
@employments_controller_api.route("/api/Employments", methods=['GET'])

def get_employments():
    obj = employments_db.get()
    return jsonify(obj), HTTPStatus.OK

@employments_controller_api.route("/api/Employments/<int:id>", methods=['GET'])
def get_employments_id(id):
    obj = employments_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@employments_controller_api.route("/api/Employments", methods=['POST'])
def post_employment():
    obj = Employment()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.PersonId = req_data["PersonId"]
        obj.HRJobId = req_data["HRJobId"]
        obj.ManagerEmployeeId = req_data["ManagerEmployeeId"]
        obj.StartDate = req_data["StartDate"]
        obj.EndDate = req_data["EndDate"]
        obj.Salary = req_data["Salary"]
        obj.CommissionPercent = req_data["CommissionPercent"]
        obj.Employmentcol = req_data["Employmentcol"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        employments_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@employments_controller_api.route("/api/Employments/<int:id>", methods=['DELETE'])
def delete_employment(id):
    try:
        employments_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@employments_controller_api.route("/api/Employments/<int:id>", methods=['PUT'])
def put_employment(id):
    obj = Employment()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.PersonId = req_data["PersonId"]
        obj.HRJobId = req_data["HRJobId"]
        obj.ManagerEmployeeId = req_data["ManagerEmployeeId"]
        obj.StartDate = req_data["StartDate"]
        obj.EndDate = req_data["EndDate"]
        obj.Salary = req_data["Salary"]
        obj.CommissionPercent = req_data["CommissionPercent"]
        obj.Employmentcol = req_data["Employmentcol"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        employments_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    