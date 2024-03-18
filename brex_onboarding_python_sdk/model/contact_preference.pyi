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


class ContactPreference(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    When set to `EMAIL_OUTBOUND`, Brex will email the referred prospective customer directly to prompt them to create their account rather than rely on you to direct them to claim the account. If not provided, you are responsible for contacting the prospect and the value defaults to `NO_OUTBOUND`.
    """
    
    @schemas.classproperty
    def NO_OUTBOUND(cls):
        return cls("NO_OUTBOUND")
    
    @schemas.classproperty
    def EMAIL_OUTBOUND(cls):
        return cls("EMAIL_OUTBOUND")
