---
title: gremlin_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - gremlin_resources
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
<tr><td><b>Name</b></td><td><code>gremlin_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.gremlin_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GremlinResources_CreateUpdateGremlinDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB Gremlin database |
| `GremlinResources_CreateUpdateGremlinGraph` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB Gremlin graph |
| `GremlinResources_DeleteGremlinDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Gremlin database. |
| `GremlinResources_DeleteGremlinGraph` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Gremlin graph. |
| `GremlinResources_GetGremlinDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Gets the Gremlin databases under an existing Azure Cosmos DB database account with the provided name. |
| `GremlinResources_GetGremlinDatabaseThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name. |
| `GremlinResources_GetGremlinGraph` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId` | Gets the Gremlin graph under an existing Azure Cosmos DB database account. |
| `GremlinResources_GetGremlinGraphThroughput` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId` | Gets the Gremlin graph throughput under an existing Azure Cosmos DB database account with the provided name. |
| `GremlinResources_ListGremlinDatabases` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the Gremlin databases under an existing Azure Cosmos DB database account. |
| `GremlinResources_ListGremlinGraphs` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Lists the Gremlin graph under an existing Azure Cosmos DB database account. |
| `GremlinResources_MigrateGremlinDatabaseToAutoscale` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB Gremlin database from manual throughput to autoscale |
| `GremlinResources_MigrateGremlinDatabaseToManualThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB Gremlin database from autoscale to manual throughput |
| `GremlinResources_MigrateGremlinGraphToAutoscale` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB Gremlin graph from manual throughput to autoscale |
| `GremlinResources_MigrateGremlinGraphToManualThroughput` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB Gremlin graph from autoscale to manual throughput |
| `GremlinResources_RetrieveContinuousBackupInformation` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId` | Retrieves continuous backup information for a gremlin graph. |
| `GremlinResources_UpdateGremlinDatabaseThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Update RUs per second of an Azure Cosmos DB Gremlin database |
| `GremlinResources_UpdateGremlinGraphThroughput` | `EXEC` | `accountName, databaseName, graphName, resourceGroupName, subscriptionId, data__properties` | Update RUs per second of an Azure Cosmos DB Gremlin graph |
