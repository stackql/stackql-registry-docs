---
title: channel_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_connections
  - eventarc
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.channel_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The name of the connection. |
| `uid` | `string` | Output only. Server assigned ID of the resource. The server guarantees uniqueness and immutability until deleted. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `activationToken` | `string` | Input only. Activation token for the channel. The token will be used during the creation of ChannelConnection to bind the channel with the provider project. This field will not be stored in the provider resource. |
| `channel` | `string` | Required. The name of the connected subscriber Channel. This is a weak reference to avoid cross project and cross accounts references. This must be in `projects/&#123;project&#125;/location/&#123;location&#125;/channels/&#123;channel_id&#125;` format. |
| `createTime` | `string` | Output only. The creation time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `channelConnectionsId, locationsId, projectsId` | Get a single ChannelConnection. |
| `list` | `SELECT` | `locationsId, projectsId` | List channel connections. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new ChannelConnection in a particular project and location. |
| `delete` | `DELETE` | `channelConnectionsId, locationsId, projectsId` | Delete a single ChannelConnection. |
| `_list` | `EXEC` | `locationsId, projectsId` | List channel connections. |
