from flask import Blueprint, request
from Application.Repositories.customers_repository import CustomersRepository
from Application.Models.customer import Customer

from Application.Abstraction.initialize import customers_controller_init
db = customers_controller_init()

customers_controller_api = Blueprint('customers_controller_api', __name__)

customers_api = Blueprint('customers_api', __name__)

@customers_controller_api.route("/api/Customers", methods=['GET'])
def get_customers():
    return db.get()


@customers_controller_api.route("/api/Customers/<int:id>", methods=['GET'])
def get_customers_id(id):
    return db.get_id(id)


@customers_controller_api.route("/api/Customers", methods=['POST'])
def post_customer():
    obj = Customer()
    req_data = request.get_json()
    obj.PersonId = req_data["PersonId"]
    obj.CustomEmployeeId = req_data["CustomEmployeeId"]
    obj.AccountMgrId = req_data["AccountMgrId"]
    obj.IncomeLevel = req_data["IncomeLevel"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customers_controller_api.route("/api/Customers/<int:id>", methods=['DELETE'])
def delete_customer(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@customers_controller_api.route("/api/Customers/<int:id>", methods=['PUT'])
def put_customer(id):
    obj = Customer()
    req_data = request.get_json()
    obj.PersonId = req_data["PersonId"]
    obj.CustomEmployeeId = req_data["CustomEmployeeId"]
    obj.AccountMgrId = req_data["AccountMgrId"]
    obj.IncomeLevel = req_data["IncomeLevel"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    