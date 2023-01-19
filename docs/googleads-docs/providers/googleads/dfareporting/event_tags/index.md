---
title: event_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_tags
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
<tr><td><b>Name</b></td><td><code>event_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.event_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this event tag. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this event tag. This is a required field and must be less than 256 characters long. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#eventTag". |
| `urlEscapeLevels` | `integer` | Number of times the landing page URL should be URL-escaped before being appended to the click-through event tag URL. Only applies to click-through event tags as specified by the event tag type. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `siteFilterType` | `string` | Site filter type for this event tag. If no type is specified then the event tag will be applied to all sites. |
| `subaccountId` | `string` | Subaccount ID of this event tag. This is a read-only field that can be left blank. |
| `status` | `string` | Status of this event tag. Must be ENABLED for this event tag to fire. This is a required field. |
| `siteIds` | `array` | Filter list of site IDs associated with this event tag. The siteFilterType determines whether this is a allowlist or blocklist filter. |
| `advertiserId` | `string` | Advertiser ID of this event tag. This field or the campaignId field is required on insertion. |
| `type` | `string` | Event tag type. Can be used to specify whether to use a third-party pixel, a third-party JavaScript URL, or a third-party click-through URL for either impression or click tracking. This is a required field. |
| `campaignId` | `string` | Campaign ID of this event tag. This field or the advertiserId field is required on insertion. |
| `url` | `string` | Payload URL for this event tag. The URL on a click-through event tag should have a landing page URL appended to the end of it. This field is required on insertion. |
| `enabledByDefault` | `boolean` | Whether this event tag should be automatically enabled for all of the advertiser's campaigns and ads. |
| `accountId` | `string` | Account ID of this event tag. This is a read-only field that can be left blank. |
| `excludeFromAdxRequests` | `boolean` | Whether to remove this event tag from ads that are trafficked through Display & Video 360 to Ad Exchange. This may be useful if the event tag uses a pixel that is unapproved for Ad Exchange bids on one or more networks, such as the Google Display Network. |
| `campaignIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `sslCompliant` | `boolean` | Whether this tag is SSL-compliant or not. This is a read-only field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `eventTags_get` | `SELECT` | `id, profileId` | Gets one event tag by ID. |
| `eventTags_list` | `SELECT` | `profileId` | Retrieves a list of event tags, possibly filtered. |
| `eventTags_delete` | `DELETE` | `id, profileId` | Deletes an existing event tag. |
| `eventTags_insert` | `EXEC` | `profileId` | Inserts a new event tag. |
| `eventTags_patch` | `EXEC` | `id, profileId` | Updates an existing event tag. This method supports patch semantics. |
| `eventTags_update` | `EXEC` | `profileId` | Updates an existing event tag. |
