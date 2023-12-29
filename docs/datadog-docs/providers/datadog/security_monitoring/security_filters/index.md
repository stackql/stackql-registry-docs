---
title: security_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - security_filters
  - security_monitoring
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
<tr><td><b>Name</b></td><td><code>security_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.security_monitoring.security_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the security filter. |
| `attributes` | `object` | The object describing a security filter. |
| `type` | `string` | The type of the resource. The value should always be `security_filters`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_security_filter` | `SELECT` | `security_filter_id, dd_site` | Get the details of a specific security filter.<br /><br />See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/)<br />for more examples. |
| `list_security_filters` | `SELECT` | `dd_site` | Get the list of configured security filters with their definitions. |
| `create_security_filter` | `INSERT` | `data__data, dd_site` | Create a security filter.<br /><br />See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/)<br />for more examples. |
| `delete_security_filter` | `DELETE` | `security_filter_id, dd_site` | Delete a specific security filter. |
| `_get_security_filter` | `EXEC` | `security_filter_id, dd_site` | Get the details of a specific security filter.<br /><br />See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/)<br />for more examples. |
| `_list_security_filters` | `EXEC` | `dd_site` | Get the list of configured security filters with their definitions. |
| `update_security_filter` | `EXEC` | `security_filter_id, data__data, dd_site` | Update a specific security filter.<br />Returns the security filter object when the request is successful. |
