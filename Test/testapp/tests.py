import json
from django.test import TestCase

# Create your tests here.

from django.test import Client
from django.conf import settings
from rest_framework.test import APIClient
from testapp.models import *


class Views(TestCase):

    def setUp(self):
        print('Setting up the test environment for distance calculator testapp: views...')
        Shop.objects.create(name="test1", 
                            owner='owner1', 
                            latitude=32.74448208110986, 
                            longitude=74.83270256828057)
        

        Shop.objects.create(name="test2", 
                            owner='owner2', 
                            latitude=32.73199325121623,
                            longitude=74.83754393673517)



    def test_SubmitShopFormAPI(self):
        print('Testing test_SubmitShopFormAPI...')

        client = APIClient()

        # test case 1: a shop nearby to test1 shop created above should return test1 object
        # This will fetch first object which is less than 0.5 km from the below lat and long
        json_string = json.dumps({
            "latitude": 32.74506332016356,
            "longitude": 74.8343579053311,
            "distance": 0.5,
        })


        request = client.post('/submit-shop-form',
                              json_string,
                              content_type='application/json')

        response = request.data
        self.assertEqual(response["status"], 200)
        self.assertEqual(len(response['data']), 1)
        self.assertEqual(response['data'][0]["name"], "test1")

        # test case 2: similar to test case 1 but distance is increased to 1 km.
        # This will fetch both the shops created above because both are less than 1 km
        # w.r.t below lat long
        json_string = json.dumps({
            "latitude": 32.74506332016356,
            "longitude": 74.8343579053311,
            "distance": 1,
        })


        request = client.post('/submit-shop-form',
                              json_string,
                              content_type='application/json')

        response = request.data
        self.assertEqual(response["status"], 200)
        self.assertEqual(len(response['data']), 2)
        self.assertEqual(response['data'][0]["name"], "test1")
        self.assertEqual(response['data'][1]["name"], "test2")

        # test case 3: No data will be returned because the lat long used below are far off
        # w.r.t the above shops and also the distance is less
        json_string = json.dumps({
            "latitude": 33.74506332016356,
            "longitude": 75.8343579053311,
            "distance": 100,
        })


        request = client.post('/submit-shop-form',
                              json_string,
                              content_type='application/json')

        response = request.data
        self.assertEqual(response["status"], 200)
        self.assertEqual(len(response['data']), 0)

    