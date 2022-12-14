---
title: capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities
  - powerbi_dedicated
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
<tr><td><b>Name</b></td><td><code>capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_dedicated.capacities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the PowerBI Dedicated resource. |
| `name` | `string` | The name of the PowerBI Dedicated resource. |
| `type` | `string` | The type of the PowerBI Dedicated resource. |
| `location` | `string` | Location of the PowerBI Dedicated resource. |
| `properties` | `object` | Properties of Dedicated Capacity resource. |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Capacities_List` | `SELECT` | `subscriptionId` | Lists all the Dedicated capacities for the given subscription. |
| `Capacities_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Dedicated capacities for the given resource group. |
| `Capacities_Create` | `INSERT` | `dedicatedCapacityName, resourceGroupName, subscriptionId, data__sku` | Provisions the specified Dedicated capacity based on the configuration specified in the request. |
| `Capacities_Delete` | `DELETE` | `dedicatedCapacityName, resourceGroupName, subscriptionId` | Deletes the specified Dedicated capacity. |
| `Capacities_CheckNameAvailability` | `EXEC` | `location, subscriptionId` | Check the name availability in the target location. |
| `Capacities_GetDetails` | `EXEC` | `dedicatedCapacityName, resourceGroupName, subscriptionId` | Gets details about the specified dedicated capacity. |
| `Capacities_ListSkus` | `EXEC` | `subscriptionId` | Lists eligible SKUs for PowerBI Dedicated resource provider. |
| `Capacities_ListSkusForCapacity` | `EXEC` | `dedicatedCapacityName, resourceGroupName, subscriptionId` | Lists eligible SKUs for a PowerBI Dedicated resource. |
| `Capacities_Resume` | `EXEC` | `dedicatedCapacityName, resourceGroupName, subscriptionId` | Resumes operation of the specified Dedicated capacity instance. |
| `Capacities_Suspend` | `EXEC` | `dedicatedCapacityName, resourceGroupName, subscriptionId` | Suspends operation of the specified dedicated capacity instance. |
| `Capacities_Update` | `EXEC` | `dedicatedCapacityName, resourceGroupName, subscriptionId` | Updates the current state of the specified Dedicated capacity. |
