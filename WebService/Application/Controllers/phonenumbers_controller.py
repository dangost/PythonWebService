from flask import Blueprint, request
from Application.Repositories.phonenumbers_repository import PhoneNumbersRepository
from Application.Models.phonenumber import PhoneNumber

phonenumbers_controller_api = Blueprint('phonenumbers_controller_api', __name__)

phonenumbers_api = Blueprint('phonenumbers_api', __name__)
db = PhoneNumbersRepository()


@phonenumbers_controller_api.route("/api/PhoneNumbers", methods=['GET'])
def get_phonenumbers():
    return db.get()


@phonenumbers_controller_api.route("/api/PhoneNumbers/<int:id>", methods=['GET'])
def get_phonenumbers_id(id):
    return db.get_id(id)


@phonenumbers_controller_api.route("/api/PhoneNumbers", methods=['POST'])
def post_phonenumber():
    obj = PhoneNumber()
    req_data = request.get_json()
    obj.PeoplePersonId = req_data["PeoplePersonId"]
    obj.LocationLocationId = req_data["LocationLocationId"]
    obj.Phonenumber = req_data["Phonenumber"]
    obj.CountryCode = req_data["CountryCode"]
    obj.PhoneType = req_data["PhoneType"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@phonenumbers_controller_api.route("/api/PhoneNumbers/<int:id>", methods=['DELETE'])
def delete_phonenumber(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@phonenumbers_controller_api.route("/api/PhoneNumbers/<int:id>", methods=['PUT'])
def put_phonenumber(id):
    obj = PhoneNumber()
    req_data = request.get_json()
    obj.PeoplePersonId = req_data["PeoplePersonId"]
    obj.LocationLocationId = req_data["LocationLocationId"]
    obj.Phonenumber = req_data["Phonenumber"]
    obj.CountryCode = req_data["CountryCode"]
    obj.PhoneType = req_data["PhoneType"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    