---
title: creatives
hide_title: false
hide_table_of_contents: false
keywords:
  - creatives
  - realtimebidding
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
<tr><td><b>Name</b></td><td><code>creatives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.creatives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the creative. Follows the pattern `buyers/&#123;buyer&#125;/creatives/&#123;creative&#125;`, where `&#123;buyer&#125;` represents the account ID of the buyer who owns the creative, and `&#123;creative&#125;` is the buyer-specific creative ID that references this creative in the bid response. |
| `native` | `object` | Native content for a creative. |
| `dealIds` | `array` | Output only. IDs of all of the deals with which this creative has been used in bidding. Can be used to filter the response of the creatives.list method. |
| `declaredAttributes` | `array` | All declared attributes for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. If the `excluded_attribute` field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto") contains one of the attributes that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. |
| `agencyId` | `string` | The agency ID for this creative. |
| `version` | `integer` | Output only. The version of the creative. Version for a new creative is 1 and it increments during subsequent creative updates. |
| `advertiserName` | `string` | The name of the company being advertised in the creative. Can be used to filter the response of the creatives.list method. |
| `creativeId` | `string` | Buyer-specific creative ID that references this creative in bid responses. This field is Ignored in update operations. Can be used to filter the response of the creatives.list method. The maximum length of the creative ID is 128 bytes. |
| `declaredRestrictedCategories` | `array` | All declared restricted categories for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. |
| `restrictedCategories` | `array` | All restricted categories for the ads that may be shown from this creative. |
| `declaredVendorIds` | `array` | IDs for the declared ad technology vendors that may be used by this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. Can be used to filter the response of the creatives.list method. |
| `adChoicesDestinationUrl` | `string` | The link to AdChoices destination page. This is only supported for native ads. |
| `apiUpdateTime` | `string` | Output only. The last update timestamp of the creative through the API. |
| `renderUrl` | `string` | Experimental field that can be used during the [FLEDGE Origin Trial](/authorized-buyers/rtb/fledge-origin-trial). The URL to fetch an interest group ad used in [TURTLEDOVE on-device auction](https://github.com/WICG/turtledove/blob/main/FLEDGE.md#1-browsers-record-interest-groups"). This should be unique among all creatives for a given `accountId`. |
| `accountId` | `string` | Output only. ID of the buyer account that this creative is owned by. Can be used to filter the response of the creatives.list method with equality and inequality check. |
| `creativeFormat` | `string` | Output only. The format of this creative. Can be used to filter the response of the creatives.list method. |
| `declaredClickThroughUrls` | `array` | The set of declared destination URLs for the creative. Can be used to filter the response of the creatives.list method. |
| `html` | `object` | HTML content for a creative. |
| `impressionTrackingUrls` | `array` | The set of URLs to be called to record an impression. |
| `creativeServingDecision` | `object` | Top level status and detected attributes of a creative. |
| `video` | `object` | Video content for a creative. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_creatives_list` | `SELECT` | `biddersId` | Lists creatives as they are at the time of the initial request. This call may take multiple hours to complete. For large, paginated requests, this method returns a snapshot of creatives at the time of request for the first page. `lastStatusUpdate` and `creativeServingDecision` may be outdated for creatives on sequential pages. We recommend [Google Cloud Pub/Sub](//cloud.google.com/pubsub/docs/overview) to view the latest status. |
| `buyers_creatives_get` | `SELECT` | `buyersId, creativesId` | Gets a creative. |
| `buyers_creatives_list` | `SELECT` | `buyersId` | Lists creatives as they are at the time of the initial request. This call may take multiple hours to complete. For large, paginated requests, this method returns a snapshot of creatives at the time of request for the first page. `lastStatusUpdate` and `creativeServingDecision` may be outdated for creatives on sequential pages. We recommend [Google Cloud Pub/Sub](//cloud.google.com/pubsub/docs/overview) to view the latest status. |
| `buyers_creatives_create` | `INSERT` | `buyersId` | Creates a creative. |
| `bidders_creatives_watch` | `EXEC` | `biddersId` | Watches all creatives pertaining to a bidder. It is sufficient to invoke this endpoint once per bidder. A Pub/Sub topic will be created and notifications will be pushed to the topic when any of the bidder's creatives change status. All of the bidder's service accounts will have access to read from the topic. Subsequent invocations of this method will return the existing Pub/Sub configuration. |
| `buyers_creatives_patch` | `EXEC` | `buyersId, creativesId` | Updates a creative. |
