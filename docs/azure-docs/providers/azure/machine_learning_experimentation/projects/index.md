---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - machine_learning_experimentation
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_experimentation.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `properties` | `object` | The properties of a machine learning project. |
| `tags` | `object` | The tags of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Projects_Get` | `SELECT` | `accountName, projectName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified machine learning project. |
| `Projects_ListByWorkspace` | `SELECT` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Lists all the available machine learning projects under the specified workspace. |
| `Projects_CreateOrUpdate` | `INSERT` | `accountName, projectName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a project with the specified parameters. |
| `Projects_Delete` | `DELETE` | `accountName, projectName, resourceGroupName, subscriptionId, workspaceName` | Deletes a project. |
| `Projects_Update` | `EXEC` | `accountName, projectName, resourceGroupName, subscriptionId, workspaceName` | Updates a project with the specified parameters. |
