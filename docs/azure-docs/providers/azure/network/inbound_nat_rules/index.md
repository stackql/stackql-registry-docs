---
title: inbound_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_nat_rules
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
<tr><td><b>Name</b></td><td><code>inbound_nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.inbound_nat_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the inbound NAT rule. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId` | Gets the specified load balancer inbound NAT rule. |
| `list` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the inbound NAT rules in a load balancer. |
| `create_or_update` | `INSERT` | `inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer inbound NAT rule. |
| `delete` | `DELETE` | `inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer inbound NAT rule. |
| `_list` | `EXEC` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the inbound NAT rules in a load balancer. |
