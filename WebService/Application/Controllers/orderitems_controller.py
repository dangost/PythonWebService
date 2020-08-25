from flask import Blueprint, request
from Application.Repositories.orderitems_repository import OrderItemsRepository
from Application.Models.orderitem import OrderItem

from Application.Abstraction.initialize import orderitems_controller_init
db = orderitems_controller_init()

orderitems_controller_api = Blueprint('orderitems_controller_api', __name__)

orderitems_api = Blueprint('orderitems_api', __name__)


@orderitems_controller_api.route("/api/OrderItems", methods=['GET'])
def get_orderitems():
    return db.get()


@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['GET'])
def get_orderitems_id(id):
    return db.get_id(id)


@orderitems_controller_api.route("/api/OrderItems", methods=['POST'])
def post_orderitem():
    obj = OrderItem()
    req_data = request.get_json()
    obj.OrderId = req_data["OrderId"]
    obj.ProductId = req_data["ProductId"]
    obj.UnitPrice = req_data["UnitPrice"]
    obj.Quantity = req_data["Quantity"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['DELETE'])
def delete_orderitem(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['PUT'])
def put_orderitem(id):
    obj = OrderItem()
    req_data = request.get_json()
    obj.OrderId = req_data["OrderId"]
    obj.ProductId = req_data["ProductId"]
    obj.UnitPrice = req_data["UnitPrice"]
    obj.Quantity = req_data["Quantity"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    