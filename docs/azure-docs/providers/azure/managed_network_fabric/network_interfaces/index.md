---
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_interfaces</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId` | Get the Network Interface resource details. |
| `list_by_network_device` | `SELECT` | `networkDeviceName, resourceGroupName, subscriptionId` | List all the Network Interface resources in a given resource group. |
| `create` | `INSERT` | `networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId, data__properties` | Create a Network Interface resource. |
| `delete` | `DELETE` | `networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId` | Delete the Network Interface resource. |
| `_list_by_network_device` | `EXEC` | `networkDeviceName, resourceGroupName, subscriptionId` | List all the Network Interface resources in a given resource group. |
| `update` | `EXEC` | `networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId` | Update certain properties of the Network Interface resource. |
