---
title: droplet_bandwidth
hide_title: false
hide_table_of_contents: false
keywords:
  - droplet_bandwidth
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
<tr><td><b>Name</b></td><td><code>droplet_bandwidth</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.monitoring.droplet_bandwidth</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metric` | `object` | An object containing the metric labels. |
| `values` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_dropletBandwidthMetrics` | `SELECT` | `direction, end, host_id, interface, start` |
| `_get_dropletBandwidthMetrics` | `EXEC` | `direction, end, host_id, interface, start` |
