---
title: i18n_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - i18n_regions
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
<tr><td><b>Name</b></td><td><code>i18n_regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.i18n_regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the i18n region. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#i18nRegion". |
| `snippet` | `object` | Basic details about an i18n region, such as region code and human-readable name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `i18nRegions_list` | `SELECT` | `part` |
