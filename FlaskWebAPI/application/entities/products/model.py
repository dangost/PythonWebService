from dataclasses import dataclass


@dataclass()
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


	ProductId: int

	ProductName: str

	Description: str

	Category: int

	WeightClass: str

	WarrantlyPeriod: int

	SupplierId: int

	Status: str

	ListPrice: int

	MinimumPrice: int

	PriceCurrency: str

	CatalogURL: str