from flask import Blueprint, request
from Application.Repositories.customeremployees_repository import CustomerEmployeesRepository
from Application.Models.customeremployee import CustomerEmployee

from Application.Abstraction.initialize import customers_controller_init
db = customers_controller_init()

customeremployees_controller_api = Blueprint('customeremployees_controller_api', __name__)

customeremployees_api = Blueprint('customeremployees_api', __name__)


@customeremployees_controller_api.route("/api/CustomerEmployees", methods=['GET'])
def get_customeremployees():
    return db.get()


@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['GET'])
def get_customeremployees_id(id):
    return db.get_id(id)


@customeremployees_controller_api.route("/api/CustomerEmployees", methods=['POST'])
def post_customeremployee():
    obj = CustomerEmployee()
    req_data = request.get_json()
    obj.CompanyId = req_data["CompanyId"]
    obj.BadgeNumber = req_data["BadgeNumber"]
    obj.JobTitle = req_data["JobTitle"]
    obj.Department = req_data["Department"]
    obj.CreditLimit = req_data["CreditLimit"]
    obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['DELETE'])
def delete_customeremployee(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customeremployees_controller_api.route("/api/CustomerEmployees/<int:id>", methods=['PUT'])
def put_customeremployee(id):
    obj = CustomerEmployee()
    req_data = request.get_json()
    obj.CompanyId = req_data["CompanyId"]
    obj.BadgeNumber = req_data["BadgeNumber"]
    obj.JobTitle = req_data["JobTitle"]
    obj.Department = req_data["Department"]
    obj.CreditLimit = req_data["CreditLimit"]
    obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    