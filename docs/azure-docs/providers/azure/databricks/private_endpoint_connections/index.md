---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - databricks
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
<tr><td><b>Id</b></td><td><code>azure.databricks.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The properties of a private endpoint connection |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Get a private endpoint connection properties for a workspace |
| `PrivateEndpointConnections_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List private endpoint connections of the workspace |
| `PrivateEndpointConnections_Create` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Update the status of a private endpoint connection with the specified name |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Remove private endpoint connection with the specified name |