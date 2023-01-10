---
title: playlist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - playlist_items
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
<tr><td><b>Name</b></td><td><code>playlist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.playlist_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the playlist item. |
| `contentDetails` | `object` |  |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#playlistItem". |
| `snippet` | `object` | Basic details about a playlist, including title, description and thumbnails. Basic details of a YouTube Playlist item provided by the author. Next ID: 15 |
| `status` | `object` | Information about the playlist item's privacy status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `playlistItems_list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `playlistItems_delete` | `DELETE` | `id` | Deletes a resource. |
| `playlistItems_insert` | `EXEC` | `part` | Inserts a new resource into this collection. |
| `playlistItems_update` | `EXEC` | `part` | Updates an existing resource. |
