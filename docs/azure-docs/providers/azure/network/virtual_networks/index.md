---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the virtual network. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets the specified virtual network by resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all virtual networks in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Creates or updates a virtual network in the specified resource group. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deletes the specified virtual network. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all virtual networks in a resource group. |
| `check_ip_address_availability` | `EXEC` | `ipAddress, resourceGroupName, subscriptionId, virtualNetworkName` | Checks whether a private IP address is available for use. |
