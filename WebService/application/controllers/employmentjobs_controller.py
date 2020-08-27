import json
import sqlite3
from application.app import employmentjobs_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.valid.json_schemes import Schemes
from application.models.employmentjobs import EmploymentJobs


employmentjobs_controller_api = Blueprint('employmentjobs_controller_api', __name__)
employmentjobs_api = Blueprint('employmentjobs_api', __name__)


@employmentjobs_controller_api.route("/api/EmploymentJobs", methods=['GET'])
def get_employmentjobs():
    obj = employmentjobs_db.get()
    return jsonify(obj), HTTPStatus.OK
    
@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['GET'])
def get_employmentjobs_id(id):
    obj = employmentjobs_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK
    
@employmentjobs_controller_api.route("/api/EmploymentJobs", methods=['POST'])
def post_employmentjobs():
    obj = EmploymentJobs()
    req_data = request.get_json()

    schema = Schemes.employmentjobs_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.NO_CONTENT

    try:
        obj.CountriesCountryId = req_data["CountriesCountryId"]
        obj.JobTitle = req_data["JobTitle"]
        obj.MinSalary = req_data["MinSalary"]
        obj.MaxSalary = req_data["MaxSalary"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.NO_CONTENT
    try:
        employmentjobs_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['DELETE'])
def delete_employmentjobs(id):
    try:
        employmentjobs_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['PUT'])
def put_employmentjobs(id):
    obj = EmploymentJobs()
    req_data = request.get_json()

    schema = Schemes.employmentjobs_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.NO_CONTENT

    try:
        obj.CountriesCountryId = req_data["CountriesCountryId"]
        obj.JobTitle = req_data["JobTitle"]
        obj.MinSalary = req_data["MinSalary"]
        obj.MaxSalary = req_data["MaxSalary"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.NO_CONTENT
    try:
        employmentjobs_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    