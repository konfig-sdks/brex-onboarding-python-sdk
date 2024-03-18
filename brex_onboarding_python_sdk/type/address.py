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


class RequiredAddress(TypedDict):
    pass

class OptionalAddress(TypedDict, total=False):
    # Address line 1, no PO Box.
    line1: typing.Optional[str]

    # Address line 2 (e.g., apartment, suite, unit, or building).
    line2: typing.Optional[str]

    # City, district, suburb, town, or village.
    city: typing.Optional[str]

    # For US-addressed the 2-letter State abbreviation. For international-addresses the county, providence, or region.
    state: typing.Optional[str]

    # Two-letter country code (ISO 3166-1 alpha-2).
    country: typing.Optional[str]

    # ZIP or postal code.
    postal_code: typing.Optional[str]

    # Phone number.
    phone_number: typing.Optional[str]

class Address(RequiredAddress, OptionalAddress):
    pass
