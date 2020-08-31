from application.entities.products.model import Product


def temp_product():
    temp = Product()
    temp.ProductId = 0
    temp.ProductName = "erwr"
    temp.Description = "12313"
    temp.Category = 1
    temp.WeightClass = 1
    temp.WarrantlyPeriod = 112
    temp.SupplierId = 1
    temp.Status = "qewr"
    temp.ListPrice = 123
    temp.MinimumPrice = 1
    temp.PriceCurrency = "eqww:"
    temp.CatalogURL = "qwe"
    #
    return temp

def test_load():
    fetch = (0, "erwr", "12313", 1,1,112,1,"qewr", 123, 1, "eqww", "qwe")
    obj = Product()
    obj.load(fetch)

    return obj


assert test_load() == temp_product()
