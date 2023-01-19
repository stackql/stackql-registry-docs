---
title: assigned_targeting_options
hide_title: false
hide_table_of_contents: false
keywords:
  - assigned_targeting_options
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
<tr><td><b>Name</b></td><td><code>assigned_targeting_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.assigned_targeting_options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this assigned targeting option. |
| `inventorySourceGroupDetails` | `object` | Targeting details for inventory source group. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_INVENTORY_SOURCE_GROUP`. |
| `businessChainDetails` | `object` | Details for assigned Business chain targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_BUSINESS_CHAIN`. |
| `contentOutstreamPositionDetails` | `object` | Assigned content outstream position targeting option details. This will be populated in the content_outstream_position_details field when targeting_type is `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION`. |
| `householdIncomeDetails` | `object` | Details for assigned household income targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_HOUSEHOLD_INCOME`. |
| `languageDetails` | `object` | Details for assigned language targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_LANGUAGE`. |
| `inheritance` | `string` | Output only. The inheritance status of the assigned targeting option. |
| `nativeContentPositionDetails` | `object` | Details for native content position assigned targeting option. This will be populated in the native_content_position_details field when targeting_type is `TARGETING_TYPE_NATIVE_CONTENT_POSITION`. Explicitly targeting all options is not supported. Remove all native content position targeting options to achieve this effect. |
| `contentDurationDetails` | `object` | Details for content duration assigned targeting option. This will be populated in the content_duration_details field when targeting_type is `TARGETING_TYPE_CONTENT_DURATION`. Explicitly targeting all options is not supported. Remove all content duration targeting options to achieve this effect. |
| `regionalLocationListDetails` | `object` | Targeting details for regional location list. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_REGIONAL_LOCATION_LIST`. |
| `thirdPartyVerifierDetails` | `object` | Assigned third party verifier targeting option details. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_THIRD_PARTY_VERIFIER`. |
| `categoryDetails` | `object` | Assigned category targeting option details. This will be populated in the category_details field when targeting_type is `TARGETING_TYPE_CATEGORY`. |
| `userRewardedContentDetails` | `object` | User rewarded content targeting option details. This will be populated in the user_rewarded_content_details field when targeting_type is `TARGETING_TYPE_USER_REWARDED_CONTENT`. |
| `authorizedSellerStatusDetails` | `object` | Represents an assigned authorized seller status. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_AUTHORIZED_SELLER_STATUS`. |
| `ageRangeDetails` | `object` | Represents a targetable age range. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_AGE_RANGE`. |
| `environmentDetails` | `object` | Assigned environment targeting option details. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_ENVIRONMENT`. |
| `contentInstreamPositionDetails` | `object` | Assigned content instream position targeting option details. This will be populated in the content_instream_position_details field when targeting_type is `TARGETING_TYPE_CONTENT_INSTREAM_POSITION`. |
| `sensitiveCategoryExclusionDetails` | `object` | Targeting details for sensitive category. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION`. |
| `contentStreamTypeDetails` | `object` | Details for content stream type assigned targeting option. This will be populated in the content_stream_type_details field when targeting_type is `TARGETING_TYPE_CONTENT_STREAM_TYPE`. Explicitly targeting all options is not supported. Remove all content stream type targeting options to achieve this effect. |
| `digitalContentLabelExclusionDetails` | `object` | Targeting details for digital content label. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION`. |
| `audienceGroupDetails` | `object` | Assigned audience group targeting option details. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_AUDIENCE_GROUP`. The relation between each group is UNION, except for excluded_first_and_third_party_audience_group and excluded_google_audience_group, of which COMPLEMENT is used as an INTERSECTION with other groups. |
| `contentGenreDetails` | `object` | Details for content genre assigned targeting option. This will be populated in the content_genre_details field when targeting_type is `TARGETING_TYPE_CONTENT_GENRE`. Explicitly targeting all options is not supported. Remove all content genre targeting options to achieve this effect. |
| `negativeKeywordListDetails` | `object` | Targeting details for negative keyword list. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_NEGATIVE_KEYWORD_LIST`. |
| `assignedTargetingOptionId` | `string` | Output only. The unique ID of the assigned targeting option. The ID is only unique within a given resource and targeting type. It may be reused in other contexts. |
| `parentalStatusDetails` | `object` | Details for assigned parental status targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_PARENTAL_STATUS`. |
| `appDetails` | `object` | Details for assigned app targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_APP`. |
| `videoPlayerSizeDetails` | `object` | Video player size targeting option details. This will be populated in the video_player_size_details field when targeting_type is `TARGETING_TYPE_VIDEO_PLAYER_SIZE`. Explicitly targeting all options is not supported. Remove all video player size targeting options to achieve this effect. |
| `geoRegionDetails` | `object` | Details for assigned geographic region targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_GEO_REGION`. |
| `appCategoryDetails` | `object` | Details for assigned app category targeting option. This will be populated in the app_category_details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_APP_CATEGORY`. |
| `carrierAndIspDetails` | `object` | Details for assigned carrier and ISP targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_CARRIER_AND_ISP`. |
| `deviceMakeModelDetails` | `object` | Assigned device make and model targeting option details. This will be populated in the device_make_model_details field when targeting_type is `TARGETING_TYPE_DEVICE_MAKE_MODEL`. |
| `genderDetails` | `object` | Details for assigned gender targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_GENDER`. |
| `inventorySourceDetails` | `object` | Targeting details for inventory source. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_INVENTORY_SOURCE`. |
| `urlDetails` | `object` | Details for assigned URL targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_URL`. |
| `onScreenPositionDetails` | `object` | On screen position targeting option details. This will be populated in the on_screen_position_details field when targeting_type is `TARGETING_TYPE_ON_SCREEN_POSITION`. |
| `proximityLocationListDetails` | `object` | Targeting details for proximity location list. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_PROXIMITY_LOCATION_LIST`. |
| `browserDetails` | `object` | Details for assigned browser targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_BROWSER`. |
| `subExchangeDetails` | `object` | Details for assigned sub-exchange targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_SUB_EXCHANGE`. |
| `operatingSystemDetails` | `object` | Assigned operating system targeting option details. This will be populated in the operating_system_details field when targeting_type is `TARGETING_TYPE_OPERATING_SYSTEM`. |
| `deviceTypeDetails` | `object` | Targeting details for device type. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_DEVICE_TYPE`. |
| `keywordDetails` | `object` | Details for assigned keyword targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_KEYWORD`. |
| `audioContentTypeDetails` | `object` | Details for audio content type assigned targeting option. This will be populated in the audio_content_type_details field when targeting_type is `TARGETING_TYPE_AUDIO_CONTENT_TYPE`. Explicitly targeting all options is not supported. Remove all audio content type targeting options to achieve this effect. |
| `channelDetails` | `object` | Details for assigned channel targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_CHANNEL`. |
| `exchangeDetails` | `object` | Details for assigned exchange targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_EXCHANGE`. |
| `omidDetails` | `object` | Represents a targetable Open Measurement enabled inventory type. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_OMID`. |
| `dayAndTimeDetails` | `object` | Representation of a segment of time defined on a specific day of the week and with a start and end time. The time represented by `start_hour` must be before the time represented by `end_hour`. |
| `targetingType` | `string` | Output only. Identifies the type of this assigned targeting option. |
| `assignedTargetingOptionIdAlias` | `string` | Output only. An alias for the assigned_targeting_option_id. This value can be used in place of `assignedTargetingOptionId` when retrieving or deleting existing targeting. This field will only be supported for all assigned targeting options of the following targeting types: * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_DEVICE_TYPE` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_EXCHANGE` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_HOUSEHOLD_INCOME` * `TARGETING_TYPE_NATIVE_CONTENT_POSITION` * `TARGETING_TYPE_OMID` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_VIDEO_PLAYER_SIZE` * `TARGETING_TYPE_VIEWABILITY` This field is also supported for line item assigned targeting options of the following targeting types: * `TARGETING_TYPE_CONTENT_INSTREAM_POSITION` * `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION` |
| `viewabilityDetails` | `object` | Assigned viewability targeting option details. This will be populated in the viewability_details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_VIEWABILITY`. |
| `poiDetails` | `object` | Details for assigned POI targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_POI`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_campaigns_targetingTypes_assignedTargetingOptions_get` | `SELECT` | `advertisersId, assignedTargetingOptionsId, campaignsId, targetingTypesId` | Gets a single targeting option assigned to a campaign. |
| `advertisers_campaigns_targetingTypes_assignedTargetingOptions_list` | `SELECT` | `advertisersId, campaignsId, targetingTypesId` | Lists the targeting options assigned to a campaign for a specified targeting type. |
| `advertisers_insertionOrders_targetingTypes_assignedTargetingOptions_get` | `SELECT` | `advertisersId, assignedTargetingOptionsId, insertionOrdersId, targetingTypesId` | Gets a single targeting option assigned to an insertion order. |
| `advertisers_insertionOrders_targetingTypes_assignedTargetingOptions_list` | `SELECT` | `advertisersId, insertionOrdersId, targetingTypesId` | Lists the targeting options assigned to an insertion order. |
| `advertisers_lineItems_targetingTypes_assignedTargetingOptions_get` | `SELECT` | `advertisersId, assignedTargetingOptionsId, lineItemsId, targetingTypesId` | Gets a single targeting option assigned to a line item. |
| `advertisers_lineItems_targetingTypes_assignedTargetingOptions_list` | `SELECT` | `advertisersId, lineItemsId, targetingTypesId` | Lists the targeting options assigned to a line item. |
| `advertisers_targetingTypes_assignedTargetingOptions_get` | `SELECT` | `advertisersId, assignedTargetingOptionsId, targetingTypesId` | Gets a single targeting option assigned to an advertiser. |
| `advertisers_targetingTypes_assignedTargetingOptions_list` | `SELECT` | `advertisersId, targetingTypesId` | Lists the targeting options assigned to an advertiser. |
| `partners_targetingTypes_assignedTargetingOptions_get` | `SELECT` | `assignedTargetingOptionsId, partnersId, targetingTypesId` | Gets a single targeting option assigned to a partner. |
| `partners_targetingTypes_assignedTargetingOptions_list` | `SELECT` | `partnersId, targetingTypesId` | Lists the targeting options assigned to a partner. |
| `advertisers_insertionOrders_targetingTypes_assignedTargetingOptions_create` | `INSERT` | `advertisersId, insertionOrdersId, targetingTypesId` | Assigns a targeting option to an insertion order. Returns the assigned targeting option if successful. Supported targeting types: * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_BROWSER` * `TARGETING_TYPE_CATEGORY` * `TARGETING_TYPE_CHANNEL` * `TARGETING_TYPE_DEVICE_MAKE_MODEL` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_KEYWORD` * `TARGETING_TYPE_LANGUAGE` * `TARGETING_TYPE_NEGATIVE_KEYWORD_LIST` * `TARGETING_TYPE_OPERATING_SYSTEM` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_VIEWABILITY` |
| `advertisers_lineItems_targetingTypes_assignedTargetingOptions_create` | `INSERT` | `advertisersId, lineItemsId, targetingTypesId` | Assigns a targeting option to a line item. Returns the assigned targeting option if successful. Requests to this endpoint cannot be made concurrently with the following requests updating the same line item: * BulkEditAssignedTargetingOptions * BulkUpdate * UpdateLineItem * DeleteLineItemAssignedTargetingOption |
| `advertisers_targetingTypes_assignedTargetingOptions_create` | `INSERT` | `advertisersId, targetingTypesId` | Assigns a targeting option to an advertiser. Returns the assigned targeting option if successful. |
| `partners_targetingTypes_assignedTargetingOptions_create` | `INSERT` | `partnersId, targetingTypesId` | Assigns a targeting option to a partner. Returns the assigned targeting option if successful. |
| `advertisers_insertionOrders_targetingTypes_assignedTargetingOptions_delete` | `DELETE` | `advertisersId, assignedTargetingOptionsId, insertionOrdersId, targetingTypesId` | Deletes an assigned targeting option from an insertion order. Supported targeting types: * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_BROWSER` * `TARGETING_TYPE_CATEGORY` * `TARGETING_TYPE_CHANNEL` * `TARGETING_TYPE_DEVICE_MAKE_MODEL` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_KEYWORD` * `TARGETING_TYPE_LANGUAGE` * `TARGETING_TYPE_NEGATIVE_KEYWORD_LIST` * `TARGETING_TYPE_OPERATING_SYSTEM` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_VIEWABILITY` |
| `advertisers_lineItems_targetingTypes_assignedTargetingOptions_delete` | `DELETE` | `advertisersId, assignedTargetingOptionsId, lineItemsId, targetingTypesId` | Deletes an assigned targeting option from a line item. Requests to this endpoint cannot be made concurrently with the following requests updating the same line item: * BulkEditAssignedTargetingOptions * BulkUpdate * UpdateLineItem * CreateLineItemAssignedTargetingOption |
| `advertisers_targetingTypes_assignedTargetingOptions_delete` | `DELETE` | `advertisersId, assignedTargetingOptionsId, targetingTypesId` | Deletes an assigned targeting option from an advertiser. |
| `partners_targetingTypes_assignedTargetingOptions_delete` | `DELETE` | `assignedTargetingOptionsId, partnersId, targetingTypesId` | Deletes an assigned targeting option from a partner. |
