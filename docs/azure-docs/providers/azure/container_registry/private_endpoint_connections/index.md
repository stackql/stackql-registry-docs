---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - container_registry
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | The properties of a private endpoint connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, registryName, resourceGroupName, subscriptionId` | Get the specified private endpoint connection associated with the container registry. |
| `PrivateEndpointConnections_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | List all private endpoint connections in a container registry. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `privateEndpointConnectionName, registryName, resourceGroupName, subscriptionId` | Update the state of specified private endpoint connection associated with the container registry. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, registryName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint connection associated with the container registry. |
