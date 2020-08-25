from Application.DI import customers_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.customers_repository import CustomersRepository
from Application.Models.customer import Customer

customers_controller_api = Blueprint('customers_controller_api', __name__)

customers_api = Blueprint('customers_api', __name__)


@customers_controller_api.route("/api/Customers", methods=['GET'])
def get_customers():
    return jsonify(customers_db.get())


@customers_controller_api.route("/api/Customers/<int:id>", methods=['GET'])
def get_customers_id(id):
    return jsonify(customers_db.get_id(id))


@customers_controller_api.route("/api/Customers", methods=['POST'])
def post_customer():
    obj = Customer()
    req_data = request.get_json()
    try:
        obj.AccountMgrId = req_data["AccountMgrId"]
        obj.IncomeLevel = req_data["IncomeLevel"]

    except BaseException:
        return "Invalid data"
    ls = [obj.AccountMgrId, obj.IncomeLevel]
    if not validation(ls): return "Invalid data"

    try:
        customers_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customers_controller_api.route("/api/Customers/<int:id>", methods=['DELETE'])
def delete_customer(id):
    try:
        customers_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customers_controller_api.route("/api/Customers/<int:id>", methods=['PUT'])
def put_customer(id):
    obj = Customer()
    req_data = request.get_json()
    try:
        obj.AccountMgrId = req_data["AccountMgrId"]
        obj.IncomeLevel = req_data["IncomeLevel"]

    except BaseException:
        return "Invalid data"
    ls = [obj.AccountMgrId, obj.IncomeLevel]
    if not validation(ls): return "Invalid data"
    try:
        customers_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    