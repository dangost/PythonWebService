class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee","Employment","EmploymentJobs","Inventory","Location","OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product", "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees","Employments", "EmploymentJobs", "Inventories","Locations","OrderItems", "Orders", "People", "PersonLocations","PhoneNumbers", "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId","CustomerId","CompanyId","CustomerEmployeeId","EmployeeID","HRJobId","InventoryId","LocationId","OrderItemId","OrderId","Id","","PhoneNumberId","ProductId","","WarehouseId"]


path = r"C:\Users\danil\Desktop\autoflask\web_service\web_service.txt"

temp = ""
file = open(path, 'w')
for i in range(len(class_names)):
    temp += "from Application.Controllers."+list_names[i].lower()+"_controller import "+list_names[i].lower()+"_controller_api\n"

temp += "\n\n\n"

for i in range(len(class_names)):
    temp += "app.register_blueprint("+list_names[i].lower()+"_controller_api)\n"

file.write(temp)