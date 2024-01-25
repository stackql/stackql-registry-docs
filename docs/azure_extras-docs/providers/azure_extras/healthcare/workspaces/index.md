---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - healthcare
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Workspaces resource specific properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified workspace. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available workspaces under the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the available workspaces under the specified subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace resource with the specified parameters. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a specified workspace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the available workspaces under the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the available workspaces under the specified subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Patch workspace details. |
