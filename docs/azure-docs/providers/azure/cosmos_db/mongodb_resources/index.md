---
title: mongodb_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - mongodb_resources
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
<tr><td><b>Name</b></td><td><code>mongodb_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.mongodb_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MongoDBResources_CreateUpdateMongoDBCollection` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB MongoDB Collection |
| `MongoDBResources_CreateUpdateMongoDBDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Create or updates Azure Cosmos DB MongoDB database |
| `MongoDBResources_CreateUpdateMongoRoleDefinition` | `EXEC` | `accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId` | Creates or updates an Azure Cosmos DB Mongo Role Definition. |
| `MongoDBResources_CreateUpdateMongoUserDefinition` | `EXEC` | `accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId` | Creates or updates an Azure Cosmos DB Mongo User Definition. |
| `MongoDBResources_DeleteMongoDBCollection` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB MongoDB Collection. |
| `MongoDBResources_DeleteMongoDBDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB MongoDB database. |
| `MongoDBResources_DeleteMongoRoleDefinition` | `EXEC` | `accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Mongo Role Definition. |
| `MongoDBResources_DeleteMongoUserDefinition` | `EXEC` | `accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Mongo User Definition. |
| `MongoDBResources_GetMongoDBCollection` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Gets the MongoDB collection under an existing Azure Cosmos DB database account. |
| `MongoDBResources_GetMongoDBCollectionThroughput` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Gets the RUs per second of the MongoDB collection under an existing Azure Cosmos DB database account with the provided name. |
| `MongoDBResources_GetMongoDBDatabase` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Gets the MongoDB databases under an existing Azure Cosmos DB database account with the provided name. |
| `MongoDBResources_GetMongoDBDatabaseThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Gets the RUs per second of the MongoDB database under an existing Azure Cosmos DB database account with the provided name. |
| `MongoDBResources_GetMongoRoleDefinition` | `EXEC` | `accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id. |
| `MongoDBResources_GetMongoUserDefinition` | `EXEC` | `accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB Mongo User Definition with the given Id. |
| `MongoDBResources_ListMongoDBCollectionPartitionMerge` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Merges the partitions of a MongoDB Collection |
| `MongoDBResources_ListMongoDBCollections` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Lists the MongoDB collection under an existing Azure Cosmos DB database account. |
| `MongoDBResources_ListMongoDBDatabases` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the MongoDB databases under an existing Azure Cosmos DB database account. |
| `MongoDBResources_ListMongoRoleDefinitions` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the list of all Azure Cosmos DB Mongo Role Definitions. |
| `MongoDBResources_ListMongoUserDefinitions` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the list of all Azure Cosmos DB Mongo User Definition. |
| `MongoDBResources_MigrateMongoDBCollectionToAutoscale` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB collection from manual throughput to autoscale |
| `MongoDBResources_MigrateMongoDBCollectionToManualThroughput` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB collection from autoscale to manual throughput |
| `MongoDBResources_MigrateMongoDBDatabaseToAutoscale` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB database from manual throughput to autoscale |
| `MongoDBResources_MigrateMongoDBDatabaseToManualThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB database from autoscale to manual throughput |
| `MongoDBResources_MongoDBContainerRedistributeThroughput` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB MongoDB container |
| `MongoDBResources_MongoDBContainerRetrieveThroughputDistribution` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB MongoDB container |
| `MongoDBResources_MongoDBDatabaseRedistributeThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB MongoDB database |
| `MongoDBResources_MongoDBDatabaseRetrieveThroughputDistribution` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB MongoDB database |
| `MongoDBResources_RetrieveContinuousBackupInformation` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Retrieves continuous backup information for a Mongodb collection. |
| `MongoDBResources_UpdateMongoDBCollectionThroughput` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties` | Update the RUs per second of an Azure Cosmos DB MongoDB collection |
| `MongoDBResources_UpdateMongoDBDatabaseThroughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Update RUs per second of the an Azure Cosmos DB MongoDB database |
