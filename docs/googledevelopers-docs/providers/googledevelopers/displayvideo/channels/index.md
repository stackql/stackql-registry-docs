---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the channel. |
| `partnerId` | `string` | The ID of the partner that owns the channel. |
| `positivelyTargetedLineItemCount` | `string` | Output only. Number of line items that are directly targeting this channel positively. |
| `advertiserId` | `string` | The ID of the advertiser that owns the channel. |
| `channelId` | `string` | Output only. The unique ID of the channel. Assigned by the system. |
| `displayName` | `string` | Required. The display name of the channel. Must be UTF-8 encoded with a maximum length of 240 bytes. |
| `negativelyTargetedLineItemCount` | `string` | Output only. Number of line items that are directly targeting this channel negatively. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_channels_get` | `SELECT` | `advertisersId, channelsId` | Gets a channel for a partner or advertiser. |
| `advertisers_channels_list` | `SELECT` | `advertisersId` | Lists channels for a partner or advertiser. |
| `partners_channels_get` | `SELECT` | `channelsId, partnersId` | Gets a channel for a partner or advertiser. |
| `partners_channels_list` | `SELECT` | `partnersId` | Lists channels for a partner or advertiser. |
| `advertisers_channels_create` | `INSERT` | `advertisersId` | Creates a new channel. Returns the newly created channel if successful. |
| `partners_channels_create` | `INSERT` | `partnersId` | Creates a new channel. Returns the newly created channel if successful. |
| `advertisers_channels_patch` | `EXEC` | `advertisersId, channelId` | Updates a channel. Returns the updated channel if successful. |
| `partners_channels_patch` | `EXEC` | `channelId, partnersId` | Updates a channel. Returns the updated channel if successful. |
