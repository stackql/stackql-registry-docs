---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - quantum
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
<tr><td><b>Id</b></td><td><code>azure_extras.quantum.workspaces</code></td></tr>
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
| `Workspaces_Get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns the Workspace resource associated with the given name. |
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of Workspaces within a resource group. |
| `Workspaces_ListBySubscription` | `SELECT` | `subscriptionId` | Gets the list of Workspaces within a Subscription. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace resource. |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a Workspace resource. |
| `Workspaces_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates an existing workspace's tags. |
