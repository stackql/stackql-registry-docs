---
title: comment_threads
hide_title: false
hide_table_of_contents: false
keywords:
  - comment_threads
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
<tr><td><b>Name</b></td><td><code>comment_threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.comment_threads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the comment thread. |
| `snippet` | `object` | Basic details about a comment thread. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#commentThread". |
| `replies` | `object` | Comments written in (direct or indirect) reply to the top level comment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `commentThreads_list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `commentThreads_insert` | `EXEC` | `part` | Inserts a new resource into this collection. |
