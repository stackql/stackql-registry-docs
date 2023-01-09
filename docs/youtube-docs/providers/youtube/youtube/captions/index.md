---
title: captions
hide_title: false
hide_table_of_contents: false
keywords:
  - captions
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
<tr><td><b>Name</b></td><td><code>captions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.captions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the caption track. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#caption". |
| `snippet` | `object` | Basic details about a caption track, such as its language and name. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `part, videoId` | Retrieves a list of resources, possibly filtered. |
| `insert` | `INSERT` | `part` | Inserts a new resource into this collection. |
| `delete` | `DELETE` | `id` | Deletes a resource. |
| `download` | `EXEC` | `id` | Downloads a caption track. |
| `update` | `EXEC` | `part` | Updates an existing resource. |
