class Product:

	def __init__(self):
		pass

	def load(self, fetch):
		self.ProductId = fetch[0]
		self.ProductName = fetch[1]
		self.Description = fetch[2]
		self.Category = fetch[3]
		self.WeightClass = fetch[4]
		self.WarrantlyPeriod = fetch[5]
		self.SupplierId = fetch[6]
		self.Status = fetch[7]
		self.ListPrice = fetch[8]
		self.MinimumPrice = fetch[9]
		self.PriceCurrency = fetch[10]
		self.CatalogURL = fetch[11]

	def to_json(self):
		dictionary = {"ProductId": self.ProductId, "ProductName": self.ProductName, "Description": self.Description, "Category": self.Category, "WeightClass": self.WeightClass, "WarrantlyPeriod": self.WarrantlyPeriod, "SupplierId": self.SupplierId, "Status": self.Status, "ListPrice": self.ListPrice, "MinimumPrice": self.MinimumPrice, "PriceCurrency": self.PriceCurrency, "CatalogURL": self.CatalogURL}
		return dictionary


	ProductId = 0

	ProductName = ""

	Description = ""

	Category = 0

	WeightClass = ""

	WarrantlyPeriod = 0

	SupplierId = 0

	Status = ""

	ListPrice = 0

	MinimumPrice = 0

	PriceCurrency = ""

	CatalogURL = ""