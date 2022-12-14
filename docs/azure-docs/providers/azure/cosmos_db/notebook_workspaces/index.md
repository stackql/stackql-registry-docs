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
| `NotebookWorkspaces_Get` | `SELECT` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Gets the notebook workspace for a Cosmos DB account. |
| `NotebookWorkspaces_ListByDatabaseAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the notebook workspace resources of an existing Cosmos DB account. |
| `NotebookWorkspaces_CreateOrUpdate` | `INSERT` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Creates the notebook workspace for a Cosmos DB account. |
| `NotebookWorkspaces_Delete` | `DELETE` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Deletes the notebook workspace for a Cosmos DB account. |
| `NotebookWorkspaces_ListConnectionInfo` | `EXEC` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Retrieves the connection info for the notebook workspace |
| `NotebookWorkspaces_RegenerateAuthToken` | `EXEC` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Regenerates the auth token for the notebook workspace |
| `NotebookWorkspaces_Start` | `EXEC` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` | Starts the notebook workspace |
