from Testing import data

import requests

data = data.Data()
ll = r"log.txt"
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs", "Inventories", "Locations","OrderItems", "Orders", "People", "PersonLocations","PhoneNumbers", "Products", "RestrictedInfo", "Warehouses"]

valid_list = [data.country_valid_json, data.customer_company_valid_json, data.customer_company_valid_json, data.customer_employee_valid_json, data.employment_valid_json, data.employment_jobs_valid_json, data.inventory_valid_json, data.location_valid_json, data.order_item_valid_json, data.orders_valid_json, data.person_valid_json, data.person_location_valid_json, data.phone_number_valid_json, data.product_valid_json, data.restricted_valid_json, data.warehouse_valid_json]
invalid_list = [data.country_invalid_json, data.customer_company_invalid_json, data.customer_company_invalid_json, data.customer_employee_invalid_json, data.employment_invalid_json, data.employment_jobs_invalid_json, data.inventory_invalid_json, data.location_invalid_json, data.order_item_invalid_json, data.orders_invalid_json, data.person_invalid_json, data.person_location_invalid_json, data.phone_number_invalid_json, data.product_invalid_json, data.restricted_invalid_json, data.warehouse_invalid_json]

file = open(ll, 'w')
for i in range(len(list_names)):
    link = r"http://127.0.0.1:5000/api/"+list_names[i]

    log = ""
    log += ""+list_names[i]+" \nValid: "
    if requests.post(link, json=valid_list[i]).text == "Invalid data":
        log += "Denied\n\n"
    else:
        log += "Accepted\n\n"

    log += "Invalid: "
    if requests.post(link, json=invalid_list[i]).text != "Invalid data":
        log += "Denied\n\n\n\n"
    else:
        log += "Accepted\n\n\n\n"

    file.write(log)

