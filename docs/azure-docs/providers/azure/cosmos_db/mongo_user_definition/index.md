---
title: mongo_user_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_user_definition
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
<tr><td><b>Name</b></td><td><code>mongo_user_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.mongo_user_definition</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the database account. |
| `name` | `string` | The name of the database account. |
| `properties` | `object` | Azure Cosmos DB Mongo User Definition resource object. |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB Mongo User Definition with the given Id. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves the list of all Azure Cosmos DB Mongo User Definition. |
| `delete` | `DELETE` | `accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Mongo User Definition. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the list of all Azure Cosmos DB Mongo User Definition. |
| `create_update` | `EXEC` | `accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId` | Creates or updates an Azure Cosmos DB Mongo User Definition. |
