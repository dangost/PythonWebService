from dataclasses import dataclass


@dataclass()
class Inventory:

	def __init__(self):
		pass

	def load(self, fetch):
		self.InventoryId = fetch[0]
		self.ProductId = fetch[1]
		self.WarehouseId = fetch[2]
		self.QuantityOnHand = fetch[3]
		self.QuantityAvaliable = fetch[4]


	InventoryId: int

	ProductId: int

	WarehouseId: int

	QuantityOnHand: int

	QuantityAvaliable: int