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


class Document(BaseModel):
    # This is a presigned S3 link that should be used to attach the document. The maximum size accepted for this document is 50 MB.
    uri: str = Field(alias='uri')

    # Unique identifier for the document.
    id: str = Field(alias='id')
    class Config:
        arbitrary_types_allowed = True
