---
title: channel_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_sections
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
<tr><td><b>Name</b></td><td><code>channel_sections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.channel_sections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the channel section. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#channelSection". |
| `localizations` | `object` | Localizations for different languages |
| `snippet` | `object` | Basic details about a channel section, including title, style and position. |
| `targeting` | `object` | ChannelSection targeting setting. |
| `contentDetails` | `object` | Details about a channelsection, including playlists and channels. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `channelSections_list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `channelSections_delete` | `DELETE` | `id` | Deletes a resource. |
| `channelSections_insert` | `EXEC` | `part` | Inserts a new resource into this collection. |
| `channelSections_update` | `EXEC` | `part` | Updates an existing resource. |
