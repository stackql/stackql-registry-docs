---
title: registered_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_servers
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
<tr><td><b>Name</b></td><td><code>registered_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.registered_servers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Get a given registered server. |
| `list_by_storage_sync_service` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a given registered server list. |
| `create` | `INSERT` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Add a new registered server. |
| `delete` | `DELETE` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Delete the given registered server. |
| `_list_by_storage_sync_service` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a given registered server list. |
| `trigger_rollover` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Triggers Server certificate rollover. |
| `update` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Update registered server. |
