from flask import Blueprint, request
from Application.Repositories.personlocations_repository import PersonLocationsRepository
from Application.Models.personlocation import PersonLocation

personlocations_controller_api = Blueprint('personlocations_controller_api', __name__)

personlocations_api = Blueprint('personlocations_api', __name__)
db = PersonLocationsRepository()


@personlocations_controller_api.route("/api/PersonLocations", methods=['GET'])
def get_personlocations():
    return db.get()


@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['GET'])
def get_personlocations_id(id):
    return db.get_id(id)


@personlocations_controller_api.route("/api/PersonLocations", methods=['POST'])
def post_personlocation():
    obj = PersonLocation()
    req_data = request.get_json()
    obj.LocationsLocationsId = req_data["LocationsLocationsId"]
    obj.SubAdress = req_data["SubAdress"]
    obj.LocationUsage = req_data["LocationUsage"]
    obj.Notes = req_data["Notes"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['DELETE'])
def delete_personlocation(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['PUT'])
def put_personlocation(id):
    obj = PersonLocation()
    req_data = request.get_json()
    obj.LocationsLocationsId = req_data["LocationsLocationsId"]
    obj.SubAdress = req_data["SubAdress"]
    obj.LocationUsage = req_data["LocationUsage"]
    obj.Notes = req_data["Notes"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    