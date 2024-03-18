import typing_extensions

from brex_onboarding_python_sdk.apis.tags import TagValues
from brex_onboarding_python_sdk.apis.tags.referrals_api import ReferralsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.REFERRALS: ReferralsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.REFERRALS: ReferralsApi,
    }
)
