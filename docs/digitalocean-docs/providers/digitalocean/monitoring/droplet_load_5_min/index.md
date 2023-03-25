---
title: droplet_load_5_min
hide_title: false
hide_table_of_contents: false
keywords:
  - droplet_load_5_min
  - monitoring
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>droplet_load_5_min</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.monitoring.droplet_load_5_min</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metric` | `object` | An object containing the metric labels. |
| `values` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_dropletLoad5Metrics` | `SELECT` | `end, host_id, start` |
| `_get_dropletLoad5Metrics` | `EXEC` | `end, host_id, start` |
