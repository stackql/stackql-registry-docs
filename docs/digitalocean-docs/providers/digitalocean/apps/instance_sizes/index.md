---
title: instance_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_sizes
  - apps
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
<tr><td><b>Name</b></td><td><code>instance_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.instance_sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `cpu_type` | `string` |
| `tier_downgrade_to` | `string` |
| `usd_per_month` | `string` |
| `slug` | `string` |
| `cpus` | `string` |
| `memory_bytes` | `string` |
| `tier_upgrade_to` | `string` |
| `usd_per_second` | `string` |
| `tier_slug` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_instanceSize` | `SELECT` | `slug` | Retrieve information about a specific instance size for `service`, `worker`, and `job` components. |
| `list_instanceSizes` | `SELECT` |  | List all instance sizes for `service`, `worker`, and `job` components. |
| `_get_instanceSize` | `EXEC` | `slug` | Retrieve information about a specific instance size for `service`, `worker`, and `job` components. |
| `_list_instanceSizes` | `EXEC` |  | List all instance sizes for `service`, `worker`, and `job` components. |
