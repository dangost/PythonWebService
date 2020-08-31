import json
import sqlite3
from application.app import warehouses_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.warehouses.schema import get_json_schema
from application.entities.warehouses.model import Warehouse
warehouses_controller_api = Blueprint('warehouses_controller_api', __name__)
warehouses_api = Blueprint('warehouses_api', __name__)
@warehouses_controller_api.route("/api/Warehouses", methods=['GET'])

def get_warehouses():
    obj = warehouses_db.get()
    return jsonify(obj), HTTPStatus.OK

@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['GET'])
def get_warehouses_id(id):
    obj = warehouses_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@warehouses_controller_api.route("/api/Warehouses", methods=['POST'])
def post_warehouse():
    obj = Warehouse()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.LocationId = req_data["LocationId"]
        obj.WarehouseName = req_data["WarehouseName"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        warehouses_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['DELETE'])
def delete_warehouse(id):
    try:
        warehouses_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['PUT'])
def put_warehouse(id):
    obj = Warehouse()
    req_data = request.get_json()
    schema = get_json_schema
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.LocationId = req_data["LocationId"]
        obj.WarehouseName = req_data["WarehouseName"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        warehouses_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    