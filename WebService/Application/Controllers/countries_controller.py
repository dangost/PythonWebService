from flask import Blueprint
countries_controller_api = Blueprint('countries_controller_api', __name__)


class CountriesController:
    countries_api = Blueprint('countries_api', __name__)

    @staticmethod
    @countries_controller_api.route("/api/Countries", method='GET')
    def get_countries():
        return "Countries in JSON"

    @staticmethod
    @countries_controller_api.route("/api/Countries/<int:id>", method='GET')
    def get_countries_id(id):
        return "Countries[" + str(id) + "]"

    @staticmethod
    @countries_controller_api.route("/api/Countries", method='POST')
    def post_country():
        pass

    @staticmethod
    @countries_controller_api.route("/api/Countries/<int:id>", method='DELETE')
    def delete_country(id):
        pass




