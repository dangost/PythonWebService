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

	def to_json(self):
		dictionary = {"OrderId": self.OrderId, "CustomerId": self.CustomerId, "SalesRepId": self.SalesRepId, "OrderDate": self.OrderDate, "OrderCode": self.OrderCode, "OrderStatus": self.OrderStatus, "OrderTotal": self.OrderTotal, "OrderCurrency": self.OrderCurrency, "PromotionCode": self.PromotionCode}
		return dictionary


	OrderId = 0

	CustomerId = 0

	SalesRepId = 0

	OrderDate = ""

	OrderCode = ""

	OrderStatus = ""

	OrderTotal = 0

	OrderCurrency = ""

	PromotionCode = ""