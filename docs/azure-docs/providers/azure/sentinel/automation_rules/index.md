---
title: automation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_rules
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
<tr><td><b>Name</b></td><td><code>automation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.automation_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Automation rule properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationRuleId, resourceGroupName, subscriptionId, workspaceName` | Gets the automation rule. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all automation rules. |
| `create_or_update` | `INSERT` | `automationRuleId, resourceGroupName, subscriptionId, workspaceName, data__properties` | Creates or updates the automation rule. |
| `delete` | `DELETE` | `automationRuleId, resourceGroupName, subscriptionId, workspaceName` | Delete the automation rule. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all automation rules. |
