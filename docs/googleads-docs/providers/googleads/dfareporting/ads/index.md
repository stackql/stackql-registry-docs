---
title: ads
hide_title: false
hide_table_of_contents: false
keywords:
  - ads
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.ads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this ad. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this ad. This is a required field and must be less than 256 characters long. |
| `geoTargeting` | `object` | Geographical Targeting. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `defaultClickThroughEventTagProperties` | `object` | Properties of inheriting and overriding the default click-through event tag. A campaign may override the event tag defined at the advertiser level, and an ad may also override the campaign's setting further. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `placementAssignments` | `array` | Placement assignments for this ad. |
| `clickThroughUrlSuffixProperties` | `object` | Click Through URL Suffix settings. |
| `advertiserId` | `string` | Advertiser ID of this ad. This is a required field on insertion. |
| `comments` | `string` | Comments for this ad. |
| `creativeRotation` | `object` | Creative Rotation. |
| `creativeGroupAssignments` | `array` | Creative group assignments for this ad. Applicable when type is AD_SERVING_CLICK_TRACKER. Only one assignment per creative group number is allowed for a maximum of two assignments. |
| `active` | `boolean` | Whether this ad is active. When true, archived must be false. |
| `campaignId` | `string` | Campaign ID of this ad. This is a required field on insertion. |
| `campaignIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `remarketingListExpression` | `object` | Remarketing List Targeting Expression. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#ad". |
| `subaccountId` | `string` | Subaccount ID of this ad. This is a read-only field that can be left blank. |
| `compatibility` | `string` | Compatibility of this ad. Applicable when type is AD_SERVING_DEFAULT_AD. DISPLAY and DISPLAY_INTERSTITIAL refer to either rendering on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are only used for existing default ads. New mobile placements must be assigned DISPLAY or DISPLAY_INTERSTITIAL and default ads created for those placements will be limited to those compatibility types. IN_STREAM_VIDEO refers to rendering in-stream video ads developed with the VAST standard. |
| `size` | `object` | Represents the dimensions of ads, placements, creatives, or creative assets. |
| `targetingTemplateId` | `string` | Targeting template ID, used to apply preconfigured targeting information to this ad. This cannot be set while any of dayPartTargeting, geoTargeting, keyValueTargetingExpression, languageTargeting, remarketingListExpression, or technologyTargeting are set. Applicable when type is AD_SERVING_STANDARD_AD. |
| `clickThroughUrl` | `object` | Click-through URL |
| `createInfo` | `object` | Modification timestamp. |
| `endTime` | `string` |  |
| `sslRequired` | `boolean` | Whether this ad requires ssl. This is a read-only field that is auto-generated when the ad is inserted or updated. |
| `dayPartTargeting` | `object` | Day Part Targeting. |
| `audienceSegmentId` | `string` | Audience segment ID that is being targeted for this ad. Applicable when type is AD_SERVING_STANDARD_AD. |
| `sslCompliant` | `boolean` | Whether this ad is ssl compliant. This is a read-only field that is auto-generated when the ad is inserted or updated. |
| `startTime` | `string` |  |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `type` | `string` | Type of ad. This is a required field on insertion. Note that default ads ( AD_SERVING_DEFAULT_AD) cannot be created directly (see Creative resource). |
| `accountId` | `string` | Account ID of this ad. This is a read-only field that can be left blank. |
| `technologyTargeting` | `object` | Technology Targeting. |
| `deliverySchedule` | `object` | Delivery Schedule. |
| `archived` | `boolean` | Whether this ad is archived. When true, active must be false. |
| `dynamicClickTracker` | `boolean` | Whether this ad is a dynamic click tracker. Applicable when type is AD_SERVING_CLICK_TRACKER. This is a required field on insert, and is read-only after insert. |
| `eventTagOverrides` | `array` | Event tag overrides for this ad. |
| `languageTargeting` | `object` | Language Targeting. |
| `keyValueTargetingExpression` | `object` | Key Value Targeting Expression. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one ad by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of ads, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new ad. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing ad. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing ad. |
