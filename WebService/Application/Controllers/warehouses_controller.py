from Application.DI import warehouses_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.warehouses_repository import WarehousesRepository
from Application.Models.warehouse import Warehouse

warehouses_controller_api = Blueprint('warehouses_controller_api', __name__)

warehouses_api = Blueprint('warehouses_api', __name__)


@warehouses_controller_api.route("/api/Warehouses", methods=['GET'])
def get_warehouses():
    return jsonify(warehouses_db.get())


@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['GET'])
def get_warehouses_id(id):
    return jsonify(warehouses_db.get_id(id))


@warehouses_controller_api.route("/api/Warehouses", methods=['POST'])
def post_warehouse():
    obj = Warehouse()
    req_data = request.get_json()
    try:
        obj.LocationId = req_data["LocationId"]
        obj.WarehouseName = req_data["WarehouseName"]

    except BaseException:
        return "Invalid data"
    ls = [obj.LocationId, obj.WarehouseName]
    if not validation(ls): return "Invalid data"


    try:
        warehouses_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['DELETE'])
def delete_warehouse(id):
    try:
        warehouses_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@warehouses_controller_api.route("/api/Warehouses/<int:id>", methods=['PUT'])
def put_warehouse(id):
    obj = Warehouse()
    req_data = request.get_json()
    try:
        obj.LocationId = req_data["LocationId"]
        obj.WarehouseName = req_data["WarehouseName"]

    except BaseException:
        return "Invalid data"
    ls = [obj.LocationId, obj.WarehouseName]
    if not validation(ls): return "Invalid data"
    try:
        warehouses_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    