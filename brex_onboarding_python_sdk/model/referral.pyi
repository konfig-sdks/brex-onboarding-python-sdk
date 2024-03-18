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


class Referral(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "referral_signup_url",
            "expires_at",
            "id",
            "products",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            referral_signup_url = schemas.StrSchema
            expires_at = schemas.DateTimeSchema
        
            @staticmethod
            def status() -> typing.Type['ReferralStatus']:
                return ReferralStatus
            
            
            class products(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Product']:
                        return Product
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Product'], typing.List['Product']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'products':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Product':
                    return super().__getitem__(i)
            
            
            class customer_email(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'email'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customer_email':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "referral_signup_url": referral_signup_url,
                "expires_at": expires_at,
                "status": status,
                "products": products,
                "customer_email": customer_email,
            }
    
    referral_signup_url: MetaOapg.properties.referral_signup_url
    expires_at: MetaOapg.properties.expires_at
    id: MetaOapg.properties.id
    products: MetaOapg.properties.products
    status: 'ReferralStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referral_signup_url"]) -> MetaOapg.properties.referral_signup_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_at"]) -> MetaOapg.properties.expires_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ReferralStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["products"]) -> MetaOapg.properties.products: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_email"]) -> MetaOapg.properties.customer_email: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "referral_signup_url", "expires_at", "status", "products", "customer_email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referral_signup_url"]) -> MetaOapg.properties.referral_signup_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_at"]) -> MetaOapg.properties.expires_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'ReferralStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["products"]) -> MetaOapg.properties.products: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_email"]) -> typing.Union[MetaOapg.properties.customer_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "referral_signup_url", "expires_at", "status", "products", "customer_email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        referral_signup_url: typing.Union[MetaOapg.properties.referral_signup_url, str, ],
        expires_at: typing.Union[MetaOapg.properties.expires_at, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        products: typing.Union[MetaOapg.properties.products, list, tuple, ],
        status: 'ReferralStatus',
        customer_email: typing.Union[MetaOapg.properties.customer_email, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Referral':
        return super().__new__(
            cls,
            *args,
            referral_signup_url=referral_signup_url,
            expires_at=expires_at,
            id=id,
            products=products,
            status=status,
            customer_email=customer_email,
            _configuration=_configuration,
            **kwargs,
        )

from brex_onboarding_python_sdk.model.product import Product
from brex_onboarding_python_sdk.model.referral_status import ReferralStatus