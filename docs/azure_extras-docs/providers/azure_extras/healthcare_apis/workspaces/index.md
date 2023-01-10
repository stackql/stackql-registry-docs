---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - healthcare_apis
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
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Workspaces resource specific properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified workspace. |
| `Workspaces_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Lists all the available workspaces under the specified resource group. |
| `Workspaces_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Lists all the available workspaces under the specified subscription. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace resource with the specified parameters. |
| `Workspaces_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Deletes a specified workspace. |
| `Workspaces_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Patch workspace details. |
