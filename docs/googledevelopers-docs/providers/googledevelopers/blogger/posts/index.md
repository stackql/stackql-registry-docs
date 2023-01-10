---
title: posts
hide_title: false
hide_table_of_contents: false
keywords:
  - posts
  - blogger
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>posts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.posts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of this Post. |
| `replies` | `object` | The container of comments on this Post. |
| `url` | `string` | The URL where this Post is displayed. |
| `readerComments` | `string` | Comment control and display setting for readers of this post. |
| `blog` | `object` | Data about the blog containing this Post. |
| `published` | `string` | RFC 3339 date-time when this Post was published. |
| `images` | `array` | Display image for the Post. |
| `title` | `string` | The title of the Post. |
| `etag` | `string` | Etag of the resource. |
| `customMetaData` | `string` | The JSON meta-data for the Post. |
| `location` | `object` | The location for geotagged posts. |
| `author` | `object` | The author of this Post. |
| `kind` | `string` | The kind of this entity. Always blogger#post. |
| `content` | `string` | The content of the Post. May contain HTML markup. |
| `trashed` | `string` | RFC 3339 date-time when this Post was last trashed. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `status` | `string` | Status of the post. Only set for admin-level requests. |
| `updated` | `string` | RFC 3339 date-time when this Post was last updated. |
| `titleLink` | `string` | The title link URL, similar to atom's related link. |
| `labels` | `array` | The list of labels this Post was tagged with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blogId, postId` | Gets a post by blog id and post id |
| `list` | `SELECT` | `blogId` | Lists posts. |
| `insert` | `INSERT` | `blogId` | Inserts a post. |
| `delete` | `DELETE` | `blogId, postId` | Deletes a post by blog id and post id. |
| `patch` | `EXEC` | `blogId, postId` | Patches a post. |
| `publish` | `EXEC` | `blogId, postId` | Publishes a post. |
| `revert` | `EXEC` | `blogId, postId` | Reverts a published or scheduled post to draft state. |
| `search` | `EXEC` | `blogId, q` | Searches for posts matching given query terms in the specified blog. |
| `update` | `EXEC` | `blogId, postId` | Updates a post by blog id and post id. |
