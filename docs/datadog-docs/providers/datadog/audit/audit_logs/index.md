---
title: audit_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_logs
  - audit
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
<tr><td><b>Name</b></td><td><code>audit_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.audit.audit_logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the event. |
| `attributes` | `object` | JSON object containing all event attributes and their associated values. |
| `type` | `string` | Type of the event. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_audit_logs` | `SELECT` | `dd_site` | List endpoint returns events that match a Audit Logs search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to see your latest Audit Logs events.<br /><br />[1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination |
| `_list_audit_logs` | `EXEC` | `dd_site` | List endpoint returns events that match a Audit Logs search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to see your latest Audit Logs events.<br /><br />[1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination |
| `search_audit_logs` | `EXEC` | `dd_site` | List endpoint returns Audit Logs events that match an Audit search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to build complex Audit Logs events filtering and search.<br /><br />[1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination |
