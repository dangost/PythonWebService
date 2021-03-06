import unittest
import requests


class LocationsTest(unittest.TestCase):

    json_valid = {"CountryId": 12,
                     "AdressLine1": "1asdfff",
                     "AdressLine2":  "asdfdfef",
                     "City":  "asdffef",
                     "State":  "ewrert",
                     "District":  "sdfgfg",
                     "PostalCode":  "sdfefgf",
                     "LocationTypeCode": 4567,
                     "Description": "jfeifjefkdls;a",
                     "ShippingNotes":  "asdjfkl;",
                     "CountriesCountryId": 578}

    json_invalid = {"CountryId": 12,
                     "AdressLine1": "1asdfff",
                     "AdressLine2":  "asdfdfef",
                     "City":  "asdffef",
                     "LocationTypeCode": 4567,
                     "Description": "jfeifjefkdls;a",
                     "ShippingNotes":  "asdjfkl;",
                     "CountriesCountryId": 578}


    url = "http://127.0.0.1:5000/api/Locations"

    def test_post_request(self):
        result = requests.post(self.url, json=self.json_valid).text
        self.assertEqual(result, "OK")

    def test_invalid_post_request(self):
        result = requests.post(self.url, json=self.json_invalid).text
        self.assertNotEqual(result, 'OK')

    def test_put_request(self):
        result = requests.put(self.url+"/2", json=self.json_valid).text
        self.assertEqual(result, "OK")

    def test_invalid_put_request(self):
        result = requests.put(self.url+"/2", json=self.json_invalid).text
        self.assertNotEqual(result, "OK")

    def test_delete_request(self):
        result = requests.delete(self.url+"/2").text
        self.assertEqual(result, "OK")

    def test_get_request(self):
        result = requests.get(self.url).status_code
        self.assertEqual(result, 200)

    def test_get_id_request(self):
        result = requests.get(self.url+"/1").status_code
        self.assertEqual(result, 200)

    