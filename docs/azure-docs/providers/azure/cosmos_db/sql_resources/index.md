---
title: sql_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_resources
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
<tr><td><b>Name</b></td><td><code>sql_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.sql_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlResources_CreateUpdateClientEncryptionKey` | `EXEC` | `accountName, clientEncryptionKeyName, databaseName, resourceGroupName, subscriptionId, data__properties` | Create or update a ClientEncryptionKey. This API is meant to be invoked via tools such as the Azure Powershell (instead of directly). |
| `SqlResources_CreateUpdateSqlContainer` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB SQL container |
| `SqlResources_CreateUpdateSqlDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB SQL database |
| `SqlResources_CreateUpdateSqlRoleAssignment` | `EXEC` | `accountName, resourceGroupName, roleAssignmentId, subscriptionId` | Creates or updates an Azure Cosmos DB SQL Role Assignment. |
| `SqlResources_CreateUpdateSqlRoleDefinition` | `EXEC` | `accountName, resourceGroupName, roleDefinitionId, subscriptionId` | Creates or updates an Azure Cosmos DB SQL Role Definition. |
| `SqlResources_CreateUpdateSqlStoredProcedure` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, storedProcedureName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB SQL storedProcedure |
| `SqlResources_CreateUpdateSqlTrigger` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, triggerName, data__properties` | Create or update an Azure Cosmos DB SQL trigger |
| `SqlResources_CreateUpdateSqlUserDefinedFunction` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, userDefinedFunctionName, data__properties` | Create or update an Azure Cosmos DB SQL userDefinedFunction |
| `SqlResources_DeleteSqlContainer` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB SQL container. |
| `SqlResources_DeleteSqlDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB SQL database. |
| `SqlResources_DeleteSqlRoleAssignment` | `EXEC` | `accountName, resourceGroupName, roleAssignmentId, subscriptionId` | Deletes an existing Azure Cosmos DB SQL Role Assignment. |
| `SqlResources_DeleteSqlRoleDefinition` | `EXEC` | `accountName, resourceGroupName, roleDefinitionId, subscriptionId` | Deletes an existing Azure Cosmos DB SQL Role Definition. |
| `SqlResources_DeleteSqlStoredProcedure` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, storedProcedureName, subscriptionId` | Deletes an existing Azure Cosmos DB SQL storedProcedure. |
| `SqlResources_DeleteSqlTrigger` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, triggerName` | Deletes an existing Azure Cosmos DB SQL trigger. |
| `SqlResources_DeleteSqlUserDefinedFunction` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, userDefinedFunctionName` | Deletes an existing Azure Cosmos DB SQL userDefinedFunction. |
| `SqlResources_GetClientEncryptionKey` | `EXEC` | `accountName, clientEncryptionKeyName, databaseName, resourceGroupName, subscriptionId` | Gets the ClientEncryptionKey under an existing Azure Cosmos DB SQL database. |
| `SqlResources_GetSqlContainer` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Gets the SQL container under an existing Azure Cosmos DB database account. |
| `SqlResources_GetSqlContainerThroughput` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Gets the RUs per second of the SQL container under an existing Azure Cosmos DB database account. |
| `SqlResources_GetSqlDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Gets the SQL database under an existing Azure Cosmos DB database account with the provided name. |
| `SqlResources_GetSqlDatabaseThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Gets the RUs per second of the SQL database under an existing Azure Cosmos DB database account with the provided name. |
| `SqlResources_GetSqlRoleAssignment` | `EXEC` | `accountName, resourceGroupName, roleAssignmentId, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB SQL Role Assignment with the given Id. |
| `SqlResources_GetSqlRoleDefinition` | `EXEC` | `accountName, resourceGroupName, roleDefinitionId, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB SQL Role Definition with the given Id. |
| `SqlResources_GetSqlStoredProcedure` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, storedProcedureName, subscriptionId` | Gets the SQL storedProcedure under an existing Azure Cosmos DB database account. |
| `SqlResources_GetSqlTrigger` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, triggerName` | Gets the SQL trigger under an existing Azure Cosmos DB database account. |
| `SqlResources_GetSqlUserDefinedFunction` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, userDefinedFunctionName` | Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account. |
| `SqlResources_ListClientEncryptionKeys` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Lists the ClientEncryptionKeys under an existing Azure Cosmos DB SQL database. |
| `SqlResources_ListSqlContainerPartitionMerge` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Merges the partitions of a SQL Container |
| `SqlResources_ListSqlContainers` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Lists the SQL container under an existing Azure Cosmos DB database account. |
| `SqlResources_ListSqlDatabases` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the SQL databases under an existing Azure Cosmos DB database account. |
| `SqlResources_ListSqlRoleAssignments` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the list of all Azure Cosmos DB SQL Role Assignments. |
| `SqlResources_ListSqlRoleDefinitions` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the list of all Azure Cosmos DB SQL Role Definitions. |
| `SqlResources_ListSqlStoredProcedures` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Lists the SQL storedProcedure under an existing Azure Cosmos DB database account. |
| `SqlResources_ListSqlTriggers` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Lists the SQL trigger under an existing Azure Cosmos DB database account. |
| `SqlResources_ListSqlUserDefinedFunctions` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Lists the SQL userDefinedFunction under an existing Azure Cosmos DB database account. |
| `SqlResources_MigrateSqlContainerToAutoscale` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL container from manual throughput to autoscale |
| `SqlResources_MigrateSqlContainerToManualThroughput` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL container from autoscale to manual throughput |
| `SqlResources_MigrateSqlDatabaseToAutoscale` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL database from manual throughput to autoscale |
| `SqlResources_MigrateSqlDatabaseToManualThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL database from autoscale to manual throughput |
| `SqlResources_RetrieveContinuousBackupInformation` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Retrieves continuous backup information for a container resource. |
| `SqlResources_SqlContainerRedistributeThroughput` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB SQL container |
| `SqlResources_SqlContainerRetrieveThroughputDistribution` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB SQL container |
| `SqlResources_SqlDatabaseRedistributeThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB SQL database |
| `SqlResources_SqlDatabaseRetrieveThroughputDistribution` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB SQL database |
| `SqlResources_UpdateSqlContainerThroughput` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties` | Update RUs per second of an Azure Cosmos DB SQL container |
| `SqlResources_UpdateSqlDatabaseThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Update RUs per second of an Azure Cosmos DB SQL database |
