---
title: long_term_retention_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_backups
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
<tr><td><b>Name</b></td><td><code>long_term_retention_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.long_term_retention_backups</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LongTermRetentionBackups_Get` | `SELECT` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Gets a long term retention backup. |
| `LongTermRetentionBackups_ListByDatabase` | `SELECT` | `locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Lists all long term retention backups for a database. |
| `LongTermRetentionBackups_ListByLocation` | `SELECT` | `locationName, subscriptionId` | Lists the long term retention backups for a given location. |
| `LongTermRetentionBackups_ListByResourceGroupDatabase` | `SELECT` | `locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Lists all long term retention backups for a database. |
| `LongTermRetentionBackups_ListByResourceGroupLocation` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given location. |
| `LongTermRetentionBackups_ListByResourceGroupServer` | `SELECT` | `locationName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given server. |
| `LongTermRetentionBackups_ListByServer` | `SELECT` | `locationName, longTermRetentionServerName, subscriptionId` | Lists the long term retention backups for a given server. |
| `LongTermRetentionBackups_Delete` | `DELETE` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Deletes a long term retention backup. |
| `LongTermRetentionBackups_DeleteByResourceGroup` | `DELETE` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Deletes a long term retention backup. |
| `LongTermRetentionBackups_Copy` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Copy an existing long term retention backup. |
| `LongTermRetentionBackups_CopyByResourceGroup` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Copy an existing long term retention backup to a different server. |
| `LongTermRetentionBackups_GetByResourceGroup` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Gets a long term retention backup. |
| `LongTermRetentionBackups_Update` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Updates an existing long term retention backup. |
| `LongTermRetentionBackups_UpdateByResourceGroup` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Updates an existing long term retention backup. |
