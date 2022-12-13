---
title: virtual_hub_route_table_v2s
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_route_table_v2s
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
<tr><td><b>Name</b></td><td><code>virtual_hub_route_table_v2s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_hub_route_table_v2s</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Parameters for VirtualHubRouteTableV2. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualHubRouteTableV2s_Get` | `SELECT` | `resourceGroupName, routeTableName, subscriptionId, virtualHubName` | Retrieves the details of a VirtualHubRouteTableV2. |
| `VirtualHubRouteTableV2s_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all VirtualHubRouteTableV2s. |
| `VirtualHubRouteTableV2s_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeTableName, subscriptionId, virtualHubName` | Creates a VirtualHubRouteTableV2 resource if it doesn't exist else updates the existing VirtualHubRouteTableV2. |
| `VirtualHubRouteTableV2s_Delete` | `DELETE` | `resourceGroupName, routeTableName, subscriptionId, virtualHubName` | Deletes a VirtualHubRouteTableV2. |
