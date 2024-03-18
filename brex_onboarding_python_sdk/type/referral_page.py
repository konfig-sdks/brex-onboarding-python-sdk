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

from brex_onboarding_python_sdk.type.referral import Referral

class RequiredReferralPage(TypedDict):
    items: typing.List[Referral]

class OptionalReferralPage(TypedDict, total=False):
    next_cursor: typing.Optional[str]

class ReferralPage(RequiredReferralPage, OptionalReferralPage):
    pass
