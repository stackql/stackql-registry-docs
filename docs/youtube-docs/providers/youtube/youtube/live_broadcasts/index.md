---
title: live_broadcasts
hide_title: false
hide_table_of_contents: false
keywords:
  - live_broadcasts
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
<tr><td><b>Name</b></td><td><code>live_broadcasts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.live_broadcasts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube assigns to uniquely identify the broadcast. |
| `snippet` | `object` | Basic broadcast information. |
| `statistics` | `object` | Statistics about the live broadcast. These represent a snapshot of the values at the time of the request. Statistics are only returned for live broadcasts. |
| `status` | `object` | Live broadcast state. |
| `contentDetails` | `object` | Detailed settings of a broadcast. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#liveBroadcast". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `liveBroadcasts_list` | `SELECT` | `part` | Retrieve the list of broadcasts associated with the given channel. |
| `liveBroadcasts_delete` | `DELETE` | `id` | Delete a given broadcast. |
| `liveBroadcasts_bind` | `EXEC` | `id, part` | Bind a broadcast to a stream. |
| `liveBroadcasts_insert` | `EXEC` | `part` | Inserts a new stream for the authenticated user. |
| `liveBroadcasts_insertCuepoint` | `EXEC` |  | Insert cuepoints in a broadcast |
| `liveBroadcasts_transition` | `EXEC` | `broadcastStatus, id, part` | Transition a broadcast to a given status. |
| `liveBroadcasts_update` | `EXEC` | `part` | Updates an existing broadcast for the authenticated user. |
