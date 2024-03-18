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


class RequiredDomesticInstruction(TypedDict):
    account_type: str

    bank_account_number: str

    bank_routing_number: str

    beneficiary_name: str

    beneficiary_address: str

    bank_name: str

    bank_address: str

class OptionalDomesticInstruction(TypedDict, total=False):
    pass

class DomesticInstruction(RequiredDomesticInstruction, OptionalDomesticInstruction):
    pass
