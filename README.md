<div align="left">

[![Visit Brex](./header.png)](https://brex.com)

# Brex<a id="brex"></a>


The onboarding API allows you to refer your customers and personal contacts to Brex.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`brexonboarding.referrals.create_new_referral`](#brexonboardingreferralscreate_new_referral)
  * [`brexonboarding.referrals.get_by_id`](#brexonboardingreferralsget_by_id)
  * [`brexonboarding.referrals.get_list`](#brexonboardingreferralsget_list)
  * [`brexonboarding.referrals.upload_document`](#brexonboardingreferralsupload_document)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Brex&serviceName=Onboarding&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from brex_onboarding_python_sdk import BrexOnboarding, ApiException

brexonboarding = BrexOnboarding(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Creates a referral
    create_new_referral_response = brexonboarding.referrals.create_new_referral(
        referral_code="string_example",
        applicant={
            "last_name": "last_name_example",
            "first_name": "first_name_example",
            "email": "email_example",
        },
        business=None,
        contact_preference=None,
    )
    print(create_new_referral_response)
except ApiException as e:
    print("Exception when calling ReferralsApi.create_new_referral: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from brex_onboarding_python_sdk import BrexOnboarding, ApiException

brexonboarding = BrexOnboarding(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Creates a referral
        create_new_referral_response = (
            await brexonboarding.referrals.acreate_new_referral(
                referral_code="string_example",
                applicant={
                    "last_name": "last_name_example",
                    "first_name": "first_name_example",
                    "email": "email_example",
                },
                business=None,
                contact_preference=None,
            )
        )
        print(create_new_referral_response)
    except ApiException as e:
        print("Exception when calling ReferralsApi.create_new_referral: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from brex_onboarding_python_sdk import BrexOnboarding, ApiException

brexonboarding = BrexOnboarding(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Creates a referral
    create_new_referral_response = brexonboarding.referrals.raw.create_new_referral(
        referral_code="string_example",
        applicant={
            "last_name": "last_name_example",
            "first_name": "first_name_example",
            "email": "email_example",
        },
        business=None,
        contact_preference=None,
    )
    pprint(create_new_referral_response.body)
    pprint(create_new_referral_response.body["id"])
    pprint(create_new_referral_response.body["referral_signup_url"])
    pprint(create_new_referral_response.body["expires_at"])
    pprint(create_new_referral_response.body["status"])
    pprint(create_new_referral_response.body["products"])
    pprint(create_new_referral_response.body["customer_email"])
    pprint(create_new_referral_response.headers)
    pprint(create_new_referral_response.status)
    pprint(create_new_referral_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ReferralsApi.create_new_referral: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `brexonboarding.referrals.create_new_referral`<a id="brexonboardingreferralscreate_new_referral"></a>

This creates new referrals. The response will contain an identifier and a unique personalized link to an application flow. Many fields are optional and when they're provided they'll prefill the application flow for Brex.  You should handle and store these references securely as they contain sensitive information about the referral.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_referral_response = brexonboarding.referrals.create_new_referral(
    referral_code="string_example",
    applicant={
        "last_name": "last_name_example",
        "first_name": "first_name_example",
        "email": "email_example",
    },
    business=None,
    contact_preference=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### referral_code: `str`<a id="referral_code-str"></a>

Referral code that attributes credit to you if the prospect signs up for a Brex account.

##### applicant: [`Applicant`](./brex_onboarding_python_sdk/type/applicant.py)<a id="applicant-applicantbrex_onboarding_python_sdktypeapplicantpy"></a>


##### business: Union[`Business`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_onboarding_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="business-unionbusiness-unionbool-date-datetime-dict-float-int-list-str-nonebrex_onboarding_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### contact_preference: Union[[`ContactPreference`](./brex_onboarding_python_sdk/type/contact_preference.py), [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_onboarding_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="contact_preference-unioncontactpreferencebrex_onboarding_python_sdktypecontact_preferencepy-unionbool-date-datetime-dict-float-int-list-str-nonebrex_onboarding_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateReferralRequest`](./brex_onboarding_python_sdk/type/create_referral_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Referral`](./brex_onboarding_python_sdk/pydantic/referral.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/referrals` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexonboarding.referrals.get_by_id`<a id="brexonboardingreferralsget_by_id"></a>

Returns a referral object by ID if it exists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = brexonboarding.referrals.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Referral`](./brex_onboarding_python_sdk/pydantic/referral.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/referrals/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexonboarding.referrals.get_list`<a id="brexonboardingreferralsget_list"></a>

Returns referrals created.
*Note*: This doesn't include referrals that have expired.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = brexonboarding.referrals.get_list(
    cursor="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReferralPage`](./brex_onboarding_python_sdk/pydantic/referral_page.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/referrals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexonboarding.referrals.upload_document`<a id="brexonboardingreferralsupload_document"></a>


The `uri` will be a presigned S3 URL allowing you to upload the referral doc securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will use this to prefill the application.

Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this presigned S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_document_response = brexonboarding.referrals.upload_document(
    type="ARTICLES_OF_INCORPORATION",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: [`DocumentType`](./brex_onboarding_python_sdk/type/document_type.py)<a id="type-documenttypebrex_onboarding_python_sdktypedocument_typepy"></a>

##### id: `str`<a id="id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDocumentRequest`](./brex_onboarding_python_sdk/type/create_document_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./brex_onboarding_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/referrals/{id}/document_upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
