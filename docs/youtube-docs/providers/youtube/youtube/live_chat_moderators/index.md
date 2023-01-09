---
title: live_chat_moderators
hide_title: false
hide_table_of_contents: false
keywords:
  - live_chat_moderators
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
<tr><td><b>Name</b></td><td><code>live_chat_moderators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.live_chat_moderators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube assigns to uniquely identify the moderator. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#liveChatModerator". |
| `snippet` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `liveChatModerators_list` | `SELECT` | `liveChatId, part` | Retrieves a list of resources, possibly filtered. |
| `liveChatModerators_delete` | `DELETE` | `id` | Deletes a chat moderator. |
| `liveChatModerators_insert` | `EXEC` | `part` | Inserts a new resource into this collection. |
