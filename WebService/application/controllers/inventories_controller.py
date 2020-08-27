import json
import sqlite3
from application.app import inventories_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.valid.json_schemes import Schemes
from application.models.inventory import Inventory


inventories_controller_api = Blueprint('inventories_controller_api', __name__)
inventories_api = Blueprint('inventories_api', __name__)


@inventories_controller_api.route("/api/Inventories", methods=['GET'])
def get_inventories():
    obj = inventories_db.get()
    return jsonify(obj), HTTPStatus.OK
    
@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['GET'])
def get_inventories_id(id):
    obj = inventories_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK
    
@inventories_controller_api.route("/api/Inventories", methods=['POST'])
def post_inventory():
    obj = Inventory()
    req_data = request.get_json()

    schema = Schemes.inventory_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.NO_CONTENT

    try:
        obj.ProductId = req_data["ProductId"]
        obj.WarehouseId = req_data["WarehouseId"]
        obj.QuantityOnHand = req_data["QuantityOnHand"]
        obj.QuantityAvaliable = req_data["QuantityAvaliable"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.NO_CONTENT
    try:
        inventories_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['DELETE'])
def delete_inventory(id):
    try:
        inventories_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['PUT'])
def put_inventory(id):
    obj = Inventory()
    req_data = request.get_json()

    schema = Schemes.inventory_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.NO_CONTENT

    try:
        obj.ProductId = req_data["ProductId"]
        obj.WarehouseId = req_data["WarehouseId"]
        obj.QuantityOnHand = req_data["QuantityOnHand"]
        obj.QuantityAvaliable = req_data["QuantityAvaliable"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.NO_CONTENT
    try:
        inventories_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    