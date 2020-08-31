import json
import sqlite3
from application.app import customers_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.customers.schema import get_json_schema
from application.entities.customers.model import Customer
customers_controller_api = Blueprint('customers_controller_api', __name__)
customers_api = Blueprint('customers_api', __name__)
@customers_controller_api.route("/api/Customers", methods=['GET'])

def get_customers():
    obj = customers_db.get()
    return jsonify(obj), HTTPStatus.OK

@customers_controller_api.route("/api/Customers/<int:id>", methods=['GET'])
def get_customers_id(id):
    obj = customers_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@customers_controller_api.route("/api/Customers", methods=['POST'])
def post_customer():
    obj = Customer()
    req_data = request.get_json()
    schema = Schemes.customer_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.PersonId = req_data["PersonId"]
        obj.CustomEmployeeId = req_data["CustomEmployeeId"]
        obj.AccountMgrId = req_data["AccountMgrId"]
        obj.IncomeLevel = req_data["IncomeLevel"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        customers_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@customers_controller_api.route("/api/Customers/<int:id>", methods=['DELETE'])
def delete_customer(id):
    try:
        customers_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@customers_controller_api.route("/api/Customers/<int:id>", methods=['PUT'])
def put_customer(id):
    obj = Customer()
    req_data = request.get_json()
    schema = Schemes.customer_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.PersonId = req_data["PersonId"]
        obj.CustomEmployeeId = req_data["CustomEmployeeId"]
        obj.AccountMgrId = req_data["AccountMgrId"]
        obj.IncomeLevel = req_data["IncomeLevel"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        customers_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    