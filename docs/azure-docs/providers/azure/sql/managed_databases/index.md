---
title: managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases
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
<tr><td><b>Name</b></td><td><code>managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | The managed database's properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed database. |
| `list_by_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed databases. |
| `create_or_update` | `INSERT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__location` | Creates a new database or updates an existing database. |
| `delete` | `DELETE` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed database. |
| `_list_by_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed databases. |
| `cancel_move` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId` | Cancels a managed database move operation. |
| `complete_move` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId` | Completes a managed database move operation. |
| `complete_restore` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__lastBackupName` | Completes the restore operation on a managed database. |
| `start_move` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId` | Starts a managed database move operation. |
| `update` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Updates an existing database. |
