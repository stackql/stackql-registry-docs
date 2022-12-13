---
title: private_link_services
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services
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
<tr><td><b>Name</b></td><td><code>private_link_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_link_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the private link service. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkServices_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets the specified private link service by resource group. |
| `PrivateLinkServices_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all private link services in a resource group. |
| `PrivateLinkServices_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all private link service in a subscription. |
| `PrivateLinkServices_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Creates or updates an private link service in the specified resource group. |
| `PrivateLinkServices_Delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Deletes the specified private link service. |
| `PrivateLinkServices_CheckPrivateLinkServiceVisibility` | `EXEC` | `location, subscriptionId` | Checks whether the subscription is visible to private link service. |
| `PrivateLinkServices_CheckPrivateLinkServiceVisibilityByResourceGroup` | `EXEC` | `location, resourceGroupName, subscriptionId` | Checks whether the subscription is visible to private link service in the specified resource group. |
| `PrivateLinkServices_DeletePrivateEndpointConnection` | `EXEC` | `peConnectionName, resourceGroupName, serviceName, subscriptionId` | Delete private end point connection for a private link service in a subscription. |
| `PrivateLinkServices_GetPrivateEndpointConnection` | `EXEC` | `peConnectionName, resourceGroupName, serviceName, subscriptionId` | Get the specific private end point connection by specific private link service in the resource group. |
| `PrivateLinkServices_ListAutoApprovedPrivateLinkServices` | `EXEC` | `location, subscriptionId` | Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region. |
| `PrivateLinkServices_ListAutoApprovedPrivateLinkServicesByResourceGroup` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region. |
| `PrivateLinkServices_ListPrivateEndpointConnections` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets all private end point connections for a specific private link service. |
| `PrivateLinkServices_UpdatePrivateEndpointConnection` | `EXEC` | `peConnectionName, resourceGroupName, serviceName, subscriptionId` | Approve or reject private end point connection for a private link service in a subscription. |
