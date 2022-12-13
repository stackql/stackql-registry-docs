---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - system_center_vm_manager
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
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworks_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Implements VirtualNetwork GET method. |
| `VirtualNetworks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualNetworks in a resource group. |
| `VirtualNetworks_ListBySubscription` | `SELECT` | `subscriptionId` | List of VirtualNetworks in a subscription. |
| `VirtualNetworks_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName, data__extendedLocation, data__location, data__properties` | Onboards the ScVmm virtual network as an Azure virtual network resource. |
| `VirtualNetworks_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deregisters the ScVmm virtual network from Azure. |
| `VirtualNetworks_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Updates the VirtualNetworks resource. |
