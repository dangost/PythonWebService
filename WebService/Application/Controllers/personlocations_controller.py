from Application.App import personlocations_db
from flask import jsonify
from flask import Blueprint, request
import cerberus
from Application.valid.json_schemes import Schemes
from Application.Repositories.personlocations_repository import PersonLocationsRepository
from Application.Models.personlocation import PersonLocation

personlocations_controller_api = Blueprint('personlocations_controller_api', __name__)

personlocations_api = Blueprint('personlocations_api', __name__)


@personlocations_controller_api.route("/api/PersonLocations", methods=['GET'])
def get_personlocations():
    return jsonify(personlocations_db.get())


@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['GET'])
def get_personlocations_id(id):
    return jsonify(personlocations_db.get_id(id))


@personlocations_controller_api.route("/api/PersonLocations", methods=['POST'])
def post_personlocation():
    obj = PersonLocation()
    req_data = request.get_json()
    
    schema = Schemes.personlocation_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json"
        
    try:
        obj.PersonsPersonId = req_data["PersonsPersonId"]
        obj.LocationsLocationsId = req_data["LocationsLocationsId"]
        obj.SubAdress = req_data["SubAdress"]
        obj.LocationUsage = req_data["LocationUsage"]
        obj.Notes = req_data["Notes"]

    except BaseException:
        return "Invalid data"


    try:
        personlocations_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['DELETE'])
def delete_personlocation(id):
    try:
        personlocations_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@personlocations_controller_api.route("/api/PersonLocations/<int:id>", methods=['PUT'])
def put_personlocation(id):
    obj = PersonLocation()
    req_data = request.get_json()
    
    schema = Schemes.personlocation_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json"
        
    try:
        obj.PersonsPersonId = req_data["PersonsPersonId"]
        obj.LocationsLocationsId = req_data["LocationsLocationsId"]
        obj.SubAdress = req_data["SubAdress"]
        obj.LocationUsage = req_data["LocationUsage"]
        obj.Notes = req_data["Notes"]

    except BaseException:
        return "Invalid data"
    try:
        personlocations_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    