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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegisteredServers_Get` | `SELECT` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Get a given registered server. |
| `RegisteredServers_ListByStorageSyncService` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a given registered server list. |
| `RegisteredServers_Create` | `INSERT` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Add a new registered server. |
| `RegisteredServers_Delete` | `DELETE` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Delete the given registered server. |
| `RegisteredServers_triggerRollover` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Triggers Server certificate rollover. |
