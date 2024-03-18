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


IncorporationType = Literal["C_CORP", "S_CORP", "B_CORP", "LLC", "LLP", "SOLE_PROP", "ORG_501C3", "LP"]
