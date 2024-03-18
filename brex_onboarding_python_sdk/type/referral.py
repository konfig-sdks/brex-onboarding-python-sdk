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

from brex_onboarding_python_sdk.type.product import Product
from brex_onboarding_python_sdk.type.referral_status import ReferralStatus

class RequiredReferral(TypedDict):
    # Unique identifier for the referral.
    id: str

    # Signup URL to redirect prospects to complete their onboarding flow.  *Note*: Necessary disclosures must be shown when the prospect clicks on this link. 
    referral_signup_url: str

    # The time at which this referral link expires.
    expires_at: datetime

    status: ReferralStatus

    products: typing.List[Product]

class OptionalReferral(TypedDict, total=False):
    # Customer's email address registered for the Brex application. This field is available only if there's a signup completed. 
    customer_email: typing.Optional[str]

class Referral(RequiredReferral, OptionalReferral):
    pass
