from Application.DI import employmentjobs_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.employmentjobs_repository import EmploymentJobsRepository
from Application.Models.employmentjobs import EmploymentJobs

employmentjobs_controller_api = Blueprint('employmentjobs_controller_api', __name__)

employmentjobs_api = Blueprint('employmentjobs_api', __name__)


@employmentjobs_controller_api.route("/api/EmploymentJobs", methods=['GET'])
def get_employmentjobs():
    return jsonify(employmentjobs_db.get())


@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['GET'])
def get_employmentjobs_id(id):
    return jsonify(employmentjobs_db.get_id(id))


@employmentjobs_controller_api.route("/api/EmploymentJobs", methods=['POST'])
def post_employmentjobs():
    obj = EmploymentJobs()
    req_data = request.get_json()
    try:
        obj.CountriesCountryId = req_data["CountriesCountryId"]
        obj.JobTitle = req_data["JobTitle"]
        obj.MinSalary = req_data["MinSalary"]
        obj.MaxSalary = req_data["MaxSalary"]

    except BaseException:
        return "Invalid data"
    ls = [obj.CountriesCountryId, obj.JobTitle, obj.MinSalary, obj.MaxSalary]
    if not validation(ls): return "Invalid data"


    try:
        employmentjobs_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['DELETE'])
def delete_employmentjobs(id):
    try:
        employmentjobs_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@employmentjobs_controller_api.route("/api/EmploymentJobs/<int:id>", methods=['PUT'])
def put_employmentjobs(id):
    obj = EmploymentJobs()
    req_data = request.get_json()
    try:
        obj.CountriesCountryId = req_data["CountriesCountryId"]
        obj.JobTitle = req_data["JobTitle"]
        obj.MinSalary = req_data["MinSalary"]
        obj.MaxSalary = req_data["MaxSalary"]

    except BaseException:
        return "Invalid data"
    ls = [obj.CountriesCountryId, obj.JobTitle, obj.MinSalary, obj.MaxSalary]
    if not validation(ls): return "Invalid data"
    try:
        employmentjobs_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    