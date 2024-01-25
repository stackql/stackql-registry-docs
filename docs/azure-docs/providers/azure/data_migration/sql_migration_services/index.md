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
| `get` | `SELECT` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Retrieve the Database Migration Service |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve all SQL migration services in the resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieve all SQL migration services in the subscriptions. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Create or Update Database Migration Service. |
| `delete` | `DELETE` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Delete Database Migration Service. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve all SQL migration services in the resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieve all SQL migration services in the subscriptions. |
| `regenerate_auth_keys` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Regenerate a new set of Authentication Keys for Self Hosted Integration Runtime. |
| `update` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` | Update Database Migration Service. |
