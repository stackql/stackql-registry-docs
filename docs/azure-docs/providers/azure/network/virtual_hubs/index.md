---
title: virtual_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs
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
<tr><td><b>Name</b></td><td><code>virtual_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `kind` | `string` | Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Parameters for VirtualHub. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualHubs_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of a VirtualHub. |
| `VirtualHubs_List` | `SELECT` | `subscriptionId` | Lists all the VirtualHubs in a subscription. |
| `VirtualHubs_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the VirtualHubs in a resource group. |
| `VirtualHubs_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualHubName, data__location` | Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub. |
| `VirtualHubs_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualHubName` | Deletes a VirtualHub. |
| `VirtualHubs_GetEffectiveVirtualHubRoutes` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Gets the effective routes configured for the Virtual Hub resource or the specified resource . |
| `VirtualHubs_GetInboundRoutes` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Gets the inbound routes configured for the Virtual Hub on a particular connection. |
| `VirtualHubs_GetOutboundRoutes` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Gets the outbound routes configured for the Virtual Hub on a particular connection. |
| `VirtualHubs_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Updates VirtualHub tags. |
