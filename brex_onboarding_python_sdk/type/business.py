# coding: utf-8

"""
    Onboarding API

     The onboarding API allows you to refer your customers and personal contacts to Brex. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from brex_onboarding_python_sdk.type.address import Address
from brex_onboarding_python_sdk.type.beneficial_owner import BeneficialOwner
from brex_onboarding_python_sdk.type.incorporation_type import IncorporationType

class RequiredBusiness(TypedDict):
    pass

class OptionalBusiness(TypedDict, total=False):
    # Company legal name.
    legal_name: typing.Optional[str]

    incorporation_type: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Company Employer Identification Number(EIN).
    employer_identification_number: typing.Optional[str]

    # Business website (or link to ecommerce store for sellers).
    website_url: typing.Optional[str]

    # Brief description of the business activity.
    activity_description: typing.Optional[str]

    address: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # List of beneficial owners of the company
    beneficial_owners: typing.Optional[typing.List[BeneficialOwner]]

    alternate_address: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Business(RequiredBusiness, OptionalBusiness):
    pass
