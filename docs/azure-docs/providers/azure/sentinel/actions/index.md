---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `etag` | `string` | Etag of the action. |
| `properties` | `object` | Action property bag. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `actionId, resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets the action of alert rule. |
| `list_by_alert_rule` | `SELECT` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets all actions of alert rule. |
| `create_or_update` | `INSERT` | `actionId, resourceGroupName, ruleId, subscriptionId, workspaceName` | Creates or updates the action of alert rule. |
| `delete` | `DELETE` | `actionId, resourceGroupName, ruleId, subscriptionId, workspaceName` | Delete the action of alert rule. |
| `_list_by_alert_rule` | `EXEC` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets all actions of alert rule. |
