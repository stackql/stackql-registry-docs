---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `kind` | `string` | Kind of database. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `managedBy` | `string` | Resource that manages the database. |
| `properties` | `object` | The database's properties. |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database. |
| `list_by_elastic_pool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of databases in an elastic pool. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of databases. |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, data__location` | Creates a new database or updates an existing database. |
| `delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId` | Deletes the database. |
| `_list_by_elastic_pool` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of databases in an elastic pool. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of databases. |
| `export` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Exports a database. |
| `failover` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Failovers a database. |
| `import` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Imports a bacpac into a new database. |
| `pause` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Pauses a database. |
| `rename` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__id` | Renames a database. |
| `resume` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Resumes a database. |
| `update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Updates an existing database. |
| `upgrade_data_warehouse` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Upgrades a data warehouse. |
