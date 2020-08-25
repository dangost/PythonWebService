from flask import Blueprint, request
from Application.Repositories.inventories_repository import InventoriesRepository
from Application.Models.inventory import Inventory

from Application.Abstraction.initialize import inventories_controller_init
db = inventories_controller_init()

inventories_controller_api = Blueprint('inventories_controller_api', __name__)

inventories_api = Blueprint('inventories_api', __name__)


@inventories_controller_api.route("/api/Inventories", methods=['GET'])
def get_inventories():
    return db.get()


@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['GET'])
def get_inventories_id(id):
    return db.get_id(id)


@inventories_controller_api.route("/api/Inventories", methods=['POST'])
def post_inventory():
    obj = Inventory()
    req_data = request.get_json()
    obj.ProductId = req_data["ProductId"]
    obj.WarehouseId = req_data["WarehouseId"]
    obj.QuantityOnHand = req_data["QuantityOnHand"]
    obj.QuantityAvaliable = req_data["QuantityAvaliable"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['DELETE'])
def delete_inventory(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@inventories_controller_api.route("/api/Inventories/<int:id>", methods=['PUT'])
def put_inventory(id):
    obj = Inventory()
    req_data = request.get_json()
    obj.ProductId = req_data["ProductId"]
    obj.WarehouseId = req_data["WarehouseId"]
    obj.QuantityOnHand = req_data["QuantityOnHand"]
    obj.QuantityAvaliable = req_data["QuantityAvaliable"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    