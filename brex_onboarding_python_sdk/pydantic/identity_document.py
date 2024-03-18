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

from brex_onboarding_python_sdk.pydantic.identity_document_type import IdentityDocumentType

class IdentityDocument(BaseModel):
    # Country where the identity document was issued.
    country: str = Field(alias='country')

    type: IdentityDocumentType = Field(alias='type')

    # US SSN or passport number.
    number: str = Field(alias='number')
    class Config:
        arbitrary_types_allowed = True
