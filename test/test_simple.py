# coding: utf-8

"""
    Onboarding API

     The onboarding API allows you to refer your customers and personal contacts to Brex. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest

import os
from pprint import pprint
from brex_onboarding_python_sdk import BrexOnboarding

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        brexonboarding = BrexOnboarding(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(brexonboarding)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
