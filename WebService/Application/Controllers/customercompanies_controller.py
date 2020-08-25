from Application.DI import customercompanies_db
from flask import jsonify
from flask import Blueprint, request
from Application.Repositories.customercompanies_repository import CustomerCompaniesRepository
from Application.Models.customercompany import CustomerCompany

customercompanies_controller_api = Blueprint('customercompanies_controller_api', __name__)

customercompanies_api = Blueprint('customercompanies_api', __name__)


@customercompanies_controller_api.route("/api/CustomerCompanies", methods=['GET'])
def get_customercompanies():
    return jsonify(customercompanies_db.get())


@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['GET'])
def get_customercompanies_id(id):
    return jsonify(customercompanies_db.get_id(id))


@customercompanies_controller_api.route("/api/CustomerCompanies", methods=['POST'])
def post_customercompany():
    obj = CustomerCompany()
    req_data = request.get_json()
    obj.CompanyName = req_data["CompanyName"]
    obj.CompanyCreditLimit = req_data["CompanyCreditLimit"]
    obj.CreditLimitCurrency = req_data["CreditLimitCurrency"]

    try:
        customercompanies_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customercompanies_controller_api.route("/api/CustomerCompanies/<int:id>", methods=['DELETE'])
def delete_customercompany(id):
    try:
        customercompanies_db.delete(id)
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
        customercompanies_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    