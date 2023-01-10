---
title: placements
hide_title: false
hide_table_of_contents: false
keywords:
  - placements
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
<tr><td><b>Name</b></td><td><code>placements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.placements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this placement. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this placement.This is a required field and must be less than or equal to 512 characters long. |
| `vpaidAdapterChoice` | `string` | VPAID adapter setting for this placement. Controls which VPAID format the measurement adapter will use for in-stream video creatives assigned to this placement. *Note:* Flash is no longer supported. This field now defaults to HTML5 when the following values are provided: FLASH, BOTH. |
| `accountId` | `string` | Account ID of this placement. This field can be left blank. |
| `videoActiveViewOptOut` | `boolean` | Whether Verification and ActiveView are disabled for in-stream video creatives for this placement. The same setting videoActiveViewOptOut exists on the site level -- the opt out occurs if either of these settings are true. These settings are distinct from DirectorySites.settings.activeViewOptOut or Sites.siteSettings.activeViewOptOut which only apply to display ads. However, Accounts.activeViewOptOut opts out both video traffic, as well as display ads, from Verification and ActiveView. |
| `lookbackConfiguration` | `object` | Lookback configuration settings. |
| `tagSetting` | `object` | Tag Settings |
| `sslRequired` | `boolean` | Whether creatives assigned to this placement must be SSL-compliant. |
| `paymentSource` | `string` | Payment source for this placement. This is a required field that is read-only after insertion. |
| `pricingSchedule` | `object` | Pricing Schedule |
| `size` | `object` | Represents the dimensions of ads, placements, creatives, or creative assets. |
| `createInfo` | `object` | Modification timestamp. |
| `siteIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `compatibility` | `string` | Placement compatibility. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering on desktop, on mobile devices or in mobile apps for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are no longer allowed for new placement insertions. Instead, use DISPLAY or DISPLAY_INTERSTITIAL. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. This field is required on insertion. |
| `additionalSizes` | `array` | Additional sizes associated with this placement. When inserting or updating a placement, only the size ID field is used. |
| `primary` | `boolean` | Whether this placement is the primary placement of a roadblock (placement group). You cannot change this field from true to false. Setting this field to true will automatically set the primary field on the original primary placement of the roadblock to false, and it will automatically set the roadblock's primaryPlacementId field to the ID of this placement. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `status` | `string` | Third-party placement status. |
| `directorySiteIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `siteId` | `string` | Site ID associated with this placement. On insert, you must set either this field or the directorySiteId field to specify the site associated with this placement. This is a required field that is read-only after insertion. |
| `paymentApproved` | `boolean` | Whether payment was approved for this placement. This is a read-only field relevant only to publisher-paid placements. |
| `advertiserId` | `string` | Advertiser ID of this placement. This field can be left blank. |
| `campaignId` | `string` | Campaign ID of this placement. This field is a required field on insertion. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `adBlockingOptOut` | `boolean` | Whether this placement opts out of ad blocking. When true, ad blocking is disabled for this placement. When false, the campaign and site settings take effect. |
| `publisherUpdateInfo` | `object` | Modification timestamp. |
| `directorySiteId` | `string` | Directory site ID of this placement. On insert, you must set either this field or the siteId field to specify the site associated with this placement. This is a required field that is read-only after insertion. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#placement". |
| `placementGroupIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `placementGroupId` | `string` | ID of this placement's group, if applicable. |
| `keyName` | `string` | Key name of this placement. This is a read-only, auto-generated field. |
| `partnerWrappingData` | `object` | Placement tag wrapping |
| `comment` | `string` | Comments for this placement. |
| `campaignIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `subaccountId` | `string` | Subaccount ID of this placement. This field can be left blank. |
| `activeStatus` | `string` | Whether this placement is active, inactive, archived or permanently archived. |
| `tagFormats` | `array` | Tag formats to generate for this placement. This field is required on insertion. Acceptable values are: - "PLACEMENT_TAG_STANDARD" - "PLACEMENT_TAG_IFRAME_JAVASCRIPT" - "PLACEMENT_TAG_IFRAME_ILAYER" - "PLACEMENT_TAG_INTERNAL_REDIRECT" - "PLACEMENT_TAG_JAVASCRIPT" - "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT" - "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT" - "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT" - "PLACEMENT_TAG_CLICK_COMMANDS" - "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH" - "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3" - "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4" - "PLACEMENT_TAG_TRACKING" - "PLACEMENT_TAG_TRACKING_IFRAME" - "PLACEMENT_TAG_TRACKING_JAVASCRIPT"  |
| `contentCategoryId` | `string` | ID of the content category assigned to this placement. |
| `placementStrategyId` | `string` | ID of the placement strategy assigned to this placement. |
| `wrappingOptOut` | `boolean` | Whether this placement opts out of tag wrapping. |
| `videoSettings` | `object` | Video Settings |
| `externalId` | `string` | External ID for this placement. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one placement by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of placements, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new placement. |
| `generatetags` | `EXEC` | `profileId` | Generates tags for a placement. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing placement. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing placement. |
