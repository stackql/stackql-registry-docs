---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.subnets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the subnet. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Gets the specified subnet by virtual network and resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets all subnets in a virtual network. |
| `create_or_update` | `INSERT` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Creates or updates a subnet in the specified virtual network. |
| `delete` | `DELETE` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Deletes the specified subnet. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets all subnets in a virtual network. |
| `prepare_network_policies` | `EXEC` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Prepares a subnet by applying network intent policies. |
| `unprepare_network_policies` | `EXEC` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Unprepares a subnet by removing network intent policies. |
