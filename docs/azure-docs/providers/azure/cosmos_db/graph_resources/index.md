---
title: graph_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_resources
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
<tr><td><b>Name</b></td><td><code>graph_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.graph_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GraphResources_CreateUpdateGraph` | `EXEC` | `accountName, graphName, resourceGroupName, subscriptionId, data__properties` | Create or update an Azure Cosmos DB Graph. |
| `GraphResources_DeleteGraphResource` | `EXEC` | `accountName, graphName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB Graph Resource. |
| `GraphResources_GetGraph` | `EXEC` | `accountName, graphName, resourceGroupName, subscriptionId` | Gets the Graph resource under an existing Azure Cosmos DB database account with the provided name. |
| `GraphResources_ListGraphs` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the graphs under an existing Azure Cosmos DB database account. |
