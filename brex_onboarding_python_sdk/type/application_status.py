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


ApplicationStatus = Literal["NO_ACCOUNT", "ACTIVE", "NOT_SUBMITTED", "INFORMATION_PENDING", "MANUAL_REVIEW", "PROCESSING", "REJECTED", "CLOSED"]
