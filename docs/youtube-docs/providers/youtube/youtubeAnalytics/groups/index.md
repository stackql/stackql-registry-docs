---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - youtubeAnalytics
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtubeAnalytics.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the group. |
| `errors` | `object` | Request Error information. The presence of an error field signals that the operation has failed. |
| `etag` | `string` | The Etag of this resource. |
| `kind` | `string` | Identifies the API resource's type. The value will be `youtube#group`. |
| `snippet` | `object` | A group snippet. |
| `contentDetails` | `object` | A group's content details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Returns a collection of groups that match the API request parameters. For example, you can retrieve all groups that the authenticated user owns, or you can retrieve one or more groups by their unique IDs. |
| `insert` | `INSERT` |  | Creates a group. |
| `delete` | `DELETE` |  | Deletes a group. |
| `update` | `EXEC` |  | Modifies a group. For example, you could change a group's title. |
