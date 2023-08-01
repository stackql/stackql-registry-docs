---
title: sql_migration_services
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_migration_services
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
<tr><td><b>Name</b></td><td><code>sql_migration_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.sql_migration_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `location` | `string` |  |
| `properties` | `object` | The SQL Migration Service properties. |
| `systemData` | `object` |  |
| `tags` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlMigrationServices_Get` | `SELECT` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Retrieve the Database Migration Service |
| `SqlMigrationServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve all SQL migration services in the resource group. |
| `SqlMigrationServices_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve all SQL migration services in the subscriptions. |
| `SqlMigrationServices_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Create or Update Database Migration Service. |
| `SqlMigrationServices_Delete` | `DELETE` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Delete Database Migration Service. |
| `SqlMigrationServices_Update` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Update Database Migration Service. |
| `SqlMigrationServices_deleteNode` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Delete the integration runtime node. |
| `SqlMigrationServices_listAuthKeys` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Retrieve the List of Authentication Keys for Self Hosted Integration Runtime. |
| `SqlMigrationServices_listMigrations` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Retrieve the List of database migrations attached to the service. |
| `SqlMigrationServices_listMonitoringData` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service. |
| `SqlMigrationServices_regenerateAuthKeys` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Regenerate a new set of Authentication Keys for Self Hosted Integration Runtime. |
