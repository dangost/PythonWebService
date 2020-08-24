from flask import Blueprint, request
from Application.Repositories.orders_repository import OrdersRepository
from Application.Models.orders import Orders

orders_controller_api = Blueprint('orders_controller_api', __name__)

orders_api = Blueprint('orders_api', __name__)
db = OrdersRepository()


@orders_controller_api.route("/api/Orders", methods=['GET'])
def get_orders():
    return db.get()


@orders_controller_api.route("/api/Orders/<int:id>", methods=['GET'])
def get_orders_id(id):
    return db.get_id(id)


@orders_controller_api.route("/api/Orders", methods=['POST'])
def post_orders():
    obj = Orders()
    req_data = request.get_json()
    obj.CustomerId = req_data["CustomerId"]
    obj.SalesRepId = req_data["SalesRepId"]
    obj.OrderDate = req_data["OrderDate"]
    obj.OrderCode = req_data["OrderCode"]
    obj.OrderStatus = req_data["OrderStatus"]
    obj.OrderTotal = req_data["OrderTotal"]
    obj.OrderCurrency = req_data["OrderCurrency"]
    obj.PromotionCode = req_data["PromotionCode"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@orders_controller_api.route("/api/Orders/<int:id>", methods=['DELETE'])
def delete_orders(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@orders_controller_api.route("/api/Orders/<int:id>", methods=['PUT'])
def put_orders(id):
    obj = Orders()
    req_data = request.get_json()
    obj.CustomerId = req_data["CustomerId"]
    obj.SalesRepId = req_data["SalesRepId"]
    obj.OrderDate = req_data["OrderDate"]
    obj.OrderCode = req_data["OrderCode"]
    obj.OrderStatus = req_data["OrderStatus"]
    obj.OrderTotal = req_data["OrderTotal"]
    obj.OrderCurrency = req_data["OrderCurrency"]
    obj.PromotionCode = req_data["PromotionCode"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    