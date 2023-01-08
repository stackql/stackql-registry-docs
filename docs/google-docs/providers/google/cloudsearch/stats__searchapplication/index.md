---
title: stats__searchapplication
hide_title: false
hide_table_of_contents: false
keywords:
  - stats__searchapplication
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
<tr><td><b>Name</b></td><td><code>stats__searchapplication</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.stats__searchapplication</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `stats` | `array` | Search application stats by date. |
| `averageSearchApplicationCount` | `string` | Average search application count for the given date range. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `stats_getSearchapplication` | `SELECT` |  |
