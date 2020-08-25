from dataclasses import dataclass


@dataclass()
class Country:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CountryId = fetch[0]
		self.CountryName = fetch[1]
		self.CountryCode = fetch[2]
		self.NatLangCode = fetch[3]
		self.CurrencyCode = fetch[4]


	CountryId: int

	CountryName: str

	CountryCode: str

	NatLangCode: int

	CurrencyCode: str