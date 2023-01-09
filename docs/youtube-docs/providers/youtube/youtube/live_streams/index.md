---
title: live_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - live_streams
  - youtube
  - youtube    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/youtube/stackql-youtube-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.live_streams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube assigns to uniquely identify the stream. |
| `status` | `object` | Brief description of the live stream status. |
| `cdn` | `object` | Brief description of the live stream cdn settings. |
| `contentDetails` | `object` | Detailed settings of a stream. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#liveStream". |
| `snippet` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `liveStreams_list` | `SELECT` | `part` | Retrieve the list of streams associated with the given channel. -- |
| `liveStreams_delete` | `DELETE` | `id` | Deletes an existing stream for the authenticated user. |
| `liveStreams_insert` | `EXEC` | `part` | Inserts a new stream for the authenticated user. |
| `liveStreams_update` | `EXEC` | `part` | Updates an existing stream for the authenticated user. |
