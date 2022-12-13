---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Action property bag. |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Actions_Get` | `SELECT` | `actionId, resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets the action of alert rule. |
| `Actions_ListByAlertRule` | `SELECT` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets all actions of alert rule. |
| `Actions_CreateOrUpdate` | `INSERT` | `actionId, resourceGroupName, ruleId, subscriptionId, workspaceName` | Creates or updates the action of alert rule. |
| `Actions_Delete` | `DELETE` | `actionId, resourceGroupName, ruleId, subscriptionId, workspaceName` | Delete the action of alert rule. |
