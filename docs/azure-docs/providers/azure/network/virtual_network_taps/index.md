---
title: virtual_network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_taps
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
<tr><td><b>Name</b></td><td><code>virtual_network_taps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_taps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Virtual Network Tap properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, tapName` | Gets information about the specified virtual network tap. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the VirtualNetworkTaps in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, tapName` | Creates or updates a Virtual Network Tap. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, tapName` | Deletes the specified virtual network tap. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the VirtualNetworkTaps in a subscription. |
