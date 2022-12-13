---
title: workspace_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_collections
  - powerbi_embedded
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
<tr><td><b>Name</b></td><td><code>workspace_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_embedded.workspace_collections</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceCollections_create` | `INSERT` | `resourceGroupName, subscriptionId, workspaceCollectionName` | Creates a new Power BI Workspace Collection with the specified properties. A Power BI Workspace Collection contains one or more workspaces, and can be used to provision keys that provide API access to those workspaces. |
| `WorkspaceCollections_delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceCollectionName` | Delete a Power BI Workspace Collection. |
| `WorkspaceCollections_checkNameAvailability` | `EXEC` | `location, subscriptionId` | Verify the specified Power BI Workspace Collection name is valid and not already in use. |
| `WorkspaceCollections_getAccessKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceCollectionName` | Retrieves the primary and secondary access keys for the specified Power BI Workspace Collection. |
| `WorkspaceCollections_getByName` | `EXEC` | `resourceGroupName, subscriptionId, workspaceCollectionName` | Retrieves an existing Power BI Workspace Collection. |
| `WorkspaceCollections_listByResourceGroup` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieves all existing Power BI workspace collections in the specified resource group. |
| `WorkspaceCollections_listBySubscription` | `EXEC` | `subscriptionId` | Retrieves all existing Power BI workspace collections in the specified subscription. |
| `WorkspaceCollections_migrate` | `EXEC` | `resourceGroupName, subscriptionId` | Migrates an existing Power BI Workspace Collection to a different resource group and/or subscription. |
| `WorkspaceCollections_regenerateKey` | `EXEC` | `resourceGroupName, subscriptionId, workspaceCollectionName` | Regenerates the primary or secondary access key for the specified Power BI Workspace Collection. |
| `WorkspaceCollections_update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceCollectionName` | Update an existing Power BI Workspace Collection with the specified properties. |
