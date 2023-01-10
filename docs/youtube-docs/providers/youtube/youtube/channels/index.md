---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the channel. |
| `snippet` | `object` | Basic details about a channel, including title, description and thumbnails. |
| `contentOwnerDetails` | `object` | The contentOwnerDetails object encapsulates channel data that is relevant for YouTube Partners linked with the channel. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#channel". |
| `brandingSettings` | `object` | Branding properties of a YouTube channel. |
| `contentDetails` | `object` | Details about the content of a channel. |
| `etag` | `string` | Etag of this resource. |
| `topicDetails` | `object` | Freebase topic information related to the channel. |
| `status` | `object` | JSON template for the status part of a channel. |
| `auditDetails` | `object` | The auditDetails object encapsulates channel data that is relevant for YouTube Partners during the audit process. |
| `conversionPings` | `object` | The conversionPings object encapsulates information about conversion pings that need to be respected by the channel. |
| `statistics` | `object` | Statistics about a channel: number of subscribers, number of videos in the channel, etc. |
| `localizations` | `object` | Localizations for different languages |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `update` | `EXEC` | `part` | Updates an existing resource. |
