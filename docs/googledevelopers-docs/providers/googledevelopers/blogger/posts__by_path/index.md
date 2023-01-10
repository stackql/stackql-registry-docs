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
| `readerComments` | `string` | Comment control and display setting for readers of this post. |
| `labels` | `array` | The list of labels this Post was tagged with. |
| `customMetaData` | `string` | The JSON meta-data for the Post. |
| `blog` | `object` | Data about the blog containing this Post. |
| `content` | `string` | The content of the Post. May contain HTML markup. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `images` | `array` | Display image for the Post. |
| `url` | `string` | The URL where this Post is displayed. |
| `titleLink` | `string` | The title link URL, similar to atom's related link. |
| `location` | `object` | The location for geotagged posts. |
| `author` | `object` | The author of this Post. |
| `replies` | `object` | The container of comments on this Post. |
| `published` | `string` | RFC 3339 date-time when this Post was published. |
| `etag` | `string` | Etag of the resource. |
| `kind` | `string` | The kind of this entity. Always blogger#post. |
| `title` | `string` | The title of the Post. |
| `trashed` | `string` | RFC 3339 date-time when this Post was last trashed. |
| `status` | `string` | Status of the post. Only set for admin-level requests. |
| `updated` | `string` | RFC 3339 date-time when this Post was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `posts_getByPath` | `SELECT` | `blogId, path` |
