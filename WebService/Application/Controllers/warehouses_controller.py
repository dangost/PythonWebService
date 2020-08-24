from flask import Blueprint, request
from Application.Repositories.warehouses_repository import WarehousesRepository
from Application.Models.warehouse import Warehouse

warehouses_controller_api = Blueprint('warehouses_controller_api', __name__)

warehouses_api = Blueprint('warehouses_api', __name__)
db = WarehousesRepository()


@warehouses_controller_api.route("/api/Warehouses", methods=['GET'])
def get_warehouses():
    return db.get()


@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['GET'])
def get_warehouses_id(id):
    return db.get_id(id)


@warehouses_controller_api.route("/api/Warehouses", methods=['POST'])
def post_warehouse():
    obj = Warehouse()
    req_data = request.get_json()
    obj.LocationId = req_data["LocationId"]
    obj.WarehouseName = req_data["WarehouseName"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['DELETE'])
def delete_warehouse(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['PUT'])
def put_warehouse(id):
    obj = Warehouse()
    req_data = request.get_json()
    obj.LocationId = req_data["LocationId"]
    obj.WarehouseName = req_data["WarehouseName"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    