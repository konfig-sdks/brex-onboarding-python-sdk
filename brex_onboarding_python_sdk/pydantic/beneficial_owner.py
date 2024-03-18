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
from brex_onboarding_python_sdk.pydantic.company_relationship import CompanyRelationship
from brex_onboarding_python_sdk.pydantic.identity_document import IdentityDocument
from brex_onboarding_python_sdk.pydantic.prong import Prong

class BeneficialOwner(BaseModel):
    # Legal full name.
    legal_name: str = Field(alias='legal_name')

    prong: Prong = Field(alias='prong')

    company_relationship: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='company_relationship')

    # Date of birth.
    date_of_birth: typing.Optional[typing.Optional[date]] = Field(None, alias='date_of_birth')

    identity_document: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='identity_document')

    address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='address')
    class Config:
        arbitrary_types_allowed = True
