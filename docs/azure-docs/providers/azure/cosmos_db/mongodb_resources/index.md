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
| `migrate_mongodb_collection_to_autoscale` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB collection from manual throughput to autoscale |
| `migrate_mongodb_collection_to_manual_throughput` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB collection from autoscale to manual throughput |
| `migrate_mongodb_database_to_autoscale` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB database from manual throughput to autoscale |
| `migrate_mongodb_database_to_manual_throughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB MongoDB database from autoscale to manual throughput |
| `mongodb_container_redistribute_throughput` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB MongoDB container |
| `mongodb_container_retrieve_throughput_distribution` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB MongoDB container |
| `mongodb_database_partition_merge` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Merges the partitions of a MongoDB database |
| `mongodb_database_redistribute_throughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB MongoDB database |
| `mongodb_database_retrieve_throughput_distribution` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB MongoDB database |
| `retrieve_continuous_backup_information` | `EXEC` | `accountName, collectionName, databaseName, resourceGroupName, subscriptionId` | Retrieves continuous backup information for a Mongodb collection. |
