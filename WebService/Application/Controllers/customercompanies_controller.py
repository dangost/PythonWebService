from flask import Blueprint, request
from Application.Repositories.customercompanies_repository import CustomerCompaniesRepository
from Application.Models.customercompany import CustomerCompany

from Application.Abstraction.initialize import customercompanies_controller_init
db = customercompanies_controller_init()

customercompanies_controller_api = Blueprint('customercompanies_controller_api', __name__)


customercompanies_api = Blueprint('customercompanies_api', __name__)



@customercompanies_controller_api.route("/api/CustomerCompanies", methods=['GET'])
def get_customercompanies():
    return db.get()


@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['GET'])
def get_customercompanies_id(id):
    return db.get_id(id)


@customercompanies_controller_api.route("/api/CustomerCompanies", methods=['POST'])
def post_customercompany():
    obj = CustomerCompany()
    req_data = request.get_json()
    obj.CompanyName = req_data["CompanyName"]
    obj.CompanyCreditLimit = req_data["CompanyCreditLimit"]
    obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['DELETE'])
def delete_customercompany(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['PUT'])
def put_customercompany(id):
    obj = CustomerCompany()
    req_data = request.get_json()
    obj.CompanyName = req_data["CompanyName"]
    obj.CompanyCreditLimit = req_data["CompanyCreditLimit"]
    obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    