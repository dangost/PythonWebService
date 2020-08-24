class Inventory:

	def __init__(self):
		pass

	def load(self, fetch):
		self.InventoryId = fetch[0]
		self.ProductId = fetch[1]
		self.WarehouseId = fetch[2]
		self.QuantityOnHand = fetch[3]
		self.QuantityAvaliable = fetch[4]

	def to_json(self):
		dictionary = {"InventoryId": self.InventoryId, "ProductId": self.ProductId, "WarehouseId": self.WarehouseId, "QuantityOnHand": self.QuantityOnHand, "QuantityAvaliable": self.QuantityAvaliable}
		return dictionary


	InventoryId = 0

	ProductId = 0

	WarehouseId = 0

	QuantityOnHand = 0

	QuantityAvaliable = 0