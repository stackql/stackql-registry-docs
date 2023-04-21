---
title: service_map
hide_title: false
hide_table_of_contents: false
keywords:
  - service_map
  - tracing
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.service_map</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `edges` | `array` | List of service map edges. |
| `nodes` | `array` | List of service map nodes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getServiceMap` | `SELECT` |  |
