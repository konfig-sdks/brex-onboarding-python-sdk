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

from brex_onboarding_python_sdk.type.applicant import Applicant
from brex_onboarding_python_sdk.type.business import Business
from brex_onboarding_python_sdk.type.contact_preference import ContactPreference

class RequiredCreateReferralRequest(TypedDict):
    # Referral code that attributes credit to you if the prospect signs up for a Brex account.
    referral_code: str

    applicant: Applicant

class OptionalCreateReferralRequest(TypedDict, total=False):
    business: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    contact_preference: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class CreateReferralRequest(RequiredCreateReferralRequest, OptionalCreateReferralRequest):
    pass
