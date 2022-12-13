---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - data_factory
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
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.managed_private_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | Properties of a managed private endpoint |
| `type` | `string` | The resource type. |
| `etag` | `string` | Etag identifies change in the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedPrivateEndpoints_Get` | `SELECT` | `api-version, factoryName, managedPrivateEndpointName, managedVirtualNetworkName, resourceGroupName, subscriptionId` | Gets a managed private endpoint. |
| `ManagedPrivateEndpoints_ListByFactory` | `SELECT` | `api-version, factoryName, managedVirtualNetworkName, resourceGroupName, subscriptionId` | Lists managed private endpoints. |
| `ManagedPrivateEndpoints_CreateOrUpdate` | `INSERT` | `api-version, factoryName, managedPrivateEndpointName, managedVirtualNetworkName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a managed private endpoint. |
| `ManagedPrivateEndpoints_Delete` | `DELETE` | `api-version, factoryName, managedPrivateEndpointName, managedVirtualNetworkName, resourceGroupName, subscriptionId` | Deletes a managed private endpoint. |
