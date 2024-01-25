---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - quantum
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
<tr><td><b>Id</b></td><td><code>azure.quantum.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed Identity information. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a Workspace |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns the Workspace resource associated with the given name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of Workspaces within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets the list of Workspaces within a Subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace resource. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a Workspace resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the list of Workspaces within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets the list of Workspaces within a Subscription. |
