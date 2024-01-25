---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - relay
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
<tr><td><b>Id</b></td><td><code>azure.relay.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the private endpoint connection resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets a description for the specified Private Endpoint Connection name. |
| `list` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets the available PrivateEndpointConnections within a namespace. |
| `create_or_update` | `INSERT` | `namespaceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Creates or updates PrivateEndpointConnections of service namespace. |
| `delete` | `DELETE` | `namespaceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| `_list` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets the available PrivateEndpointConnections within a namespace. |
