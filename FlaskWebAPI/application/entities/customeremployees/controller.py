import json
import sqlite3
from application.app import customeremployees_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.customeremployees.schema import get_json_schema
from application.entities.customeremployees.model import CustomerEmployee
customeremployees_controller_api = Blueprint('customeremployees_controller_api', __name__)
customeremployees_api = Blueprint('customeremployees_api', __name__)
@customeremployees_controller_api.route("/api/CustomerEmployees", methods=['GET'])

def get_customeremployees():
    obj = customeremployees_db.get()
    return jsonify(obj), HTTPStatus.OK

@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['GET'])
def get_customeremployees_id(id):
    obj = customeremployees_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@customeremployees_controller_api.route("/api/CustomerEmployees", methods=['POST'])
def post_customeremployee():
    obj = CustomerEmployee()
    req_data = request.get_json()
    schema = Schemes.customeremployee_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CompanyId = req_data["CompanyId"]
        obj.BadgeNumber = req_data["BadgeNumber"]
        obj.JobTitle = req_data["JobTitle"]
        obj.Department = req_data["Department"]
        obj.CreditLimit = req_data["CreditLimit"]
        obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        customeremployees_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['DELETE'])
def delete_customeremployee(id):
    try:
        customeremployees_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['PUT'])
def put_customeremployee(id):
    obj = CustomerEmployee()
    req_data = request.get_json()
    schema = Schemes.customeremployee_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CompanyId = req_data["CompanyId"]
        obj.BadgeNumber = req_data["BadgeNumber"]
        obj.JobTitle = req_data["JobTitle"]
        obj.Department = req_data["Department"]
        obj.CreditLimit = req_data["CreditLimit"]
        obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        customeremployees_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    