import typing_extensions

from brex_onboarding_python_sdk.paths import PathValues
from brex_onboarding_python_sdk.apis.paths.v1_referrals import V1Referrals
from brex_onboarding_python_sdk.apis.paths.v1_referrals_id import V1ReferralsId
from brex_onboarding_python_sdk.apis.paths.v1_referrals_id_document_upload import V1ReferralsIdDocumentUpload

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_REFERRALS: V1Referrals,
        PathValues.V1_REFERRALS_ID: V1ReferralsId,
        PathValues.V1_REFERRALS_ID_DOCUMENT_UPLOAD: V1ReferralsIdDocumentUpload,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_REFERRALS: V1Referrals,
        PathValues.V1_REFERRALS_ID: V1ReferralsId,
        PathValues.V1_REFERRALS_ID_DOCUMENT_UPLOAD: V1ReferralsIdDocumentUpload,
    }
)
