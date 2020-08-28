import json
import sqlite3
from application.app import orders_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.valid.json_schemes import Schemes
from application.models.orders import Orders


orders_controller_api = Blueprint('orders_controller_api', __name__)
orders_api = Blueprint('orders_api', __name__)


@orders_controller_api.route("/api/Orders", methods=['GET'])
def get_orders():
    obj = orders_db.get()
    return jsonify(obj), HTTPStatus.OK
    
@orders_controller_api.route("/api/Orders/<int:id>", methods=['GET'])
def get_orders_id(id):
    obj = orders_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK
    
@orders_controller_api.route("/api/Orders", methods=['POST'])
def post_orders():
    obj = Orders()
    req_data = request.get_json()

    schema = Schemes.orders_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        obj.CustomerId = req_data["CustomerId"]
        obj.SalesRepId = req_data["SalesRepId"]
        obj.OrderDate = req_data["OrderDate"]
        obj.OrderCode = req_data["OrderCode"]
        obj.OrderStatus = req_data["OrderStatus"]
        obj.OrderTotal = req_data["OrderTotal"]
        obj.OrderCurrency = req_data["OrderCurrency"]
        obj.PromotionCode = req_data["PromotionCode"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        orders_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@orders_controller_api.route("/api/Orders/<int:id>", methods=['DELETE'])
def delete_orders(id):
    try:
        orders_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@orders_controller_api.route("/api/Orders/<int:id>", methods=['PUT'])
def put_orders(id):
    obj = Orders()
    req_data = request.get_json()

    schema = Schemes.orders_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        obj.CustomerId = req_data["CustomerId"]
        obj.SalesRepId = req_data["SalesRepId"]
        obj.OrderDate = req_data["OrderDate"]
        obj.OrderCode = req_data["OrderCode"]
        obj.OrderStatus = req_data["OrderStatus"]
        obj.OrderTotal = req_data["OrderTotal"]
        obj.OrderCurrency = req_data["OrderCurrency"]
        obj.PromotionCode = req_data["PromotionCode"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        orders_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    