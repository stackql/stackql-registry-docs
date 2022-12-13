---
title: load_balancer_backend_address_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_backend_address_pools
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
<tr><td><b>Name</b></td><td><code>load_balancer_backend_address_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_backend_address_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of backend address pools used by the load balancer. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the backend address pool. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerBackendAddressPools_Get` | `SELECT` | `backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId` | Gets load balancer backend address pool. |
| `LoadBalancerBackendAddressPools_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancer backed address pools. |
| `LoadBalancerBackendAddressPools_CreateOrUpdate` | `INSERT` | `backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer backend address pool. |
| `LoadBalancerBackendAddressPools_Delete` | `DELETE` | `backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer backend address pool. |
