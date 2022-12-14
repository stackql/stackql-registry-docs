---
title: load_balancer_load_balancing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_load_balancing_rules
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
<tr><td><b>Name</b></td><td><code>load_balancer_load_balancing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_load_balancing_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of load balancing rules used by the load balancer. This name can be used to access the resource. |
| `type` | `string` | Type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the load balancer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerLoadBalancingRules_Get` | `SELECT` | `loadBalancerName, loadBalancingRuleName, resourceGroupName, subscriptionId` | Gets the specified load balancer load balancing rule. |
| `LoadBalancerLoadBalancingRules_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancing rules in a load balancer. |
