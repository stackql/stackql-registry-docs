---
title: load_balancer_frontend_ip_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_frontend_ip_configurations
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
<tr><td><b>Name</b></td><td><code>load_balancer_frontend_ip_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_frontend_ip_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of frontend IP configurations used by the load balancer. This name can be used to access the resource. |
| `type` | `string` | Type of the resource. |
| `zones` | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of Frontend IP Configuration of the load balancer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerFrontendIPConfigurations_Get` | `SELECT` | `frontendIPConfigurationName, loadBalancerName, resourceGroupName, subscriptionId` | Gets load balancer frontend IP configuration. |
| `LoadBalancerFrontendIPConfigurations_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancer frontend IP configurations. |
