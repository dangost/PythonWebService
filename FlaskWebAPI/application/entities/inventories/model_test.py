from application.entities.inventories.model import Inventory


def temp_inventory():
    temp = Inventory()
    temp.InventoryId = 0
    temp.ProductId = 1
    temp.WarehouseId = 1
    temp.QuantityOnHand = 1
    temp.QuantityAvaliable = 1
    #
    return temp

def test_load():
    fetch = (0, 1,1,1,1)
    obj = Inventory()
    obj.load(fetch)

    return obj


assert test_load() == temp_inventory()
