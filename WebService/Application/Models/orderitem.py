from dataclasses import dataclass


@dataclass()
class OrderItem:

	def __init__(self):
		pass

	def load(self, fetch):
		self.OrderItemId = fetch[0]
		self.OrderId = fetch[1]
		self.ProductId = fetch[2]
		self.UnitPrice = fetch[3]
		self.Quantity = fetch[4]


	OrderItemId: int

	OrderId: int

	ProductId: int

	UnitPrice: int

	Quantity: int