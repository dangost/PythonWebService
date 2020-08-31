from application.entities.warehouses.model import Warehouse


def temp_warehouse():
    temp = Warehouse()
    temp.WarehouseId = 1
    temp.LocationId = 1
    temp.WarehouseName = "123"
    return temp

def test_load():
    fetch = (1, 1, "123")
    obj = Warehouse()
    obj.load(fetch)

    return obj


assert test_load() == temp_warehouse()
