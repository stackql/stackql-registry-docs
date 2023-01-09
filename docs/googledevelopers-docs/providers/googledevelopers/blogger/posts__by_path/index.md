---
title: posts__by_path
hide_title: false
hide_table_of_contents: false
keywords:
  - posts__by_path
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
<tr><td><b>Name</b></td><td><code>posts__by_path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.posts__by_path</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of this Post. |
| `replies` | `object` | The container of comments on this Post. |
| `labels` | `array` | The list of labels this Post was tagged with. |
| `blog` | `object` | Data about the blog containing this Post. |
| `updated` | `string` | RFC 3339 date-time when this Post was last updated. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `etag` | `string` | Etag of the resource. |
| `titleLink` | `string` | The title link URL, similar to atom's related link. |
| `images` | `array` | Display image for the Post. |
| `trashed` | `string` | RFC 3339 date-time when this Post was last trashed. |
| `kind` | `string` | The kind of this entity. Always blogger#post. |
| `readerComments` | `string` | Comment control and display setting for readers of this post. |
| `url` | `string` | The URL where this Post is displayed. |
| `title` | `string` | The title of the Post. |
| `location` | `object` | The location for geotagged posts. |
| `published` | `string` | RFC 3339 date-time when this Post was published. |
| `status` | `string` | Status of the post. Only set for admin-level requests. |
| `author` | `object` | The author of this Post. |
| `customMetaData` | `string` | The JSON meta-data for the Post. |
| `content` | `string` | The content of the Post. May contain HTML markup. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `posts_getByPath` | `SELECT` | `blogId, path` |
