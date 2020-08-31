import json
import sqlite3
from application.app import products_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.entities.products.schema import get_json_schema
from application.entities.products.model import Product
products_controller_api = Blueprint('products_controller_api', __name__)
products_api = Blueprint('products_api', __name__)
@products_controller_api.route("/api/Products", methods=['GET'])

def get_products():
    obj = products_db.get()
    return jsonify(obj), HTTPStatus.OK

@products_controller_api.route("/api/Products/<int:id>", methods=['GET'])
def get_products_id(id):
    obj = products_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK

@products_controller_api.route("/api/Products", methods=['POST'])
def post_product():
    obj = Product()
    req_data = request.get_json()
    schema = Schemes.product_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.ProductName = req_data["ProductName"]
        obj.Description = req_data["Description"]
        obj.Category = req_data["Category"]
        obj.WeightClass = req_data["WeightClass"]
        obj.WarrantlyPeriod = req_data["WarrantlyPeriod"]
        obj.SupplierId = req_data["SupplierId"]
        obj.Status = req_data["Status"]
        obj.ListPrice = req_data["ListPrice"]
        obj.MinimumPrice = req_data["MinimumPrice"]
        obj.PriceCurrency = req_data["PriceCurrency"]
        obj.CatalogURL = req_data["CatalogURL"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        products_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@products_controller_api.route("/api/Products/<int:id>", methods=['DELETE'])
def delete_product(id):
    try:
        products_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK

@products_controller_api.route("/api/Products/<int:id>", methods=['PUT'])
def put_product(id):
    obj = Product()
    req_data = request.get_json()
    schema = Schemes.product_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        obj.ProductName = req_data["ProductName"]
        obj.Description = req_data["Description"]
        obj.Category = req_data["Category"]
        obj.WeightClass = req_data["WeightClass"]
        obj.WarrantlyPeriod = req_data["WarrantlyPeriod"]
        obj.SupplierId = req_data["SupplierId"]
        obj.Status = req_data["Status"]
        obj.ListPrice = req_data["ListPrice"]
        obj.MinimumPrice = req_data["MinimumPrice"]
        obj.PriceCurrency = req_data["PriceCurrency"]
        obj.CatalogURL = req_data["CatalogURL"]

    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        products_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    