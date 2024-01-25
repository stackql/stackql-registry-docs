---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - synapse
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
<tr><td><b>Id</b></td><td><code>azure.synapse.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The workspace managed identity |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Workspace properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets a workspace |
| `list` | `SELECT` | `subscriptionId` | Returns a list of workspaces in a subscription |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns a list of workspaces in a resource group |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a workspace |
| `_list` | `EXEC` | `subscriptionId` | Returns a list of workspaces in a subscription |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns a list of workspaces in a resource group |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a workspace |
