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
| `channelConnections` | `array` | The requested channel connections, up to the number specified in `page_size`. |
| `nextPageToken` | `string` | A page token that can be sent to `ListChannelConnections` to request the next page. If this is empty, then there are no more pages. |
| `unreachable` | `array` | Unreachable resources, if any. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `channelConnectionsId, locationsId, projectsId` | Get a single ChannelConnection. |
| `list` | `SELECT` | `locationsId, projectsId` | List channel connections. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new ChannelConnection in a particular project and location. |
| `delete` | `DELETE` | `channelConnectionsId, locationsId, projectsId` | Delete a single ChannelConnection. |
