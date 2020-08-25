from Application.DI import customeremployees_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.customeremployees_repository import CustomerEmployeesRepository
from Application.Models.customeremployee import CustomerEmployee

customeremployees_controller_api = Blueprint('customeremployees_controller_api', __name__)

customeremployees_api = Blueprint('customeremployees_api', __name__)


@customeremployees_controller_api.route("/api/CustomerEmployees", methods=['GET'])
def get_customeremployees():
    return jsonify(customeremployees_db.get())


@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['GET'])
def get_customeremployees_id(id):
    return jsonify(customeremployees_db.get_id(id))


@customeremployees_controller_api.route("/api/CustomerEmployees", methods=['POST'])
def post_customeremployee():
    obj = CustomerEmployee()
    req_data = request.get_json()
    try:
        obj.BadgeNumber = req_data["BadgeNumber"]
        obj.JobTitle = req_data["JobTitle"]
        obj.Department = req_data["Department"]
        obj.CreditLimit = req_data["CreditLimit"]
        obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    except BaseException:
        return "Invalid data"
    ls = [obj.BadgeNumber, obj.JobTitle, obj.Department, obj.CreditLimit, obj.CreditLimitCurrency]
    if not validation(ls): return "Invalid data"

    try:
        customeremployees_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['DELETE'])
def delete_customeremployee(id):
    try:
        customeremployees_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['PUT'])
def put_customeremployee(id):
    obj = CustomerEmployee()
    req_data = request.get_json()
    try:
        obj.BadgeNumber = req_data["BadgeNumber"]
        obj.JobTitle = req_data["JobTitle"]
        obj.Department = req_data["Department"]
        obj.CreditLimit = req_data["CreditLimit"]
        obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    except BaseException:
        return "Invalid data"
    ls = [obj.BadgeNumber, obj.JobTitle, obj.Department, obj.CreditLimit, obj.CreditLimitCurrency]
    if not validation(ls): return "Invalid data"
    try:
        customeremployees_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    