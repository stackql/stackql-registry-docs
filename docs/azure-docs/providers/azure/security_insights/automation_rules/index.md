---
title: automation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_rules
  - security_insights
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
<tr><td><b>Id</b></td><td><code>azure.security_insights.automation_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Automation rule properties |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AutomationRules_Get` | `SELECT` | `automationRuleId, resourceGroupName, subscriptionId, workspaceName` | Gets the automation rule. |
| `AutomationRules_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all automation rules. |
| `AutomationRules_CreateOrUpdate` | `INSERT` | `automationRuleId, resourceGroupName, subscriptionId, workspaceName, data__properties` | Creates or updates the automation rule. |
| `AutomationRules_Delete` | `DELETE` | `automationRuleId, resourceGroupName, subscriptionId, workspaceName` | Delete the automation rule. |
