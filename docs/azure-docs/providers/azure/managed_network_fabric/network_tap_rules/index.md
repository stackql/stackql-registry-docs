---
title: network_tap_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - network_tap_rules
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
<tr><td><b>Name</b></td><td><code>network_tap_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_tap_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Tap Rule Properties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkTapRuleName, resourceGroupName, subscriptionId` | Get Network Tap Rule resource details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the Network Tap Rule resources in the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the Network Tap Rule resources in the given subscription. |
| `create` | `INSERT` | `networkTapRuleName, resourceGroupName, subscriptionId, data__properties` | Create Network Tap Rule resource. |
| `delete` | `DELETE` | `networkTapRuleName, resourceGroupName, subscriptionId` | Delete Network Tap Rule resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the Network Tap Rule resources in the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the Network Tap Rule resources in the given subscription. |
| `resync` | `EXEC` | `networkTapRuleName, resourceGroupName, subscriptionId` | Implements the operation to the underlying resources. |
| `update` | `EXEC` | `networkTapRuleName, resourceGroupName, subscriptionId` | Update certain properties of the Network Tap Rule resource. |
| `validate_configuration` | `EXEC` | `networkTapRuleName, resourceGroupName, subscriptionId` | Implements the operation to the underlying resources. |
