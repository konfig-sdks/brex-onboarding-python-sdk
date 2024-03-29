# coding: utf-8

"""
    Onboarding API

     The onboarding API allows you to refer your customers and personal contacts to Brex. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from brex_onboarding_python_sdk import schemas  # noqa: F401


class DocumentType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Type of document being submitted. Allowable types:
- ARTICLES_OF_INCORPORATION
- IRS_EIN_CONFIRMATION (IRS CP 575 or 147C form)
- IRS_EIN_APPLICATION (IRS SS4 form)
- CERTIFICATE_GOOD_STANDING

    """
    
    @schemas.classproperty
    def ARTICLES_OF_INCORPORATION(cls):
        return cls("ARTICLES_OF_INCORPORATION")
    
    @schemas.classproperty
    def IRS_EIN_CONFIRMATION(cls):
        return cls("IRS_EIN_CONFIRMATION")
    
    @schemas.classproperty
    def IRS_EIN_APPLICATION(cls):
        return cls("IRS_EIN_APPLICATION")
    
    @schemas.classproperty
    def CERTIFICATE_GOOD_STANDING(cls):
        return cls("CERTIFICATE_GOOD_STANDING")
