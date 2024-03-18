# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from brex_onboarding_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_REFERRALS = "/v1/referrals"
    V1_REFERRALS_ID = "/v1/referrals/{id}"
    V1_REFERRALS_ID_DOCUMENT_UPLOAD = "/v1/referrals/{id}/document_upload"
