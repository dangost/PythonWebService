class Warehouse:

	def __init__(self):
		pass

	def load(self, fetch):
		self.WarehouseId = fetch[0]
		self.LocationId = fetch[1]
		self.WarehouseName = fetch[2]

	def to_json(self):
		dictionary = {"WarehouseId": self.WarehouseId, "LocationId": self.LocationId, "WarehouseName": self.WarehouseName}
		return dictionary


	WarehouseId = 0

	LocationId = 0

	WarehouseName = ""