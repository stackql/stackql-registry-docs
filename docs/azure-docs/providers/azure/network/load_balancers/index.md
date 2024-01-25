---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
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
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the load balancer. |
| `sku` | `object` | SKU of a load balancer. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets the specified load balancer. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the load balancers in a resource group. |
| `create_or_update` | `INSERT` | `loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer. |
| `delete` | `DELETE` | `loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the load balancers in a resource group. |
| `migrate_to_ip_based` | `EXEC` | `groupName, loadBalancerName, subscriptionId` | Migrate load balancer to IP Based |
| `swap_public_ip_addresses` | `EXEC` | `location, subscriptionId` | Swaps VIPs between two load balancers. |
