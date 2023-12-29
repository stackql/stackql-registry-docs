---
title: powerpacks
hide_title: false
hide_table_of_contents: false
keywords:
  - powerpacks
  - powerpack
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
<tr><td><b>Name</b></td><td><code>powerpacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.powerpack.powerpacks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the powerpack. |
| `attributes` | `object` | Powerpack attribute object. |
| `relationships` | `object` | Powerpack relationship object. |
| `type` | `string` | Type of widget, must be powerpack. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_powerpack` | `SELECT` | `powerpack_id, dd_site` | Get a powerpack. |
| `list_powerpacks` | `SELECT` | `dd_site` | Get a list of all powerpacks. |
| `create_powerpack` | `INSERT` | `dd_site` | Create a powerpack. |
| `delete_powerpack` | `DELETE` | `powerpack_id, dd_site` | Delete a powerpack. |
| `_get_powerpack` | `EXEC` | `powerpack_id, dd_site` | Get a powerpack. |
| `_list_powerpacks` | `EXEC` | `dd_site` | Get a list of all powerpacks. |
| `update_powerpack` | `EXEC` | `powerpack_id, dd_site` | Update a powerpack. |
