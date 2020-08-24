from flask import Blueprint, request
from Application.Repositories.employmentjobs_repository import EmploymentJobsRepository
from Application.Models.employmentjobs import EmploymentJobs

employmentjobs_controller_api = Blueprint('employmentjobs_controller_api', __name__)

employmentjobs_api = Blueprint('employmentjobs_api', __name__)
db = EmploymentJobsRepository()


@employmentjobs_controller_api.route("/api/EmploymentJobs", methods=['GET'])
def get_employmentjobs():
    return db.get()


@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['GET'])
def get_employmentjobs_id(id):
    return db.get_id(id)


@employmentjobs_controller_api.route("/api/EmploymentJobs", methods=['POST'])
def post_employmentjobs():
    obj = EmploymentJobs()
    req_data = request.get_json()
    obj.CountriesCountryId = req_data["CountriesCountryId"]
    obj.JobTitle = req_data["JobTitle"]
    obj.MinSalary = req_data["MinSalary"]
    obj.MaxSalary = req_data["MaxSalary"]

    try:
        db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['DELETE'])
def delete_employmentjobs(id):
    try:
        db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['PUT'])
def put_employmentjobs(id):
    obj = EmploymentJobs()
    req_data = request.get_json()
    obj.CountriesCountryId = req_data["CountriesCountryId"]
    obj.JobTitle = req_data["JobTitle"]
    obj.MinSalary = req_data["MinSalary"]
    obj.MaxSalary = req_data["MaxSalary"]

    try:
        db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    