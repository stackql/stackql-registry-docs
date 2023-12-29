---
title: cloud_workload_security_agent_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_workload_security_agent_rules
  - cloud_workload_security
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
<tr><td><b>Name</b></td><td><code>cloud_workload_security_agent_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.cloud_workload_security.cloud_workload_security_agent_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the Agent rule. |
| `attributes` | `object` | A Cloud Workload Security Agent rule returned by the API. |
| `type` | `string` | The type of the resource. The value should always be `agent_rule`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_cloud_workload_security_agent_rule` | `SELECT` | `agent_rule_id, dd_site` | Get the details of a specific Agent rule. |
| `list_cloud_workload_security_agent_rules` | `SELECT` | `dd_site` | Get the list of Agent rules. |
| `create_cloud_workload_security_agent_rule` | `INSERT` | `data__data, dd_site` | Create a new Agent rule with the given parameters. |
| `delete_cloud_workload_security_agent_rule` | `DELETE` | `agent_rule_id, dd_site` | Delete a specific Agent rule. |
| `_get_cloud_workload_security_agent_rule` | `EXEC` | `agent_rule_id, dd_site` | Get the details of a specific Agent rule. |
| `_list_cloud_workload_security_agent_rules` | `EXEC` | `dd_site` | Get the list of Agent rules. |
| `update_cloud_workload_security_agent_rule` | `EXEC` | `agent_rule_id, data__data, dd_site` | Update a specific Agent rule.<br />Returns the Agent rule object when the request is successful. |
