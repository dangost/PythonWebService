from Application.DI import orderitems_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.orderitems_repository import OrderItemsRepository
from Application.Models.orderitem import OrderItem

orderitems_controller_api = Blueprint('orderitems_controller_api', __name__)

orderitems_api = Blueprint('orderitems_api', __name__)


@orderitems_controller_api.route("/api/OrderItems", methods=['GET'])
def get_orderitems():
    return jsonify(orderitems_db.get())


@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['GET'])
def get_orderitems_id(id):
    return jsonify(orderitems_db.get_id(id))


@orderitems_controller_api.route("/api/OrderItems", methods=['POST'])
def post_orderitem():
    obj = OrderItem()
    req_data = request.get_json()
    try:
        obj.UnitPrice = req_data["UnitPrice"]
        obj.Quantity = req_data["Quantity"]

    except BaseException:
        return "Invalid data"
    ls = [obj.UnitPrice, obj.Quantity]
    if not validation(ls): return "Invalid data"


    try:
        orderitems_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['DELETE'])
def delete_orderitem(id):
    try:
        orderitems_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@orderitems_controller_api.route("/api/OrderItems/<int:id>", methods=['PUT'])
def put_orderitem(id):
    obj = OrderItem()
    req_data = request.get_json()
    try:
        obj.UnitPrice = req_data["UnitPrice"]
        obj.Quantity = req_data["Quantity"]

    except BaseException:
        return "Invalid data"
    ls = [obj.UnitPrice, obj.Quantity]
    if not validation(ls): return "Invalid data"
    try:
        orderitems_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    