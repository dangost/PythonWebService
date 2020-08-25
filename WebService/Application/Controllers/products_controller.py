from flask import Blueprint, request
from Application.Repositories.products_repository import ProductsRepository
from Application.Models.product import Product

from Application.Abstraction.initialize import products_controller_init
db = products_controller_init()

products_controller_api = Blueprint('products_controller_api', __name__)

products_api = Blueprint('products_api', __name__)


@products_controller_api.route("/api/Products", methods=['GET'])
def get_products():
    return db.get()


@products_controller_api.route("/api/Products/<int:id>", methods=['GET'])
def get_products_id(id):
    return db.get_id(id)


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
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@products_controller_api.route("/api/Products/<int:id>", methods=['DELETE'])
def delete_product(id):
    try:
        db.delete(id)
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
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    