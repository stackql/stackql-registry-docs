---
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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
<tr><td><b>Name</b></td><td><code>nat_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.nat_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Nat Gateway properties. |
| `sku` | `object` | SKU of nat gateway. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting the zone in which Nat Gateway should be deployed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `natGatewayName, resourceGroupName, subscriptionId` | Gets the specified nat gateway in a specified resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all nat gateways in a resource group. |
| `create_or_update` | `INSERT` | `natGatewayName, resourceGroupName, subscriptionId` | Creates or updates a nat gateway. |
| `delete` | `DELETE` | `natGatewayName, resourceGroupName, subscriptionId` | Deletes the specified nat gateway. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all nat gateways in a resource group. |
