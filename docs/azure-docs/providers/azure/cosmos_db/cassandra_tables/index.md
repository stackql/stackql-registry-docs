---
title: cassandra_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_tables
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
<tr><td><b>Name</b></td><td><code>cassandra_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.cassandra_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The location of the resource group to which the resource belongs. |
| `properties` | `object` | The properties of an Azure Cosmos DB Cassandra table |
| `tags` | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Gets the Cassandra table under an existing Azure Cosmos DB database account. |
| `list` | `SELECT` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Lists the Cassandra table under an existing Azure Cosmos DB database account. |
| `delete` | `DELETE` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName` | Deletes an existing Azure Cosmos DB Cassandra table. |
| `_list` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId` | Lists the Cassandra table under an existing Azure Cosmos DB database account. |
| `create_update` | `EXEC` | `accountName, keyspaceName, resourceGroupName, subscriptionId, tableName, data__properties` | Create or update an Azure Cosmos DB Cassandra Table |
