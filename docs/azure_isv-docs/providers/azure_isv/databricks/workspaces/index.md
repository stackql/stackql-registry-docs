---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - databricks
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.databricks.workspaces</code></td></tr>
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
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the workspace. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the workspaces within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all the workspaces within a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName, data__properties` | Creates a new workspace. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes the workspace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the workspaces within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all the workspaces within a subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a workspace. |
