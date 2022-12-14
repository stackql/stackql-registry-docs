---
title: interface_load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - interface_load_balancers
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
<tr><td><b>Name</b></td><td><code>interface_load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.interface_load_balancers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
| `sku` | `object` | SKU of a load balancer. |
| `properties` | `object` | Properties of the load balancer. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NetworkInterfaceLoadBalancers_List` | `SELECT` | `networkInterfaceName, resourceGroupName, subscriptionId` |
