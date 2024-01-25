---
title: load_balancer_network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_network_interfaces
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
<tr><td><b>Name</b></td><td><code>load_balancer_network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_network_interfaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | NetworkInterface properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `loadBalancerName, resourceGroupName, subscriptionId` |
