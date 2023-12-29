---
title: downtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - downtimes
  - downtimes
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>downtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.downtimes.downtimes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The downtime ID. |
| `attributes` | `object` | Downtime details. |
| `relationships` | `object` | All relationships associated with downtime. |
| `type` | `string` | Downtime resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_downtime` | `SELECT` | `downtime_id, dd_site` | Get downtime detail by `downtime_id`. |
| `list_downtimes` | `SELECT` | `dd_site` | Get all scheduled downtimes. |
| `create_downtime` | `INSERT` | `data__data, dd_site` | Schedule a downtime. |
| `_get_downtime` | `EXEC` | `downtime_id, dd_site` | Get downtime detail by `downtime_id`. |
| `_list_downtimes` | `EXEC` | `dd_site` | Get all scheduled downtimes. |
| `cancel_downtime` | `EXEC` | `downtime_id, dd_site` | Cancel a downtime. |
| `update_downtime` | `EXEC` | `downtime_id, data__data, dd_site` | Update a downtime by `downtime_id`. |
