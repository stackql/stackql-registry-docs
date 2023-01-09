---
title: activities
hide_title: false
hide_table_of_contents: false
keywords:
  - activities
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
<tr><td><b>Name</b></td><td><code>activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.activities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the activity. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#activity". |
| `snippet` | `object` | Basic details about an activity, including title, description, thumbnails, activity type and group. Next ID: 12 |
| `contentDetails` | `object` | Details about the content of an activity: the video that was shared, the channel that was subscribed to, etc. |
| `etag` | `string` | Etag of this resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `part` |
