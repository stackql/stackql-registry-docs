---
title: alert_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rules
  - monitor
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
<tr><td><b>Id</b></td><td><code>azure.monitor.alert_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | An alert rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AlertRules_Get` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` | Gets a classic metric alert rule |
| `AlertRules_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List the classic metric alert rules within a resource group. |
| `AlertRules_ListBySubscription` | `SELECT` | `subscriptionId` | List the classic metric alert rules within a subscription. |
| `AlertRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, ruleName, subscriptionId, data__properties` | Creates or updates a classic metric alert rule. |
| `AlertRules_Delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Deletes a classic metric alert rule |
| `AlertRules_Update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Updates an existing classic metric AlertRuleResource. To update other fields use the CreateOrUpdate method. |
