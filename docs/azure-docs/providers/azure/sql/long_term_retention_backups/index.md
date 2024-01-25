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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Gets a long term retention backup. |
| `list_by_database` | `SELECT` | `locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Lists all long term retention backups for a database. |
| `list_by_location` | `SELECT` | `locationName, subscriptionId` | Lists the long term retention backups for a given location. |
| `list_by_resource_group_database` | `SELECT` | `locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Lists all long term retention backups for a database based on a particular resource group. |
| `list_by_resource_group_location` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given location based on resource group. |
| `list_by_resource_group_server` | `SELECT` | `locationName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given server based on resource groups. |
| `list_by_server` | `SELECT` | `locationName, longTermRetentionServerName, subscriptionId` | Lists the long term retention backups for a given server. |
| `delete` | `DELETE` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Deletes a long term retention backup. |
| `delete_by_resource_group` | `DELETE` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Deletes a long term retention backup. |
| `_list_by_database` | `EXEC` | `locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Lists all long term retention backups for a database. |
| `_list_by_location` | `EXEC` | `locationName, subscriptionId` | Lists the long term retention backups for a given location. |
| `_list_by_resource_group_database` | `EXEC` | `locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Lists all long term retention backups for a database based on a particular resource group. |
| `_list_by_resource_group_location` | `EXEC` | `locationName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given location based on resource group. |
| `_list_by_resource_group_server` | `EXEC` | `locationName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given server based on resource groups. |
| `_list_by_server` | `EXEC` | `locationName, longTermRetentionServerName, subscriptionId` | Lists the long term retention backups for a given server. |
| `change_access_tier` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId, data__backupStorageAccessTier, data__operationMode` | Change a long term retention backup access tier. |
| `change_access_tier_by_resource_group` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId, data__backupStorageAccessTier, data__operationMode` | Change a long term retention backup access tier. |
| `copy` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Copy an existing long term retention backup. |
| `copy_by_resource_group` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Copy an existing long term retention backup to a different server. |
| `get_by_resource_group` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Gets a long term retention backup. |
| `update` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId` | Updates an existing long term retention backup. |
| `update_by_resource_group` | `EXEC` | `backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId` | Updates an existing long term retention backup. |
