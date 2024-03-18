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


class CompanyRelationship(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Relationship of this beneficial owner for this company.
    """


    class MetaOapg:
        enum_value_to_name = {
            "FOUNDER": "FOUNDER",
            "EXECUTIVE": "EXECUTIVE",
            "SENIOR_LEADERSHIP": "SENIOR_LEADERSHIP",
            "OTHER": "OTHER",
        }
    
    @schemas.classproperty
    def FOUNDER(cls):
        return cls("FOUNDER")
    
    @schemas.classproperty
    def EXECUTIVE(cls):
        return cls("EXECUTIVE")
    
    @schemas.classproperty
    def SENIOR_LEADERSHIP(cls):
        return cls("SENIOR_LEADERSHIP")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("OTHER")