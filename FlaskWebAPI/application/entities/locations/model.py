from dataclasses import dataclass


@dataclass()
class Location:

	def __init__(self):
		pass

	def load(self, fetch):
		self.LocationId = fetch[0]
		self.CountryId = fetch[1]
		self.AdressLine1 = fetch[2]
		self.AdressLine2 = fetch[3]
		self.City = fetch[4]
		self.State = fetch[5]
		self.District = fetch[6]
		self.PostalCode = fetch[7]
		self.LocationTypeCode = fetch[8]
		self.Description = fetch[9]
		self.ShippingNotes = fetch[10]
		self.CountriesCountryId = fetch[11]


	LocationId: int

	CountryId: int

	AdressLine1: str

	AdressLine2: str

	City: str

	State: str

	District: str

	PostalCode: str

	LocationTypeCode: int

	Description: str

	ShippingNotes: str

	CountriesCountryId: int