from dataclasses import dataclass


@dataclass()
class Orders:

	def __init__(self):
		pass

	def load(self, fetch):
		self.OrderId = fetch[0]
		self.CustomerId = fetch[1]
		self.SalesRepId = fetch[2]
		self.OrderDate = fetch[3]
		self.OrderCode = fetch[4]
		self.OrderStatus = fetch[5]
		self.OrderTotal = fetch[6]
		self.OrderCurrency = fetch[7]
		self.PromotionCode = fetch[8]


	OrderId: int

	CustomerId: int

	SalesRepId: int

	OrderDate: str

	OrderCode: str

	OrderStatus: str

	OrderTotal: int

	OrderCurrency: str

	PromotionCode: str