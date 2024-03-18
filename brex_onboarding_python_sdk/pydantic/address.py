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


class Address(BaseModel):
    # Address line 1, no PO Box.
    line1: typing.Optional[typing.Optional[str]] = Field(None, alias='line1')

    # Address line 2 (e.g., apartment, suite, unit, or building).
    line2: typing.Optional[typing.Optional[str]] = Field(None, alias='line2')

    # City, district, suburb, town, or village.
    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    # For US-addressed the 2-letter State abbreviation. For international-addresses the county, providence, or region.
    state: typing.Optional[typing.Optional[str]] = Field(None, alias='state')

    # Two-letter country code (ISO 3166-1 alpha-2).
    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    # ZIP or postal code.
    postal_code: typing.Optional[typing.Optional[str]] = Field(None, alias='postal_code')

    # Phone number.
    phone_number: typing.Optional[typing.Optional[str]] = Field(None, alias='phone_number')
    class Config:
        arbitrary_types_allowed = True
