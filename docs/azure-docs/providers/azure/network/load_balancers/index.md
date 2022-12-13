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
| `properties` | `object` | Properties of the load balancer. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `sku` | `object` | SKU of a load balancer. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancers_Get` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets the specified load balancer. |
| `LoadBalancers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the load balancers in a resource group. |
| `LoadBalancers_ListAll` | `SELECT` | `subscriptionId` | Gets all the load balancers in a subscription. |
| `LoadBalancers_CreateOrUpdate` | `INSERT` | `loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer. |
| `LoadBalancers_Delete` | `DELETE` | `loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer. |
| `LoadBalancers_ListInboundNatRulePortMappings` | `EXEC` | `backendPoolName, groupName, loadBalancerName, subscriptionId` | List of inbound NAT rule port mappings. |
| `LoadBalancers_SwapPublicIpAddresses` | `EXEC` | `location, subscriptionId` | Swaps VIPs between two load balancers. |
| `LoadBalancers_UpdateTags` | `EXEC` | `loadBalancerName, resourceGroupName, subscriptionId` | Updates a load balancer tags. |
