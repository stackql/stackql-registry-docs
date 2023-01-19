---
title: stats_index
hide_title: false
hide_table_of_contents: false
keywords:
  - stats_index
  - cloudsearch
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stats_index</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.stats_index</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `averageIndexedItemCount` | `string` | Average item count for the given date range for which billing is done. |
| `stats` | `array` | Summary of indexed item counts, one for each day in the requested range. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `stats_getIndex` | `SELECT` |  |
