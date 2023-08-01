---
title: workspace_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_private_endpoint_connections
  - healthcare_apis
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
<tr><td><b>Name</b></td><td><code>workspace_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.workspace_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspacePrivateEndpointConnections_Get` | `SELECT` | `api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Gets the specified private endpoint connection associated with the workspace. |
| `WorkspacePrivateEndpointConnections_ListByWorkspace` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Lists all private endpoint connections for a workspace. |
| `WorkspacePrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Update the state of the specified private endpoint connection associated with the workspace. |
| `WorkspacePrivateEndpointConnections_Delete` | `DELETE` | `api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Deletes a private endpoint connection. |
