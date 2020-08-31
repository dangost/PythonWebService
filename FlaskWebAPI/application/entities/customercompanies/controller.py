import json
import sqlite3
from application.app import customercompanies_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.customercompanies.schema import get_json_schema
from application.entities.customercompanies.model import CustomerCompany
customercompanies_controller_api = Blueprint('customercompanies_controller_api', __name__)
customercompanies_api = Blueprint('customercompanies_api', __name__)
@customercompanies_controller_api.route("/api/CustomerCompanies", methods=['GET'])

def get_customercompanies():
    obj = customercompanies_db.get()
    return jsonify(obj), HTTPStatus.OK

@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['GET'])
def get_customercompanies_id(id):
    obj = customercompanies_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@customercompanies_controller_api.route("/api/CustomerCompanies", methods=['POST'])
def post_customercompany():
    obj = CustomerCompany()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CompanyName = req_data["CompanyName"]
        obj.CompanyCreditLimit = req_data["CompanyCreditLimit"]
        obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        customercompanies_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['DELETE'])
def delete_customercompany(id):
    try:
        customercompanies_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['PUT'])
def put_customercompany(id):
    obj = CustomerCompany()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.CompanyName = req_data["CompanyName"]
        obj.CompanyCreditLimit = req_data["CompanyCreditLimit"]
        obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        customercompanies_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    