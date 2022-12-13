---
title: cassandra_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_resources
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
<tr><td><b>Name</b></td><td><code>cassandra_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.cassandra_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CassandraResources_CreateUpdateCassandraKeyspace` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB Cassandra keyspace |
| `CassandraResources_CreateUpdateCassandraTable` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName, data__properties` | Create or update an Azure Cosmos DB Cassandra Table |
| `CassandraResources_CreateUpdateCassandraView` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName, data__properties` | Create or update an Azure Cosmos DB Cassandra View |
| `CassandraResources_DeleteCassandraKeyspace` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Cassandra keyspace. |
| `CassandraResources_DeleteCassandraTable` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Deletes an existing Azure Cosmos DB Cassandra table. |
| `CassandraResources_DeleteCassandraView` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName` | Deletes an existing Azure Cosmos DB Cassandra view. |
| `CassandraResources_GetCassandraKeyspace` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Gets the Cassandra keyspaces under an existing Azure Cosmos DB database account with the provided name. |
| `CassandraResources_GetCassandraKeyspaceThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Gets the RUs per second of the Cassandra Keyspace under an existing Azure Cosmos DB database account with the provided name. |
| `CassandraResources_GetCassandraTable` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Gets the Cassandra table under an existing Azure Cosmos DB database account. |
| `CassandraResources_GetCassandraTableThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Gets the RUs per second of the Cassandra table under an existing Azure Cosmos DB database account with the provided name. |
| `CassandraResources_GetCassandraView` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName` | Gets the Cassandra view under an existing Azure Cosmos DB database account. |
| `CassandraResources_GetCassandraViewThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName` | Gets the RUs per second of the Cassandra view under an existing Azure Cosmos DB database account with the provided name. |
| `CassandraResources_ListCassandraKeyspaces` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the Cassandra keyspaces under an existing Azure Cosmos DB database account. |
| `CassandraResources_ListCassandraTables` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Lists the Cassandra table under an existing Azure Cosmos DB database account. |
| `CassandraResources_ListCassandraViews` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Lists the Cassandra materialized views under an existing Azure Cosmos DB database account. |
| `CassandraResources_MigrateCassandraKeyspaceToAutoscale` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB Cassandra Keyspace from manual throughput to autoscale |
| `CassandraResources_MigrateCassandraKeyspaceToManualThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB Cassandra Keyspace from autoscale to manual throughput |
| `CassandraResources_MigrateCassandraTableToAutoscale` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Migrate an Azure Cosmos DB Cassandra table from manual throughput to autoscale |
| `CassandraResources_MigrateCassandraTableToManualThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Migrate an Azure Cosmos DB Cassandra table from autoscale to manual throughput |
| `CassandraResources_MigrateCassandraViewToAutoscale` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName` | Migrate an Azure Cosmos DB Cassandra view from manual throughput to autoscale |
| `CassandraResources_MigrateCassandraViewToManualThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName` | Migrate an Azure Cosmos DB Cassandra view from autoscale to manual throughput |
| `CassandraResources_UpdateCassandraKeyspaceThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, data__properties` | Update RUs per second of an Azure Cosmos DB Cassandra Keyspace |
| `CassandraResources_UpdateCassandraTableThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName, data__properties` | Update RUs per second of an Azure Cosmos DB Cassandra table |
| `CassandraResources_UpdateCassandraViewThroughput` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, viewName, data__properties` | Update RUs per second of an Azure Cosmos DB Cassandra view |
