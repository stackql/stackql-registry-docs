---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - maria_db
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
<tr><td><b>Id</b></td><td><code>azure.maria_db.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, serverName, subscriptionId` | Gets a private endpoint connection. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets all private endpoint connections on a server. |
| `create_or_update` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, serverName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, serverName, subscriptionId` | Deletes a private endpoint connection with a given name. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets all private endpoint connections on a server. |
