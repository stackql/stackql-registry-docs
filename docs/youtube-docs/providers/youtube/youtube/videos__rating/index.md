---
title: videos__rating
hide_title: false
hide_table_of_contents: false
keywords:
  - videos__rating
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
<tr><td><b>Name</b></td><td><code>videos__rating</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.videos__rating</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rating` | `string` | Rating of a video. |
| `videoId` | `string` | The ID that YouTube uses to uniquely identify the video. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `videos_getRating` | `SELECT` | `id` |
