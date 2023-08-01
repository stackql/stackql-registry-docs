---
title: energy_services
hide_title: false
hide_table_of_contents: false
keywords:
  - energy_services
  - open_energy_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>energy_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.open_energy_platform.energy_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Geo-location where the resource lives. |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EnergyServices_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns oep resource for a given name. |
| `EnergyServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of oep resources.. |
| `EnergyServices_ListBySubscription` | `SELECT` | `subscriptionId` | Lists a collection of oep resources under the given Azure Subscription ID. |
| `EnergyServices_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId, data__location` | Method that gets called if subscribed for ResourceCreationBegin trigger. |
| `EnergyServices_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes oep resource |
| `EnergyServices_AddPartition` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Method that gets called if new partition is to be added in a resource. |
| `EnergyServices_ListPartitions` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Method that gets called when list of partitions is requested. |
| `EnergyServices_RemovePartition` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Method that gets called if new partition is to be removed from a resource. |
| `EnergyServices_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
