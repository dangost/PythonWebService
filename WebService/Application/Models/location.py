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

	def to_json(self):
		dictionary = {"LocationId": self.LocationId, "CountryId": self.CountryId, "AdressLine1": self.AdressLine1, "AdressLine2": self.AdressLine2, "City": self.City, "State": self.State, "District": self.District, "PostalCode": self.PostalCode, "LocationTypeCode": self.LocationTypeCode, "Description": self.Description, "ShippingNotes": self.ShippingNotes, "CountriesCountryId": self.CountriesCountryId}
		return dictionary


	LocationId = 0

	CountryId = 0

	AdressLine1 = ""

	AdressLine2 = ""

	City = ""

	State = ""

	District = ""

	PostalCode = ""

	LocationTypeCode = 0

	Description = ""

	ShippingNotes = ""

	CountriesCountryId = 0