from Application.DI import products_db
from flask import jsonify
from flask import Blueprint, request
from Application.Repositories.products_repository import ProductsRepository
from Application.Models.product import Product

products_controller_api = Blueprint('products_controller_api', __name__)

products_api = Blueprint('products_api', __name__)


@products_controller_api.route("/api/Products", methods=['GET'])
def get_products():
    return jsonify(products_db.get())


@products_controller_api.route("/api/Products/<int:id>", methods=['GET'])
def get_products_id(id):
    return jsonify(products_db.get_id(id))


@products_controller_api.route("/api/Products", methods=['POST'])
def post_product():
    obj = Product()
    req_data = request.get_json()
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

    try:
        products_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@products_controller_api.route("/api/Products/<int:id>", methods=['DELETE'])
def delete_product(id):
    try:
        products_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@products_controller_api.route("/api/Products/<int:id>", methods=['PUT'])
def put_product(id):
    obj = Product()
    req_data = request.get_json()
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

    try:
        products_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    