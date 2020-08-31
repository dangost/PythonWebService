from dataclasses import dataclass


@dataclass()
class Warehouse:

	def __init__(self):
		pass

	def load(self, fetch):
		self.WarehouseId = fetch[0]
		self.LocationId = fetch[1]
		self.WarehouseName = fetch[2]


	WarehouseId: int

	LocationId: int

	WarehouseName: str