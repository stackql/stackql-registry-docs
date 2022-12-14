---
title: table_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - table_resources
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>table_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.table_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TableResources_CreateUpdateTable` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName, data__properties` | Create or update an Azure Cosmos DB Table |
| `TableResources_DeleteTable` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName` | Deletes an existing Azure Cosmos DB Table. |
| `TableResources_GetTable` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName` | Gets the Tables under an existing Azure Cosmos DB database account with the provided name. |
| `TableResources_GetTableThroughput` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName` | Gets the RUs per second of the Table under an existing Azure Cosmos DB database account with the provided name. |
| `TableResources_ListTables` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the Tables under an existing Azure Cosmos DB database account. |
| `TableResources_MigrateTableToAutoscale` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName` | Migrate an Azure Cosmos DB Table from manual throughput to autoscale |
| `TableResources_MigrateTableToManualThroughput` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName` | Migrate an Azure Cosmos DB Table from autoscale to manual throughput |
| `TableResources_RetrieveContinuousBackupInformation` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName` | Retrieves continuous backup information for a table. |
| `TableResources_UpdateTableThroughput` | `EXEC` | `accountName, resourceGroupName, subscriptionId, tableName, data__properties` | Update RUs per second of an Azure Cosmos DB Table |
