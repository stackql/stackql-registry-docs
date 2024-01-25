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
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the IpAllocation. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ipAllocationName, resourceGroupName, subscriptionId` | Gets the specified IpAllocation by resource group. |
| `list` | `SELECT` | `subscriptionId` | Gets all IpAllocations in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all IpAllocations in a resource group. |
| `create_or_update` | `INSERT` | `ipAllocationName, resourceGroupName, subscriptionId` | Creates or updates an IpAllocation in the specified resource group. |
| `delete` | `DELETE` | `ipAllocationName, resourceGroupName, subscriptionId` | Deletes the specified IpAllocation. |
| `_list` | `EXEC` | `subscriptionId` | Gets all IpAllocations in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all IpAllocations in a resource group. |
