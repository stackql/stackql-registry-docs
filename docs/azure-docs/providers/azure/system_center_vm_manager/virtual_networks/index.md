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
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Implements VirtualNetwork GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualNetworks in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List of VirtualNetworks in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName, data__extendedLocation, data__properties` | Onboards the ScVmm virtual network as an Azure virtual network resource. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deregisters the ScVmm virtual network from Azure. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List of VirtualNetworks in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List of VirtualNetworks in a subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Updates the VirtualNetworks resource. |
