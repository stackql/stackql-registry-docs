---
title: monitor_config_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_config_policies
  - monitors
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
<tr><td><b>Name</b></td><td><code>monitor_config_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.monitors.monitor_config_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this monitor configuration policy. |
| `attributes` | `object` | Policy and policy type for a monitor configuration policy. |
| `type` | `string` | Monitor configuration policy resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_monitor_config_policy` | `SELECT` | `policy_id, dd_site` | Get a monitor configuration policy by `policy_id`. |
| `list_monitor_config_policies` | `SELECT` | `dd_site` | Get all monitor configuration policies. |
| `create_monitor_config_policy` | `INSERT` | `data__data, dd_site` | Create a monitor configuration policy. |
| `delete_monitor_config_policy` | `DELETE` | `policy_id, dd_site` | Delete a monitor configuration policy. |
| `_get_monitor_config_policy` | `EXEC` | `policy_id, dd_site` | Get a monitor configuration policy by `policy_id`. |
| `_list_monitor_config_policies` | `EXEC` | `dd_site` | Get all monitor configuration policies. |
| `update_monitor_config_policy` | `EXEC` | `policy_id, data__data, dd_site` | Edit a monitor configuration policy. |
