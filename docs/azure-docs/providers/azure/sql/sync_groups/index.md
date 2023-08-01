---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
  - sql
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
<tr><td><b>Id</b></td><td><code>azure.sql.sync_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a sync group. |
| `sku` | `object` | An ARM Resource SKU. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SyncGroups_Get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Gets a sync group. |
| `SyncGroups_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists sync groups under a hub database. |
| `SyncGroups_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Creates or updates a sync group. |
| `SyncGroups_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Deletes a sync group. |
| `SyncGroups_CancelSync` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Cancels a sync group synchronization. |
| `SyncGroups_ListHubSchemas` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Gets a collection of hub database schemas. |
| `SyncGroups_ListLogs` | `EXEC` | `databaseName, endTime, resourceGroupName, serverName, startTime, subscriptionId, syncGroupName, type` | Gets a collection of sync group logs. |
| `SyncGroups_ListSyncDatabaseIds` | `EXEC` | `locationName, subscriptionId` | Gets a collection of sync database ids. |
| `SyncGroups_RefreshHubSchema` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Refreshes a hub database schema. |
| `SyncGroups_TriggerSync` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Triggers a sync group synchronization. |
| `SyncGroups_Update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Updates a sync group. |
