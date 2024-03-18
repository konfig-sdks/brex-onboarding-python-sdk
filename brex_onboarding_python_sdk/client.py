# coding: utf-8
"""
    Onboarding API

     The onboarding API allows you to refer your customers and personal contacts to Brex. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import typing
import inspect
from datetime import date, datetime
from brex_onboarding_python_sdk.client_custom import ClientCustom
from brex_onboarding_python_sdk.configuration import Configuration
from brex_onboarding_python_sdk.api_client import ApiClient
from brex_onboarding_python_sdk.type_util import copy_signature
from brex_onboarding_python_sdk.apis.tags.referrals_api import ReferralsApi



class BrexOnboarding(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.referrals: ReferralsApi = ReferralsApi(api_client)
