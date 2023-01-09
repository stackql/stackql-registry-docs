---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
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
<tr><td><b>Name</b></td><td><code>campaigns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.campaigns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the campaign. |
| `advertiserId` | `string` | Output only. The unique ID of the advertiser the campaign belongs to. |
| `campaignId` | `string` | Output only. The unique ID of the campaign. Assigned by the system. |
| `campaignBudgets` | `array` | The list of budgets available to this campaign. If this field is not set, the campaign uses an unlimited budget. |
| `entityStatus` | `string` | Required. Controls whether or not the insertion orders under this campaign can spend their budgets and bid on inventory. * Accepted values are `ENTITY_STATUS_ACTIVE`, `ENTITY_STATUS_ARCHIVED`, and `ENTITY_STATUS_PAUSED`. * For CreateCampaign method, `ENTITY_STATUS_ARCHIVED` is not allowed. |
| `campaignFlight` | `object` | Settings that track the planned spend and duration of a campaign. |
| `campaignGoal` | `object` | Settings that control the goal of a campaign. |
| `displayName` | `string` | Required. The display name of the campaign. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `updateTime` | `string` | Output only. The timestamp when the campaign was last updated. Assigned by the system. |
| `frequencyCap` | `object` | Settings that control the number of times a user may be shown with the same ad during a given time period. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_campaigns_get` | `SELECT` | `advertisersId, campaignsId` | Gets a campaign. |
| `advertisers_campaigns_list` | `SELECT` | `advertisersId` | Lists campaigns in an advertiser. The order is defined by the order_by parameter. If a filter by entity_status is not specified, campaigns with `ENTITY_STATUS_ARCHIVED` will not be included in the results. |
| `advertisers_campaigns_create` | `INSERT` | `advertisersId` | Creates a new campaign. Returns the newly created campaign if successful. |
| `advertisers_campaigns_delete` | `DELETE` | `advertisersId, campaignsId` | Permanently deletes a campaign. A deleted campaign cannot be recovered. The campaign should be archived first, i.e. set entity_status to `ENTITY_STATUS_ARCHIVED`, to be able to delete it. |
| `advertisers_campaigns_patch` | `EXEC` | `advertisersId, campaignsId` | Updates an existing campaign. Returns the updated campaign if successful. |
