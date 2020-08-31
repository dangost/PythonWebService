class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee","Employment","EmploymentJobs","Inventory","Location","OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product", "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees","Employments", "EmploymentJobs", "Inventories","Locations","OrderItems", "Orders", "People", "PersonLocations","PhoneNumbers", "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId","CustomerId","CompanyId","CustomerEmployeeId","EmployeeID","HRJobId","InventoryId","LocationId","OrderItemId","OrderId","Id","","PhoneNumberId","ProductId","","WarehouseId"]

temp = ""

for i in range(len(class_names)):
    temp += "from Application.Repositories."+list_names[i].lower()+"_repository import "+list_names[i]+"Repository\n"+list_names[i].lower()+"_db: ARepository = "+list_names[i]+"Repository()\n"


path = r"C:\Users\danil\Desktop\tttt.txt"
file = open(path, 'w')

file.write(temp)