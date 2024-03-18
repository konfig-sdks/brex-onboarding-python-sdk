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

from brex_onboarding_python_sdk.pydantic.instruction import Instruction

class Account(BaseModel):
    # Brex Cash management account ID.
    id: str = Field(alias='id')

    created_at: datetime = Field(alias='created_at')

    instructions: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='instructions')
    class Config:
        arbitrary_types_allowed = True
