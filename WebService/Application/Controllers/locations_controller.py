from flask import Blueprint, request
from Application.Repositories.locations_repository import LocationsRepository
from Application.Models.location import Location

locations_controller_api = Blueprint('locations_controller_api', __name__)

locations_api = Blueprint('locations_api', __name__)
db = LocationsRepository()


@locations_controller_api.route("/api/Locations", methods=['GET'])
def get_locations():
    return db.get()


@locations_controller_api.route("/api/Locations/<int:id>", methods=['GET'])
def get_locations_id(id):
    return db.get_id(id)


@locations_controller_api.route("/api/Locations", methods=['POST'])
def post_location():
    obj = Location()
    req_data = request.get_json()
    obj.CountryId = req_data["CountryId"]
    obj.AdressLine1 = req_data["AdressLine1"]
    obj.AdressLine2 = req_data["AdressLine2"]
    obj.City = req_data["City"]
    obj.State = req_data["State"]
    obj.District = req_data["District"]
    obj.PostalCode = req_data["PostalCode"]
    obj.LocationTypeCode = req_data["LocationTypeCode"]
    obj.Description = req_data["Description"]
    obj.ShippingNotes = req_data["ShippingNotes"]
    obj.CountriesCountryId = req_data["CountriesCountryId"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@locations_controller_api.route("/api/Locations/<int:id>", methods=['DELETE'])
def delete_location(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@locations_controller_api.route("/api/Locations/<int:id>", methods=['PUT'])
def put_location(id):
    obj = Location()
    req_data = request.get_json()
    obj.CountryId = req_data["CountryId"]
    obj.AdressLine1 = req_data["AdressLine1"]
    obj.AdressLine2 = req_data["AdressLine2"]
    obj.City = req_data["City"]
    obj.State = req_data["State"]
    obj.District = req_data["District"]
    obj.PostalCode = req_data["PostalCode"]
    obj.LocationTypeCode = req_data["LocationTypeCode"]
    obj.Description = req_data["Description"]
    obj.ShippingNotes = req_data["ShippingNotes"]
    obj.CountriesCountryId = req_data["CountriesCountryId"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    