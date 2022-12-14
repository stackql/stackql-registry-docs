---
title: targeting_options
hide_title: false
hide_table_of_contents: false
keywords:
  - targeting_options
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>targeting_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.targeting_options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this targeting option. |
| `contentOutstreamPositionDetails` | `object` | Represents a targetable content outstream position, which could be used by display and video ads. This will be populated in the content_outstream_position_details field when targeting_type is `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION`. |
| `exchangeDetails` | `object` | Represents a targetable exchange. This will be populated in the exchange_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_EXCHANGE`. |
| `deviceMakeModelDetails` | `object` | Represents a targetable device make and model. This will be populated in the device_make_model_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_DEVICE_MAKE_MODEL`. |
| `businessChainDetails` | `object` | Represents a targetable business chain within a geo region. This will be populated in the business_chain_details field when targeting_type is `TARGETING_TYPE_BUSINESS_CHAIN`. |
| `environmentDetails` | `object` | Represents a targetable environment. This will be populated in the environment_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_ENVIRONMENT`. |
| `categoryDetails` | `object` | Represents a targetable category. This will be populated in the category_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_CATEGORY`. |
| `sensitiveCategoryDetails` | `object` | Represents a targetable sensitive category. This will be populated in the sensitive_category_details field of the TargetingOption when targeting_type is `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION`. |
| `deviceTypeDetails` | `object` | Represents a targetable device type. This will be populated in the device_type_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_DEVICE_TYPE`. |
| `audioContentTypeDetails` | `object` | Represents a targetable audio content type. This will be populated in the audio_content_type_details field when targeting_type is `TARGETING_TYPE_AUDIO_CONTENT_TYPE`. |
| `omidDetails` | `object` | Represents a targetable Open Measurement enabled inventory type. This will be populated in the omid_details field when targeting_type is `TARGETING_TYPE_OMID`. |
| `appCategoryDetails` | `object` | Represents a targetable collection of apps. A collection lets you target dynamic groups of related apps that are maintained by the platform, for example `All Apps/Google Play/Games`. This will be populated in the app_category_details field when targeting_type is `TARGETING_TYPE_APP_CATEGORY`. |
| `parentalStatusDetails` | `object` | Represents a targetable parental status. This will be populated in the parental_status_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_PARENTAL_STATUS`. |
| `householdIncomeDetails` | `object` | Represents a targetable household income. This will be populated in the household_income_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_HOUSEHOLD_INCOME`. |
| `contentStreamTypeDetails` | `object` | Represents a targetable content stream type. This will be populated in the content_stream_type_details field when targeting_type is `TARGETING_TYPE_CONTENT_STREAM_TYPE`. |
| `onScreenPositionDetails` | `object` | Represents a targetable on screen position, which could be used by display and video ads. This will be populated in the on_screen_position_details field when targeting_type is `TARGETING_TYPE_ON_SCREEN_POSITION`. |
| `contentInstreamPositionDetails` | `object` | Represents a targetable content instream position, which could be used by video and audio ads. This will be populated in the content_instream_position_details field when targeting_type is `TARGETING_TYPE_CONTENT_INSTREAM_POSITION`. |
| `digitalContentLabelDetails` | `object` | Represents a targetable digital content label rating tier. This will be populated in the digital_content_label_details field of the TargetingOption when targeting_type is `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION`. |
| `viewabilityDetails` | `object` | Represents a targetable viewability. This will be populated in the viewability_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_VIEWABILITY`. |
| `operatingSystemDetails` | `object` | Represents a targetable operating system. This will be populated in the operating_system_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_OPERATING_SYSTEM`. |
| `genderDetails` | `object` | Represents a targetable gender. This will be populated in the gender_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_GENDER`. |
| `geoRegionDetails` | `object` | Represents a targetable geographic region. This will be populated in the geo_region_details field when targeting_type is `TARGETING_TYPE_GEO_REGION`. |
| `subExchangeDetails` | `object` | Represents a targetable sub-exchange. This will be populated in the sub_exchange_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_SUB_EXCHANGE`. |
| `authorizedSellerStatusDetails` | `object` | Represents a targetable authorized seller status. This will be populated in the authorized_seller_status_details field when targeting_type is `TARGETING_TYPE_AUTHORIZED_SELLER_STATUS`. |
| `nativeContentPositionDetails` | `object` | Represents a targetable native content position. This will be populated in the native_content_position_details field when targeting_type is `TARGETING_TYPE_NATIVE_CONTENT_POSITION`. |
| `browserDetails` | `object` | Represents a targetable browser. This will be populated in the browser_details field when targeting_type is `TARGETING_TYPE_BROWSER`. |
| `userRewardedContentDetails` | `object` | Represents a targetable user rewarded content status for video ads only. This will be populated in the user_rewarded_content_details field when targeting_type is `TARGETING_TYPE_USER_REWARDED_CONTENT`. |
| `ageRangeDetails` | `object` | Represents a targetable age range. This will be populated in the age_range_details field when targeting_type is `TARGETING_TYPE_AGE_RANGE`. |
| `videoPlayerSizeDetails` | `object` | Represents a targetable video player size. This will be populated in the video_player_size_details field when targeting_type is `TARGETING_TYPE_VIDEO_PLAYER_SIZE`. |
| `contentGenreDetails` | `object` | Represents a targetable content genre. This will be populated in the content_genre_details field when targeting_type is `TARGETING_TYPE_CONTENT_GENRE`. |
| `contentDurationDetails` | `object` | Represents a targetable content duration. This will be populated in the content_duration_details field when targeting_type is `TARGETING_TYPE_CONTENT_DURATION`. |
| `languageDetails` | `object` | Represents a targetable language. This will be populated in the language_details field when targeting_type is `TARGETING_TYPE_LANGUAGE`. |
| `poiDetails` | `object` | Represents a targetable point of interest(POI). This will be populated in the poi_details field when targeting_type is `TARGETING_TYPE_POI`. |
| `targetingOptionId` | `string` | Output only. A unique identifier for this targeting option. The tuple &#123;`targeting_type`, `targeting_option_id`&#125; will be unique. |
| `targetingType` | `string` | Output only. The type of this targeting option. |
| `carrierAndIspDetails` | `object` | Represents a targetable carrier or ISP. This will be populated in the carrier_and_isp_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_CARRIER_AND_ISP`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `targetingTypes_targetingOptions_get` | `SELECT` | `targetingOptionsId, targetingTypesId` | Gets a single targeting option. |
| `targetingTypes_targetingOptions_list` | `SELECT` | `targetingTypesId` | Lists targeting options of a given type. |
| `targetingTypes_targetingOptions_search` | `EXEC` | `targetingTypesId` | Searches for targeting options of a given type based on the given search terms. |
