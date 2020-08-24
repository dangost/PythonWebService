class Country:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CountryId = fetch[0]
		self.CountryName = fetch[1]
		self.CountryCode = fetch[2]
		self.NatLangCode = fetch[3]
		self.CurrencyCode = fetch[4]

	def to_json(self):
		dictionary = {"CountryId": self.CountryId, "CountryName": self.CountryName, "CountryCode": self.CountryCode, "NatLangCode": self.NatLangCode, "CurrencyCode": self.CurrencyCode}
		return dictionary


	CountryId = 0

	CountryName = ""

	CountryCode = ""

	NatLangCode = 0

	CurrencyCode = ""