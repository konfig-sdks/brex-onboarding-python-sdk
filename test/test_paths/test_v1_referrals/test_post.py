# coding: utf-8

"""
    Onboarding API

     The onboarding API allows you to refer your customers and personal contacts to Brex. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest
from unittest.mock import patch

import urllib3

import brex_onboarding_python_sdk
from brex_onboarding_python_sdk.paths.v1_referrals import post
from brex_onboarding_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1Referrals(ApiTestMixin, unittest.TestCase):
    """
    V1Referrals unit test stubs
        Creates a referral
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
