---
title: network_racks
hide_title: false
hide_table_of_contents: false
keywords:
  - network_racks
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
<tr><td><b>Name</b></td><td><code>network_racks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_racks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Rack Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkRackName, resourceGroupName, subscriptionId` | Get Network Rack resource details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all Network Rack resources in the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all Network Rack resources in the given subscription |
| `create` | `INSERT` | `networkRackName, resourceGroupName, subscriptionId, data__location, data__properties` | Create Network Rack resource. |
| `delete` | `DELETE` | `networkRackName, resourceGroupName, subscriptionId` | Delete Network Rack resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all Network Rack resources in the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all Network Rack resources in the given subscription |
| `update` | `EXEC` | `networkRackName, resourceGroupName, subscriptionId` | Update certain properties of the Network Rack resource. |
