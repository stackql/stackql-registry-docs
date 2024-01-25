---
title: notebook_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_workspaces
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
<tr><td><b>Name</b></td><td><code>notebook_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.notebook_workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the database account. |
| `name` | `string` | The name of the database account. |
| `properties` | `object` | Properties of a notebook workspace resource. |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Gets the notebook workspace for a Cosmos DB account. |
| `list_by_database_account` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the notebook workspace resources of an existing Cosmos DB account. |
| `create_or_update` | `INSERT` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Creates the notebook workspace for a Cosmos DB account. |
| `delete` | `DELETE` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Deletes the notebook workspace for a Cosmos DB account. |
| `_list_by_database_account` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the notebook workspace resources of an existing Cosmos DB account. |
| `regenerate_auth_token` | `EXEC` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Regenerates the auth token for the notebook workspace |
| `start` | `EXEC` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Starts the notebook workspace |
