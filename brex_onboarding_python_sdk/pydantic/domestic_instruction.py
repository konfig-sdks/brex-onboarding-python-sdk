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


class DomesticInstruction(BaseModel):
    account_type: str = Field(alias='account_type')

    bank_account_number: str = Field(alias='bank_account_number')

    bank_routing_number: str = Field(alias='bank_routing_number')

    beneficiary_name: str = Field(alias='beneficiary_name')

    beneficiary_address: str = Field(alias='beneficiary_address')

    bank_name: str = Field(alias='bank_name')

    bank_address: str = Field(alias='bank_address')
    class Config:
        arbitrary_types_allowed = True
