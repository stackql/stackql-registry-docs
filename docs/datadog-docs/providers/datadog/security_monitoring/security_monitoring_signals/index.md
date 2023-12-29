---
title: security_monitoring_signals
hide_title: false
hide_table_of_contents: false
keywords:
  - security_monitoring_signals
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
<tr><td><b>Name</b></td><td><code>security_monitoring_signals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.security_monitoring.security_monitoring_signals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of the security signal. |
| `attributes` | `object` | The object containing all signal attributes and their<br />associated values. |
| `type` | `string` | The type of event. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_security_monitoring_signal` | `SELECT` | `signal_id, dd_site` | Get a signal's details. |
| `list_security_monitoring_signals` | `SELECT` | `dd_site` | The list endpoint returns security signals that match a search query.<br />Both this endpoint and the POST endpoint can be used interchangeably when listing<br />security signals. |
| `_get_security_monitoring_signal` | `EXEC` | `signal_id, dd_site` | Get a signal's details. |
| `_list_security_monitoring_signals` | `EXEC` | `dd_site` | The list endpoint returns security signals that match a search query.<br />Both this endpoint and the POST endpoint can be used interchangeably when listing<br />security signals. |
| `edit_security_monitoring_signal_assignee` | `EXEC` | `signal_id, data__data, dd_site` | Modify the triage assignee of a security signal. |
| `edit_security_monitoring_signal_incidents` | `EXEC` | `signal_id, data__data, dd_site` | Change the related incidents for a security signal. |
| `edit_security_monitoring_signal_state` | `EXEC` | `signal_id, data__data, dd_site` | Change the triage state of a security signal. |
| `search_security_monitoring_signals` | `EXEC` | `dd_site` | Returns security signals that match a search query.<br />Both this endpoint and the GET endpoint can be used interchangeably for listing<br />security signals. |
