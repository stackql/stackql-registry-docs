---
title: database_migrations_sql_mi
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_mi
  - data_migration
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
<tr><td><b>Name</b></td><td><code>database_migrations_sql_mi</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.database_migrations_sql_mi</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `properties` | `object` | Database Migration Resource properties for SQL Managed Instance. |
| `systemData` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseMigrationsSqlMi_Get` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId, targetDbName` | Retrieve the specified database migration for a given SQL Managed Instance. |
| `DatabaseMigrationsSqlMi_CreateOrUpdate` | `INSERT` | `managedInstanceName, resourceGroupName, subscriptionId, targetDbName` | Create a new database migration to a given SQL Managed Instance. |
| `DatabaseMigrationsSqlMi_cancel` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId, targetDbName` | Stop in-progress database migration to SQL Managed Instance. |
| `DatabaseMigrationsSqlMi_cutover` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId, targetDbName` | Initiate cutover for in-progress online database migration to SQL Managed Instance. |
