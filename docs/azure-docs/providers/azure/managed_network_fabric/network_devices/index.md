---
title: network_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - network_devices
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
<tr><td><b>Name</b></td><td><code>network_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Device Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkDeviceName, resourceGroupName, subscriptionId` | Gets the Network Device resource details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the Network Device resources in a given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the Network Device resources in a given subscription. |
| `create` | `INSERT` | `networkDeviceName, resourceGroupName, subscriptionId, data__properties` | Create a Network Device resource |
| `delete` | `DELETE` | `networkDeviceName, resourceGroupName, subscriptionId` | Delete the Network Device resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the Network Device resources in a given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the Network Device resources in a given subscription. |
| `reboot` | `EXEC` | `networkDeviceName, resourceGroupName, subscriptionId` | Reboot the Network Device. |
| `refresh_configuration` | `EXEC` | `networkDeviceName, resourceGroupName, subscriptionId` | Refreshes the configuration the Network Device. |
| `update` | `EXEC` | `networkDeviceName, resourceGroupName, subscriptionId` | Update certain properties of the Network Device resource. |
| `upgrade` | `EXEC` | `networkDeviceName, resourceGroupName, subscriptionId` | Upgrades the version of the Network Device. |
