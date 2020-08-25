from Application.DI import inventories_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.inventories_repository import InventoriesRepository
from Application.Models.inventory import Inventory

inventories_controller_api = Blueprint('inventories_controller_api', __name__)

inventories_api = Blueprint('inventories_api', __name__)


@inventories_controller_api.route("/api/Inventories", methods=['GET'])
def get_inventories():
    return jsonify(inventories_db.get())


@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['GET'])
def get_inventories_id(id):
    return jsonify(inventories_db.get_id(id))


@inventories_controller_api.route("/api/Inventories", methods=['POST'])
def post_inventory():
    obj = Inventory()
    req_data = request.get_json()
    try:
        obj.WarehouseId = req_data["WarehouseId"]
        obj.QuantityOnHand = req_data["QuantityOnHand"]
        obj.QuantityAvaliable = req_data["QuantityAvaliable"]

    except BaseException:
        return "Invalid data"
    ls = [obj.WarehouseId, obj.QuantityOnHand, obj.QuantityAvaliable]
    if not validation(ls): return "Invalid data"


    try:
        inventories_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['DELETE'])
def delete_inventory(id):
    try:
        inventories_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['PUT'])
def put_inventory(id):
    obj = Inventory()
    req_data = request.get_json()
    try:
        obj.WarehouseId = req_data["WarehouseId"]
        obj.QuantityOnHand = req_data["QuantityOnHand"]
        obj.QuantityAvaliable = req_data["QuantityAvaliable"]

    except BaseException:
        return "Invalid data"
    ls = [obj.WarehouseId, obj.QuantityOnHand, obj.QuantityAvaliable]
    if not validation(ls): return "Invalid data"

    try:
        inventories_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    