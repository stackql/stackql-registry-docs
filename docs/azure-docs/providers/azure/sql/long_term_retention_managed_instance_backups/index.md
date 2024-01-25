---
title: long_term_retention_managed_instance_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_managed_instance_backups
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
<tr><td><b>Name</b></td><td><code>long_term_retention_managed_instance_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.long_term_retention_managed_instance_backups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupName, databaseName, locationName, managedInstanceName, subscriptionId` | Gets a long term retention backup for a managed database. |
| `list_by_database` | `SELECT` | `databaseName, locationName, managedInstanceName, subscriptionId` | Lists all long term retention backups for a managed database. |
| `list_by_instance` | `SELECT` | `locationName, managedInstanceName, subscriptionId` | Lists the long term retention backups for a given managed instance. |
| `list_by_location` | `SELECT` | `locationName, subscriptionId` | Lists the long term retention backups for managed databases in a given location. |
| `list_by_resource_group_database` | `SELECT` | `databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Lists all long term retention backups for a managed database. |
| `list_by_resource_group_instance` | `SELECT` | `locationName, managedInstanceName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given managed instance. |
| `list_by_resource_group_location` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists the long term retention backups for managed databases in a given location. |
| `delete` | `DELETE` | `backupName, databaseName, locationName, managedInstanceName, subscriptionId` | Deletes a long term retention backup. |
| `delete_by_resource_group` | `DELETE` | `backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a long term retention backup. |
| `_list_by_database` | `EXEC` | `databaseName, locationName, managedInstanceName, subscriptionId` | Lists all long term retention backups for a managed database. |
| `_list_by_instance` | `EXEC` | `locationName, managedInstanceName, subscriptionId` | Lists the long term retention backups for a given managed instance. |
| `_list_by_location` | `EXEC` | `locationName, subscriptionId` | Lists the long term retention backups for managed databases in a given location. |
| `_list_by_resource_group_database` | `EXEC` | `databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Lists all long term retention backups for a managed database. |
| `_list_by_resource_group_instance` | `EXEC` | `locationName, managedInstanceName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given managed instance. |
| `_list_by_resource_group_location` | `EXEC` | `locationName, resourceGroupName, subscriptionId` | Lists the long term retention backups for managed databases in a given location. |
| `get_by_resource_group` | `EXEC` | `backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a long term retention backup for a managed database. |
