---
title: neighbor_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - neighbor_groups
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
<tr><td><b>Name</b></td><td><code>neighbor_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.neighbor_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Neighbor Group Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `neighborGroupName, resourceGroupName, subscriptionId` | Gets the Neighbor Group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Displays NeighborGroups list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Displays NeighborGroups list by subscription GET method. |
| `create` | `INSERT` | `neighborGroupName, resourceGroupName, subscriptionId, data__properties` | Implements the Neighbor Group PUT method. |
| `delete` | `DELETE` | `neighborGroupName, resourceGroupName, subscriptionId` | Implements Neighbor Group DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Displays NeighborGroups list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Displays NeighborGroups list by subscription GET method. |
| `update` | `EXEC` | `neighborGroupName, resourceGroupName, subscriptionId` | Updates the Neighbor Group. |
