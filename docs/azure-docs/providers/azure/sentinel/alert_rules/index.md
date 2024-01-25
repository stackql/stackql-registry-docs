---
title: alert_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rules
  - sentinel
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.alert_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the alert rule |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets the alert rule. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all alert rules. |
| `create_or_update` | `INSERT` | `resourceGroupName, ruleId, subscriptionId, workspaceName, data__kind` | Creates or updates the alert rule. |
| `delete` | `DELETE` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Delete the alert rule. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all alert rules. |
