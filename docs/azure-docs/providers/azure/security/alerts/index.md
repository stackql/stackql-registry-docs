---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - security
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | describes security alert properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_List` | `SELECT` | `api-version, subscriptionId` | List all the alerts that are associated with the subscription |
| `Alerts_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List all the alerts that are associated with the resource group |
| `Alerts_GetResourceGroupLevel` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Get an alert that is associated a resource group or a resource in a resource group |
| `Alerts_GetSubscriptionLevel` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Get an alert that is associated with a subscription |
| `Alerts_ListResourceGroupLevelByRegion` | `EXEC` | `api-version, ascLocation, resourceGroupName, subscriptionId` | List all the alerts that are associated with the resource group that are stored in a specific location |
| `Alerts_ListSubscriptionLevelByRegion` | `EXEC` | `api-version, ascLocation, subscriptionId` | List all the alerts that are associated with the subscription that are stored in a specific location |
| `Alerts_Simulate` | `EXEC` | `api-version, ascLocation, subscriptionId` | Simulate security alerts |
| `Alerts_UpdateResourceGroupLevelStateToActivate` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateResourceGroupLevelStateToDismiss` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateResourceGroupLevelStateToInProgress` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateResourceGroupLevelStateToResolve` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToActivate` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToDismiss` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToInProgress` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToResolve` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
