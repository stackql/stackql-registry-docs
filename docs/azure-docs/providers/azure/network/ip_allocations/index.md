---
title: ip_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_allocations
  - network
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
<tr><td><b>Name</b></td><td><code>ip_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.ip_allocations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the IpAllocation. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IpAllocations_Get` | `SELECT` | `ipAllocationName, resourceGroupName, subscriptionId` | Gets the specified IpAllocation by resource group. |
| `IpAllocations_List` | `SELECT` | `subscriptionId` | Gets all IpAllocations in a subscription. |
| `IpAllocations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all IpAllocations in a resource group. |
| `IpAllocations_CreateOrUpdate` | `INSERT` | `ipAllocationName, resourceGroupName, subscriptionId` | Creates or updates an IpAllocation in the specified resource group. |
| `IpAllocations_Delete` | `DELETE` | `ipAllocationName, resourceGroupName, subscriptionId` | Deletes the specified IpAllocation. |
| `IpAllocations_UpdateTags` | `EXEC` | `ipAllocationName, resourceGroupName, subscriptionId` | Updates a IpAllocation tags. |
