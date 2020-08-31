from application.entities.orderitems.model import OrderItem


def temp_orderitem():
    temp = OrderItem()
    temp.OrderItemId = 0
    temp.OrderId = 1
    temp.ProductId = 1
    temp.UnitPrice = 1
    temp.Quantity = 1
    #
    return temp

def test_load():
    fetch = (0, 1,1,1,1)
    obj = OrderItem()
    obj.load(fetch)

    return obj


assert test_load() == temp_orderitem()
