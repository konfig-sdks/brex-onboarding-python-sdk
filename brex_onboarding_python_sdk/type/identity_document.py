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

from brex_onboarding_python_sdk.type.identity_document_type import IdentityDocumentType

class RequiredIdentityDocument(TypedDict):
    # Country where the identity document was issued.
    country: str

    type: IdentityDocumentType

    # US SSN or passport number.
    number: str

class OptionalIdentityDocument(TypedDict, total=False):
    pass

class IdentityDocument(RequiredIdentityDocument, OptionalIdentityDocument):
    pass
