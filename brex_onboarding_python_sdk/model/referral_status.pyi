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


class ReferralStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Status of the referral. `UNCLAIMED` or `EXPIRED` unless the customer completes signup. Customers are attributed once `ACTIVE` until the account is `CLOSED`.
    """
    
    @schemas.classproperty
    def UNCLAIMED(cls):
        return cls("UNCLAIMED")
    
    @schemas.classproperty
    def EXPIRED(cls):
        return cls("EXPIRED")
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("ACTIVE")
    
    @schemas.classproperty
    def CLOSED(cls):
        return cls("CLOSED")