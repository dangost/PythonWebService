from Application.DI import employments_db
from flask import jsonify
from flask import Blueprint, request
from Application.Repositories.employments_repository import EmploymentsRepository
from Application.Models.employment import Employment

employments_controller_api = Blueprint('employments_controller_api', __name__)

employments_api = Blueprint('employments_api', __name__)


@employments_controller_api.route("/api/Employments", methods=['GET'])
def get_employments():
    return jsonify(employments_db.get())


@employments_controller_api.route("/api/Employments/<int:id>", methods=['GET'])
def get_employments_id(id):
    return jsonify(employments_db.get_id(id))


@employments_controller_api.route("/api/Employments", methods=['POST'])
def post_employment():
    obj = Employment()
    req_data = request.get_json()
    obj.PersonId = req_data["PersonId"]
    obj.HRJobId = req_data["HRJobId"]
    obj.ManagerEmployeeId = req_data["ManagerEmployeeId"]
    obj.StartDate = req_data["StartDate"]
    obj.EndDate = req_data["EndDate"]
    obj.Salary = req_data["Salary"]
    obj.CommissionPercent = req_data["CommissionPercent"]
    obj.Employmentcol = req_data["Employmentcol"]

    try:
        employments_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@employments_controller_api.route("/api/Employments/<int:id>", methods=['DELETE'])
def delete_employment(id):
    try:
        employments_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@employments_controller_api.route("/api/Employments/<int:id>", methods=['PUT'])
def put_employment(id):
    obj = Employment()
    req_data = request.get_json()
    obj.PersonId = req_data["PersonId"]
    obj.HRJobId = req_data["HRJobId"]
    obj.ManagerEmployeeId = req_data["ManagerEmployeeId"]
    obj.StartDate = req_data["StartDate"]
    obj.EndDate = req_data["EndDate"]
    obj.Salary = req_data["Salary"]
    obj.CommissionPercent = req_data["CommissionPercent"]
    obj.Employmentcol = req_data["Employmentcol"]

    try:
        employments_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    