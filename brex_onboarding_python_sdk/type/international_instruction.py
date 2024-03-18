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


class RequiredInternationalInstruction(TypedDict):
    account_type: str

    swift_account_number: str

    swift_bank_number: str

    beneficiary_name: str

    beneficiary_address: str

    bank_name: str

    bank_address: str

    special_instructions: str

class OptionalInternationalInstruction(TypedDict, total=False):
    pass

class InternationalInstruction(RequiredInternationalInstruction, OptionalInternationalInstruction):
    pass
