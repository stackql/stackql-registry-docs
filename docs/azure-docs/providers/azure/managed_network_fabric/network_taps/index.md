---
title: network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - network_taps
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
<tr><td><b>Name</b></td><td><code>network_taps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_taps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Tap Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkTapName, resourceGroupName, subscriptionId` | Retrieves details of this Network Tap. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Displays Network Taps list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Displays Network Taps list by subscription GET method. |
| `create` | `INSERT` | `networkTapName, resourceGroupName, subscriptionId, data__properties` | Creates a Network Tap. |
| `delete` | `DELETE` | `networkTapName, resourceGroupName, subscriptionId` | Deletes Network Tap. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Displays Network Taps list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Displays Network Taps list by subscription GET method. |
| `resync` | `EXEC` | `networkTapName, resourceGroupName, subscriptionId` | Implements the operation to the underlying resources. |
| `update` | `EXEC` | `networkTapName, resourceGroupName, subscriptionId` | API to update certain properties of the Network Tap resource. |
