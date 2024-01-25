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
| `migrate_sql_container_to_autoscale` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL container from manual throughput to autoscale |
| `migrate_sql_container_to_manual_throughput` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL container from autoscale to manual throughput |
| `migrate_sql_database_to_autoscale` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL database from manual throughput to autoscale |
| `migrate_sql_database_to_manual_throughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Migrate an Azure Cosmos DB SQL database from autoscale to manual throughput |
| `retrieve_continuous_backup_information` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId` | Retrieves continuous backup information for a container resource. |
| `sql_container_redistribute_throughput` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB SQL container |
| `sql_container_retrieve_throughput_distribution` | `EXEC` | `accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB SQL container |
| `sql_database_partition_merge` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId` | Merges the partitions of a SQL database |
| `sql_database_redistribute_throughput` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Redistribute throughput for an Azure Cosmos DB SQL database |
| `sql_database_retrieve_throughput_distribution` | `EXEC` | `accountName, databaseName, resourceGroupName, subscriptionId, data__properties` | Retrieve throughput distribution for an Azure Cosmos DB SQL database |
