---
title: group_items
hide_title: false
hide_table_of_contents: false
keywords:
  - group_items
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
<tr><td><b>Name</b></td><td><code>group_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtubeAnalytics.group_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the `channel`, `video`, `playlist`, or `asset` resource that is included in the group. Note that this ID refers specifically to the inclusion of that resource in a particular group and is different than the channel ID, video ID, playlist ID, or asset ID that uniquely identifies the resource itself. The `resource.id` property's value specifies the unique channel, video, playlist, or asset ID. |
| `etag` | `string` | The Etag of this resource. |
| `groupId` | `string` | The ID that YouTube uses to uniquely identify the group that contains the item. |
| `kind` | `string` | Identifies the API resource's type. The value will be `youtube#groupItem`. |
| `resource` | `object` |  |
| `errors` | `object` | Request Error information. The presence of an error field signals that the operation has failed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `groupItems_list` | `SELECT` |  | Returns a collection of group items that match the API request parameters. |
| `groupItems_delete` | `DELETE` |  | Removes an item from a group. |
| `groupItems_insert` | `EXEC` |  | Creates a group item. |
