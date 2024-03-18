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


class Applicant(BaseModel):
    # Last name of the applying customer.
    last_name: str = Field(alias='last_name')

    # First name of the applying customer.
    first_name: str = Field(alias='first_name')

    # Business email of the applying customer.
    email: str = Field(alias='email')
    class Config:
        arbitrary_types_allowed = True
