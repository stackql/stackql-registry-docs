---
title: droplet_filesystem_free
hide_title: false
hide_table_of_contents: false
keywords:
  - droplet_filesystem_free
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
<tr><td><b>Name</b></td><td><code>droplet_filesystem_free</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.monitoring.droplet_filesystem_free</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metric` | `object` | An object containing the metric labels. |
| `values` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_dropletFilesystemFreeMetrics` | `SELECT` | `end, host_id, start` |
| `_get_dropletFilesystemFreeMetrics` | `EXEC` | `end, host_id, start` |
