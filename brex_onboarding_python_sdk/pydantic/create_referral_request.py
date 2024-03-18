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

from brex_onboarding_python_sdk.pydantic.applicant import Applicant
from brex_onboarding_python_sdk.pydantic.business import Business
from brex_onboarding_python_sdk.pydantic.contact_preference import ContactPreference

class CreateReferralRequest(BaseModel):
    # Referral code that attributes credit to you if the prospect signs up for a Brex account.
    referral_code: str = Field(alias='referral_code')

    applicant: Applicant = Field(alias='applicant')

    business: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='business')

    contact_preference: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='contact_preference')
    class Config:
        arbitrary_types_allowed = True
