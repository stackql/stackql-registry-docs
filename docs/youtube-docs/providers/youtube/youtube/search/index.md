---
title: search
hide_title: false
hide_table_of_contents: false
keywords:
  - search
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
<tr><td><b>Name</b></td><td><code>search</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.search</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `object` | A resource id is a generic reference that points to another YouTube resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#searchResult". |
| `snippet` | `object` | Basic details about a search result, including title, description and thumbnails of the item referenced by the search result. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `part` |
