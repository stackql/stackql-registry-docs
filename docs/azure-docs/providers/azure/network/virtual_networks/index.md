---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the virtual network. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworks_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets the specified virtual network by resource group. |
| `VirtualNetworks_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all virtual networks in a resource group. |
| `VirtualNetworks_ListAll` | `SELECT` | `subscriptionId` | Gets all virtual networks in a subscription. |
| `VirtualNetworks_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Creates or updates a virtual network in the specified resource group. |
| `VirtualNetworks_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deletes the specified virtual network. |
| `VirtualNetworks_CheckIPAddressAvailability` | `EXEC` | `ipAddress, resourceGroupName, subscriptionId, virtualNetworkName` | Checks whether a private IP address is available for use. |
| `VirtualNetworks_ListDdosProtectionStatus` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets the Ddos Protection Status of all IP Addresses under the Virtual Network |
| `VirtualNetworks_ListUsage` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Lists usage stats. |
| `VirtualNetworks_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Updates a virtual network tags. |
