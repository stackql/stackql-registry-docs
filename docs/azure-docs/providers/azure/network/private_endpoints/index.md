---
title: private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoints
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
<tr><td><b>Name</b></td><td><code>private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the private endpoint. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpoints_Get` | `SELECT` | `privateEndpointName, resourceGroupName, subscriptionId` | Gets the specified private endpoint by resource group. |
| `PrivateEndpoints_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all private endpoints in a resource group. |
| `PrivateEndpoints_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all private endpoints in a subscription. |
| `PrivateEndpoints_CreateOrUpdate` | `INSERT` | `privateEndpointName, resourceGroupName, subscriptionId` | Creates or updates an private endpoint in the specified resource group. |
| `PrivateEndpoints_Delete` | `DELETE` | `privateEndpointName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint. |
