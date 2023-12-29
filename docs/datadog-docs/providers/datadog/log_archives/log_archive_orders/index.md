---
title: log_archive_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - log_archive_orders
  - log_archives
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
<tr><td><b>Name</b></td><td><code>log_archive_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.log_archives.log_archive_orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `attributes` | `object` | The attributes associated with the archive order. |
| `type` | `string` | Type of the archive order definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_logs_archive_order` | `SELECT` | `dd_site` | Get the current order of your archives.<br />This endpoint takes no JSON arguments. |
| `_get_logs_archive_order` | `EXEC` | `dd_site` | Get the current order of your archives.<br />This endpoint takes no JSON arguments. |
| `update_logs_archive_order` | `EXEC` | `dd_site` | Update the order of your archives. Since logs are processed sequentially, reordering an archive may change<br />the structure and content of the data processed by other archives.<br /><br />**Note**: Using the `PUT` method updates your archive's order by replacing the current order<br />with the new one. |
