---
title: server_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - server_endpoints
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>server_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.server_endpoints</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerEndpoints_Get` | `SELECT` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint. |
| `ServerEndpoints_ListBySyncGroup` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint list. |
| `ServerEndpoints_Create` | `INSERT` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new ServerEndpoint. |
| `ServerEndpoints_Delete` | `DELETE` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given ServerEndpoint. |
| `ServerEndpoints_Update` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Patch a given ServerEndpoint. |
| `ServerEndpoints_recallAction` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Recall a server endpoint. |
