---
title: network_fabric_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabric_controllers
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
<tr><td><b>Name</b></td><td><code>network_fabric_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_fabric_controllers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | NetworkFabricControllerProperties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFabricControllerName, resourceGroupName, subscriptionId` | Shows the provisioning status of Network Fabric Controller. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the NetworkFabricControllers thats available in the resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the NetworkFabricControllers by subscription. |
| `create` | `INSERT` | `networkFabricControllerName, resourceGroupName, subscriptionId, data__properties` | Creates a Network Fabric Controller. |
| `delete` | `DELETE` | `networkFabricControllerName, resourceGroupName, subscriptionId` | Deletes the Network Fabric Controller resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the NetworkFabricControllers thats available in the resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the NetworkFabricControllers by subscription. |
| `update` | `EXEC` | `networkFabricControllerName, resourceGroupName, subscriptionId` | Updates are currently not supported for the Network Fabric Controller resource. |
