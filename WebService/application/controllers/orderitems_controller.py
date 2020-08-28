import json
import sqlite3
from application.app import orderitems_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.valid.json_schemes import Schemes
from application.models.orderitem import OrderItem


orderitems_controller_api = Blueprint('orderitems_controller_api', __name__)
orderitems_api = Blueprint('orderitems_api', __name__)


@orderitems_controller_api.route("/api/OrderItems", methods=['GET'])
def get_orderitems():
    obj = orderitems_db.get()
    return jsonify(obj), HTTPStatus.OK
    
@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['GET'])
def get_orderitems_id(id):
    obj = orderitems_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK
    
@orderitems_controller_api.route("/api/OrderItems", methods=['POST'])
def post_orderitem():
    obj = OrderItem()
    req_data = request.get_json()

    schema = Schemes.orderitem_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        obj.OrderId = req_data["OrderId"]
        obj.ProductId = req_data["ProductId"]
        obj.UnitPrice = req_data["UnitPrice"]
        obj.Quantity = req_data["Quantity"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        orderitems_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['DELETE'])
def delete_orderitem(id):
    try:
        orderitems_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['PUT'])
def put_orderitem(id):
    obj = OrderItem()
    req_data = request.get_json()

    schema = Schemes.orderitem_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        obj.OrderId = req_data["OrderId"]
        obj.ProductId = req_data["ProductId"]
        obj.UnitPrice = req_data["UnitPrice"]
        obj.Quantity = req_data["Quantity"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        orderitems_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    