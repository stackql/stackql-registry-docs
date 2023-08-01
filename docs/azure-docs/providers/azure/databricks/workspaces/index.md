---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - databricks
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.databricks.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The workspace properties. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_Get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the workspace. |
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the workspaces within a resource group. |
| `Workspaces_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the workspaces within a subscription. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName, data__properties` | Creates a new workspace. |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes the workspace. |
| `Workspaces_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a workspace. |
