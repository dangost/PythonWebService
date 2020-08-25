from Application.DI import restrictedinfo_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.restrictedinfo_repository import RestrictedInfoRepository
from Application.Models.restrictedinfo import RestrictedInfo

restrictedinfo_controller_api = Blueprint('restrictedinfo_controller_api', __name__)

restrictedinfo_api = Blueprint('restrictedinfo_api', __name__)


@restrictedinfo_controller_api.route("/api/RestrictedInfo", methods=['GET'])
def get_restrictedinfo():
    return jsonify(restrictedinfo_db.get())


@restrictedinfo_controller_api.route("/api/RestrictedInfo/<int:id>", methods=['GET'])
def get_restrictedinfo_id(id):
    return jsonify(restrictedinfo_db.get_id(id))


@restrictedinfo_controller_api.route("/api/RestrictedInfo", methods=['POST'])
def post_restrictedinfo():
    obj = RestrictedInfo()
    req_data = request.get_json()
    try:
        obj.DateOfBirth = req_data["DateOfBirth"]
        obj.DateOfDeath = req_data["DateOfDeath"]
        obj.GovernmentId = req_data["GovernmentId"]
        obj.PassportId = req_data["PassportId"]
        obj.HireDire = req_data["HireDire"]
        obj.SeniorityCode = req_data["SeniorityCode"]

    except BaseException:
        return "Invalid data"

    ls = [obj.DateOfBirth, obj.DateOfDeath, obj.GovernmentId, obj.PassportId, obj.HireDire, obj.SeniorityCode]
    if not validation(ls): return "Invalid data"


    try:
        restrictedinfo_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@restrictedinfo_controller_api.route("/api/RestrictedInfo/<int:id>", methods=['DELETE'])
def delete_restrictedinfo(id):
    try:
        restrictedinfo_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@restrictedinfo_controller_api.route("/api/RestrictedInfo/<int:id>", methods=['PUT'])
def put_restrictedinfo(id):
    obj = RestrictedInfo()
    req_data = request.get_json()
    try:
        obj.DateOfBirth = req_data["DateOfBirth"]
        obj.DateOfDeath = req_data["DateOfDeath"]
        obj.GovernmentId = req_data["GovernmentId"]
        obj.PassportId = req_data["PassportId"]
        obj.HireDire = req_data["HireDire"]
        obj.SeniorityCode = req_data["SeniorityCode"]

    except BaseException:
        return "Invalid data"
    ls = [obj.DateOfBirth, obj.DateOfDeath, obj.GovernmentId, obj.PassportId, obj.HireDire, obj.SeniorityCode]
    if not validation(ls): return "Invalid data"
    try:
        restrictedinfo_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    