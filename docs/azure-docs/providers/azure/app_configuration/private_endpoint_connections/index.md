---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - app_configuration
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
<tr><td><b>Id</b></td><td><code>azure.app_configuration.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Properties of a private endpoint connection. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specified private endpoint connection associated with the configuration store. |
| `PrivateEndpointConnections_ListByConfigurationStore` | `SELECT` | `configStoreName, resourceGroupName, subscriptionId` | Lists all private endpoint connections for a configuration store. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Update the state of the specified private endpoint connection associated with the configuration store. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection. |
