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
| `get` | `SELECT` | `configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specified private endpoint connection associated with the configuration store. |
| `list_by_configuration_store` | `SELECT` | `configStoreName, resourceGroupName, subscriptionId` | Lists all private endpoint connections for a configuration store. |
| `create_or_update` | `INSERT` | `configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Update the state of the specified private endpoint connection associated with the configuration store. This operation cannot be used to create a private endpoint connection. Private endpoint connections must be created with the Network resource provider. |
| `delete` | `DELETE` | `configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection. |
| `_list_by_configuration_store` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Lists all private endpoint connections for a configuration store. |
