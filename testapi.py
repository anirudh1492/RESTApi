import os
import json
from urllib.request import urlopen
import unittest
from ZapApi import app
import requests

class testget(unittest.TestCase):
    def setUp(self):
        self.ApiUrl = "http://127.0.0.1:5000/GetRestraunt?Name=California"

    def testrestraunt(self):
        #testurl = (ApiUrl+"?Name=California'")
       #response=urlopen(testurl)
        response2 = requests.get(ApiUrl)
        html = response.read()
        self.assertTrue("Bawarchi,California,CAB01" in html)

if __name__ == '__main__':
    unittest.main()