---
title: blogs__by_url
hide_title: false
hide_table_of_contents: false
keywords:
  - blogs__by_url
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
<tr><td><b>Name</b></td><td><code>blogs__by_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.blogs__by_url</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this resource. |
| `name` | `string` | The name of this blog. This is displayed as the title. |
| `description` | `string` | The description of this blog. This is displayed underneath the title. |
| `updated` | `string` | RFC 3339 date-time when this blog was last updated. |
| `kind` | `string` | The kind of this entry. Always blogger#blog. |
| `published` | `string` | RFC 3339 date-time when this blog was published. |
| `locale` | `object` | The locale this Blog is set to. |
| `pages` | `object` | The container of pages in this blog. |
| `posts` | `object` | The container of posts in this blog. |
| `customMetaData` | `string` | The JSON custom meta-data for the Blog. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `status` | `string` | The status of the blog. |
| `url` | `string` | The URL where this blog is published. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `blogs_getByUrl` | `SELECT` | `url` |
