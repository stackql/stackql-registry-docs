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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint. |
| `list_by_sync_group` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint list. |
| `create` | `INSERT` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new ServerEndpoint. |
| `delete` | `DELETE` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given ServerEndpoint. |
| `_list_by_sync_group` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint list. |
| `recall_action` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Recall a server endpoint. |
| `update` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Patch a given ServerEndpoint. |
