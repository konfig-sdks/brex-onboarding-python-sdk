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

from brex_onboarding_python_sdk.pydantic.address import Address
from brex_onboarding_python_sdk.pydantic.beneficial_owner import BeneficialOwner
from brex_onboarding_python_sdk.pydantic.incorporation_type import IncorporationType

class Business(BaseModel):
    # Company legal name.
    legal_name: typing.Optional[typing.Optional[str]] = Field(None, alias='legal_name')

    incorporation_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='incorporation_type')

    # Company Employer Identification Number(EIN).
    employer_identification_number: typing.Optional[typing.Optional[str]] = Field(None, alias='employer_identification_number')

    # Business website (or link to ecommerce store for sellers).
    website_url: typing.Optional[typing.Optional[str]] = Field(None, alias='website_url')

    # Brief description of the business activity.
    activity_description: typing.Optional[typing.Optional[str]] = Field(None, alias='activity_description')

    address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='address')

    # List of beneficial owners of the company
    beneficial_owners: typing.Optional[typing.Optional[typing.List[BeneficialOwner]]] = Field(None, alias='beneficial_owners')

    alternate_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='alternate_address')
    class Config:
        arbitrary_types_allowed = True
