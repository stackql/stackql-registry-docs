---
title: page_views
hide_title: false
hide_table_of_contents: false
keywords:
  - page_views
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
<tr><td><b>Name</b></td><td><code>page_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.page_views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `blogId` | `string` | Blog Id. |
| `counts` | `array` | The container of posts in this blog. |
| `kind` | `string` | The kind of this entry. Always blogger#page_views. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `pageViews_get` | `SELECT` | `blogId` |
