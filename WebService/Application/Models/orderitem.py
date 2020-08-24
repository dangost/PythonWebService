class OrderItem:

	def __init__(self):
		pass

	def load(self, fetch):
		self.OrderItemId = fetch[0]
		self.OrderId = fetch[1]
		self.ProductId = fetch[2]
		self.UnitPrice = fetch[3]
		self.Quantity = fetch[4]

	def to_json(self):
		dictionary = {"OrderItemId": self.OrderItemId, "OrderId": self.OrderId, "ProductId": self.ProductId, "UnitPrice": self.UnitPrice, "Quantity": self.Quantity}
		return dictionary


	OrderItemId = 0

	OrderId = 0

	ProductId = 0

	UnitPrice = 0

	Quantity = 0