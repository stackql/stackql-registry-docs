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
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The managed database's properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabases_Get` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed database. |
| `ManagedDatabases_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed databases. |
| `ManagedDatabases_CreateOrUpdate` | `INSERT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__location` | Creates a new database or updates an existing database. |
| `ManagedDatabases_Delete` | `DELETE` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed database. |
| `ManagedDatabases_CancelMove` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId` | Cancels a managed database move operation. |
| `ManagedDatabases_CompleteMove` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId` | Completes a managed database move operation. |
| `ManagedDatabases_CompleteRestore` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__lastBackupName` | Completes the restore operation on a managed database. |
| `ManagedDatabases_ListInaccessibleByInstance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of inaccessible managed databases in a managed instance |
| `ManagedDatabases_StartMove` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId` | Starts a managed database move operation. |
| `ManagedDatabases_Update` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Updates an existing database. |
