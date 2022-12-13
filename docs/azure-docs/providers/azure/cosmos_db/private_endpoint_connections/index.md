---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - cosmos_db
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
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets a private endpoint connection. |
| `PrivateEndpointConnections_ListByDatabaseAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all private endpoint connections on a Cosmos DB account. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection with a given name. |
