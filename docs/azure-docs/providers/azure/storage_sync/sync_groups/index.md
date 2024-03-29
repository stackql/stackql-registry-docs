---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
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
<tr><td><b>Name</b></td><td><code>sync_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.sync_groups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a given SyncGroup. |
| `list_by_storage_sync_service` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a SyncGroup List. |
| `create` | `INSERT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new SyncGroup. |
| `delete` | `DELETE` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given SyncGroup. |
| `_list_by_storage_sync_service` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a SyncGroup List. |
