from Application.DI import people_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.people_repository import PeopleRepository
from Application.Models.person import Person

people_controller_api = Blueprint('people_controller_api', __name__)

people_api = Blueprint('people_api', __name__)


@people_controller_api.route("/api/People", methods=['GET'])
def get_people():
    return jsonify(people_db.get())


@people_controller_api.route("/api/People/<int:id>", methods=['GET'])
def get_people_id(id):
    return jsonify(people_db.get_id(id))


@people_controller_api.route("/api/People", methods=['POST'])
def post_person():
    obj = Person()
    req_data = request.get_json()
    try:
        obj.FirstName = req_data["FirstName"]
        obj.LastName = req_data["LastName"]
        obj.MiddleName = req_data["MiddleName"]
        obj.Nickname = req_data["Nickname"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CultureCode = req_data["CultureCode"]
        obj.Gender = req_data["Gender"]

    except BaseException:
        return "Invalid data"

    ls = [obj.FirstName, obj.LastName, obj.MiddleName, obj.Nickname, obj.NatLangCode, obj.CultureCode, obj.Gender]
    if not validation(ls): return "Invalid data"


    try:
        people_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@people_controller_api.route("/api/People/<int:id>", methods=['DELETE'])
def delete_person(id):
    try:
        people_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@people_controller_api.route("/api/People/<int:id>", methods=['PUT'])
def put_person(id):
    obj = Person()
    req_data = request.get_json()
    try:
        obj.FirstName = req_data["FirstName"]
        obj.LastName = req_data["LastName"]
        obj.MiddleName = req_data["MiddleName"]
        obj.Nickname = req_data["Nickname"]
        obj.NatLangCode = req_data["NatLangCode"]
        obj.CultureCode = req_data["CultureCode"]
        obj.Gender = req_data["Gender"]

    except BaseException:
        return "Invalid data"
    ls = [obj.FirstName, obj.LastName, obj.MiddleName, obj.Nickname, obj.NatLangCode, obj.CultureCode, obj.Gender]
    if not validation(ls): return "Invalid data"
    try:
        people_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    