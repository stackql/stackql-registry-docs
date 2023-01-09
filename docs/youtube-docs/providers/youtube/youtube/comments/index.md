---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the comment. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#comment". |
| `snippet` | `object` | Basic details about a comment, such as its author and text. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `insert` | `INSERT` | `part` | Inserts a new resource into this collection. |
| `delete` | `DELETE` | `id` | Deletes a resource. |
| `markAsSpam` | `EXEC` | `id` | Expresses the caller's opinion that one or more comments should be flagged as spam. |
| `setModerationStatus` | `EXEC` | `id, moderationStatus` | Sets the moderation status of one or more comments. |
| `update` | `EXEC` | `part` | Updates an existing resource. |
