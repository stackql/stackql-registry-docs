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
| `Databases_Get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database. |
| `Databases_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of databases in an elastic pool. |
| `Databases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of databases. |
| `Databases_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, data__location` | Creates a new database or updates an existing database. |
| `Databases_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId` | Deletes the database. |
| `Databases_Export` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Exports a database. |
| `Databases_Failover` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Failovers a database. |
| `Databases_Import` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Imports a bacpac into a new database. |
| `Databases_ListInaccessibleByServer` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of inaccessible databases in a logical server |
| `Databases_ListMetricDefinitions` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Returns database metric definitions. |
| `Databases_ListMetrics` | `EXEC` | `$filter, databaseName, resourceGroupName, serverName, subscriptionId` | Returns database metrics. |
| `Databases_Pause` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Pauses a database. |
| `Databases_Rename` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__id` | Renames a database. |
| `Databases_Resume` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Resumes a database. |
| `Databases_Update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Updates an existing database. |
| `Databases_UpgradeDataWarehouse` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Upgrades a data warehouse. |
