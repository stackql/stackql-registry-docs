---
title: live_chat_messages
hide_title: false
hide_table_of_contents: false
keywords:
  - live_chat_messages
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
<tr><td><b>Name</b></td><td><code>live_chat_messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.live_chat_messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube assigns to uniquely identify the message. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#liveChatMessage". |
| `snippet` | `object` | Next ID: 33 |
| `authorDetails` | `object` |  |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `liveChatMessages_list` | `SELECT` | `liveChatId, part` | Retrieves a list of resources, possibly filtered. |
| `liveChatMessages_delete` | `DELETE` | `id` | Deletes a chat message. |
| `liveChatMessages_insert` | `EXEC` | `part` | Inserts a new resource into this collection. |
