---
title: blogs
hide_title: false
hide_table_of_contents: false
keywords:
  - blogs
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
<tr><td><b>Name</b></td><td><code>blogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.blogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this resource. |
| `name` | `string` | The name of this blog. This is displayed as the title. |
| `description` | `string` | The description of this blog. This is displayed underneath the title. |
| `status` | `string` | The status of the blog. |
| `published` | `string` | RFC 3339 date-time when this blog was published. |
| `locale` | `object` | The locale this Blog is set to. |
| `url` | `string` | The URL where this blog is published. |
| `posts` | `object` | The container of posts in this blog. |
| `customMetaData` | `string` | The JSON custom meta-data for the Blog. |
| `kind` | `string` | The kind of this entry. Always blogger#blog. |
| `pages` | `object` | The container of pages in this blog. |
| `updated` | `string` | RFC 3339 date-time when this blog was last updated. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `blogId` |
