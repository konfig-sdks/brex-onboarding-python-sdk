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
from pydantic import BaseModel, Field, RootModel

from brex_onboarding_python_sdk.pydantic.product import Product
from brex_onboarding_python_sdk.pydantic.referral_status import ReferralStatus

class Referral(BaseModel):
    # Unique identifier for the referral.
    id: str = Field(alias='id')

    # Signup URL to redirect prospects to complete their onboarding flow.  *Note*: Necessary disclosures must be shown when the prospect clicks on this link. 
    referral_signup_url: str = Field(alias='referral_signup_url')

    # The time at which this referral link expires.
    expires_at: datetime = Field(alias='expires_at')

    status: ReferralStatus = Field(alias='status')

    products: typing.List[Product] = Field(alias='products')

    # Customer's email address registered for the Brex application. This field is available only if there's a signup completed. 
    customer_email: typing.Optional[typing.Optional[str]] = Field(None, alias='customer_email')
    class Config:
        arbitrary_types_allowed = True
