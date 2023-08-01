---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A page token that can be sent to `ListChannels` to request the next page. If this is empty, then there are no more pages. |
| `unreachable` | `array` | Unreachable resources, if any. |
| `channels` | `array` | The requested channels, up to the number specified in `page_size`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `channelsId, locationsId, projectsId` | Get a single Channel. |
| `list` | `SELECT` | `locationsId, projectsId` | List channels. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new channel in a particular project and location. |
| `delete` | `DELETE` | `channelsId, locationsId, projectsId` | Delete a single channel. |
| `patch` | `EXEC` | `channelsId, locationsId, projectsId` | Update a single channel. |
