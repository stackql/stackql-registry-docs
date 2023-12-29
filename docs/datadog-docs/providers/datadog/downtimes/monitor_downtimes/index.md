---
title: monitor_downtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_downtimes
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
<tr><td><b>Name</b></td><td><code>monitor_downtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.downtimes.monitor_downtimes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The downtime ID. |
| `attributes` | `object` | Downtime match details. |
| `type` | `string` | Monitor Downtime Match resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_monitor_downtimes` | `SELECT` | `monitor_id, dd_site` |
| `_list_monitor_downtimes` | `EXEC` | `monitor_id, dd_site` |
