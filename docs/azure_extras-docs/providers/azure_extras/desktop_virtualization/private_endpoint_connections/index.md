---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - desktop_virtualization
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.desktop_virtualization.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_ListByHostPool` | `SELECT` | `hostPoolName, resourceGroupName, subscriptionId` | List private endpoint connections associated with hostpool. |
| `PrivateEndpointConnections_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List private endpoint connections. |
| `PrivateEndpointConnections_DeleteByHostPool` | `DELETE` | `hostPoolName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Remove a connection. |
| `PrivateEndpointConnections_DeleteByWorkspace` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Remove a connection. |
| `PrivateEndpointConnections_GetByHostPool` | `EXEC` | `hostPoolName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Get a private endpoint connection. |
| `PrivateEndpointConnections_GetByWorkspace` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Get a private endpoint connection. |
| `PrivateEndpointConnections_UpdateByHostPool` | `EXEC` | `hostPoolName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection. |
| `PrivateEndpointConnections_UpdateByWorkspace` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Approve or reject a private endpoint connection. |
