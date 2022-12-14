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
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `sku` | `object` | SKU of nat gateway. |
| `properties` | `object` | Nat Gateway properties. |
| `location` | `string` | Resource location. |
| `zones` | `array` | A list of availability zones denoting the zone in which Nat Gateway should be deployed. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NatGateways_Get` | `SELECT` | `natGatewayName, resourceGroupName, subscriptionId` | Gets the specified nat gateway in a specified resource group. |
| `NatGateways_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all nat gateways in a resource group. |
| `NatGateways_ListAll` | `SELECT` | `subscriptionId` | Gets all the Nat Gateways in a subscription. |
| `NatGateways_CreateOrUpdate` | `INSERT` | `natGatewayName, resourceGroupName, subscriptionId` | Creates or updates a nat gateway. |
| `NatGateways_Delete` | `DELETE` | `natGatewayName, resourceGroupName, subscriptionId` | Deletes the specified nat gateway. |
| `NatGateways_UpdateTags` | `EXEC` | `natGatewayName, resourceGroupName, subscriptionId` | Updates nat gateway tags. |
