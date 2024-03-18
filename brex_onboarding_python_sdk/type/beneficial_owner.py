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
from brex_onboarding_python_sdk.type.company_relationship import CompanyRelationship
from brex_onboarding_python_sdk.type.identity_document import IdentityDocument
from brex_onboarding_python_sdk.type.prong import Prong

class RequiredBeneficialOwner(TypedDict):
    # Legal full name.
    legal_name: str

    prong: Prong

class OptionalBeneficialOwner(TypedDict, total=False):
    company_relationship: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Date of birth.
    date_of_birth: typing.Optional[date]

    identity_document: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    address: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class BeneficialOwner(RequiredBeneficialOwner, OptionalBeneficialOwner):
    pass
