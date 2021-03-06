from flask import Flask
from application.controllers.countries_controller import countries_controller_api
from application.controllers.customers_controller import customers_controller_api
from application.controllers.customercompanies_controller import customercompanies_controller_api
from application.controllers.customeremployees_controller import customeremployees_controller_api
from application.controllers.employments_controller import employments_controller_api
from application.controllers.employmentjobs_controller import employmentjobs_controller_api
from application.controllers.inventories_controller import inventories_controller_api
from application.controllers.locations_controller import locations_controller_api
from application.controllers.orderitems_controller import orderitems_controller_api
from application.controllers.orders_controller import orders_controller_api
from application.controllers.people_controller import people_controller_api
from application.controllers.personlocations_controller import personlocations_controller_api
from application.controllers.phonenumbers_controller import phonenumbers_controller_api
from application.controllers.products_controller import products_controller_api
from application.controllers.restrictedinfo_controller import restrictedinfo_controller_api
from application.controllers.warehouses_controller import warehouses_controller_api

app = Flask(__name__)

app.register_blueprint(countries_controller_api)
app.register_blueprint(customers_controller_api)
app.register_blueprint(customercompanies_controller_api)
app.register_blueprint(customeremployees_controller_api)
app.register_blueprint(employments_controller_api)
app.register_blueprint(employmentjobs_controller_api)
app.register_blueprint(inventories_controller_api)
app.register_blueprint(locations_controller_api)
app.register_blueprint(orderitems_controller_api)
app.register_blueprint(orders_controller_api)
app.register_blueprint(people_controller_api)
app.register_blueprint(personlocations_controller_api)
app.register_blueprint(phonenumbers_controller_api)
app.register_blueprint(products_controller_api)
app.register_blueprint(restrictedinfo_controller_api)
app.register_blueprint(warehouses_controller_api)


if __name__ == "__main__":
    app.run()








