---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - container_service
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
<tr><td><b>Id</b></td><td><code>azure.container_service.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the private endpoint connection. |
| `name` | `string` | The name of the private endpoint connection. |
| `properties` | `object` | Properties of a private endpoint connection. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | To learn more about private clusters, see: https://docs.microsoft.com/azure/aks/private-clusters |
| `PrivateEndpointConnections_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | To learn more about private clusters, see: https://docs.microsoft.com/azure/aks/private-clusters |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` |  |
| `PrivateEndpointConnections_Update` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` |  |
