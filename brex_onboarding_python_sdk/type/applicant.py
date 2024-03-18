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


class RequiredApplicant(TypedDict):
    # Last name of the applying customer.
    last_name: str

    # First name of the applying customer.
    first_name: str

    # Business email of the applying customer.
    email: str

class OptionalApplicant(TypedDict, total=False):
    pass

class Applicant(RequiredApplicant, OptionalApplicant):
    pass
