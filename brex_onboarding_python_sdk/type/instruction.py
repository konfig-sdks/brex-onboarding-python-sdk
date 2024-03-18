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

from brex_onboarding_python_sdk.type.domestic_instruction import DomesticInstruction
from brex_onboarding_python_sdk.type.international_instruction import InternationalInstruction

class RequiredInstruction(TypedDict):
    domestic: DomesticInstruction

    international: InternationalInstruction

class OptionalInstruction(TypedDict, total=False):
    pass

class Instruction(RequiredInstruction, OptionalInstruction):
    pass
