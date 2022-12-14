---
title: metric_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts
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
<tr><td><b>Name</b></td><td><code>metric_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | An alert rule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MetricAlerts_Get` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` | Retrieve an alert rule definition. |
| `MetricAlerts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve alert rule definitions in a resource group. |
| `MetricAlerts_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve alert rule definitions in a subscription. |
| `MetricAlerts_CreateOrUpdate` | `INSERT` | `resourceGroupName, ruleName, subscriptionId, data__properties` | Create or update an metric alert definition. |
| `MetricAlerts_Delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Delete an alert rule definition. |
| `MetricAlerts_Update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Update an metric alert definition. |
