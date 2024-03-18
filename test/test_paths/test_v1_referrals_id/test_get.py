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
from brex_onboarding_python_sdk.paths.v1_referrals_id import get
from brex_onboarding_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ReferralsId(ApiTestMixin, unittest.TestCase):
    """
    V1ReferralsId unit test stubs
        Gets a referral by ID
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
