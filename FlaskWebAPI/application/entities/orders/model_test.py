from application.entities.orders.model import Orders


def temp_orders():
    temp = Orders()
    temp.OrderId = 0
    temp.CustomerId = 0
    temp.SalesRepId = 1
    temp.OrderDate ="1231"
    temp.OrderCode = 123
    temp.OrderStatus = "123"
    temp.OrderTotal = 123
    temp.OrderCurrency = "qwe"
    temp.PromotionCode = "uio"
    #
    return temp

def test_load():
    fetch = (0,1,1,"1231", 123, "123", 123, "qwe", "uio")
    obj = Orders()
    obj.load(fetch)

    return obj


assert test_load() == temp_orders()
