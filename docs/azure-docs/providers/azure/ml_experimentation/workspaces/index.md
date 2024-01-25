---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - ml_experimentation
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
<tr><td><b>Id</b></td><td><code>azure.ml_experimentation.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `properties` | `object` | The properties of a machine learning team account workspace. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified machine learning workspace. |
| `list_by_accounts` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all the available machine learning workspaces under the specified team account. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a machine learning workspace with the specified parameters. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Deletes a machine learning workspace. |
| `_list_by_accounts` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists all the available machine learning workspaces under the specified team account. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Updates a machine learning workspace with the specified parameters. |
