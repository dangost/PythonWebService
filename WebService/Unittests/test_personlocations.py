import unittest
import requests


class PersonLocationsTest(unittest.TestCase):

    json_valid = {"PersonsPersonId": 1,
                           "LocationsLocationsId": 1,
                           "SubAdress": "asdfe",
                           "LocationUsage":  "asdfe",
                           "Notes":  "adf"}

    json_invalid = {"PersonsPersonId": 1,
                           "LocationUsage":  "asdfe",
                           "Notes":  "adf"}


    url = "http://127.0.0.1:5000/api/PersonLocations"

    def test_post_request(self):
        result = requests.post(self.url, json=self.json_valid).text
        self.assertEqual(result, "OK")

    def test_invalid_post_request(self):
        result = requests.post(self.url, json=self.json_invalid).text
        self.assertNotEqual(result, 'OK')

    def test_put_request(self):
        result = requests.put(self.url+"/1", json=self.json_valid).text
        self.assertEqual(result, "OK")

    def test_invalid_put_request(self):
        result = requests.put(self.url+"/2", json=self.json_invalid).text
        self.assertNotEqual(result, "OK")

    def test_delete_request(self):
        result = requests.delete(self.url+"/1").text
        self.assertEqual(result, "OK")

    def test_get_request(self):
        result = requests.get(self.url).status_code
        self.assertEqual(result, 200)

    def test_get_id_request(self):
        result = requests.get(self.url+"/1").status_code
        self.assertEqual(result, 200)

    