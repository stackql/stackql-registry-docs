---
title: apm_retention_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - apm_retention_filters
  - apm_retention_filters
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
<tr><td><b>Name</b></td><td><code>apm_retention_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.apm_retention_filters.apm_retention_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the retention filter. |
| `attributes` | `object` | The attributes of the retention filter. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_apm_retention_filter` | `SELECT` | `filter_id, dd_site` | Get an APM retention filter. |
| `list_apm_retention_filters` | `SELECT` | `dd_site` | Get the list of APM retention filters. |
| `create_apm_retention_filter` | `INSERT` | `data__data, dd_site` | Create a retention filter to index spans in your organization.<br />Returns the retention filter definition when the request is successful. |
| `delete_apm_retention_filter` | `DELETE` | `filter_id, dd_site` | Delete a specific retention filter from your organization. |
| `_get_apm_retention_filter` | `EXEC` | `filter_id, dd_site` | Get an APM retention filter. |
| `_list_apm_retention_filters` | `EXEC` | `dd_site` | Get the list of APM retention filters. |
| `reorder_apm_retention_filters` | `EXEC` | `data__data, dd_site` | Re-order the execution order of retention filters. |
| `update_apm_retention_filter` | `EXEC` | `filter_id, data__data, dd_site` | Update a retention filter from your organization. |
