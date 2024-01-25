---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - defender
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
<tr><td><b>Id</b></td><td><code>azure.defender.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Workspace properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns a workspace with the given name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns a list of workspaces in the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns a list of workspaces under the given subscription. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Delete a Workspace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns a list of workspaces in the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns a list of workspaces under the given subscription. |
| `create_and_update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Create or update a Workspace. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Update a Workspace. |
