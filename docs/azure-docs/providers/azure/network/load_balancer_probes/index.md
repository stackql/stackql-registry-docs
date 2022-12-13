---
title: load_balancer_probes
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_probes
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
<tr><td><b>Name</b></td><td><code>load_balancer_probes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_probes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of probes used by the load balancer. This name can be used to access the resource. |
| `properties` | `object` | Load balancer probe resource. |
| `type` | `string` | Type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerProbes_Get` | `SELECT` | `loadBalancerName, probeName, resourceGroupName, subscriptionId` | Gets load balancer probe. |
| `LoadBalancerProbes_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancer probes. |
