---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - container_registry
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
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties of a task. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `identity` | `object` | Managed identity for the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tasks_Get` | `SELECT` | `registryName, resourceGroupName, subscriptionId, taskName` | Get the properties of a specified task. |
| `Tasks_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the tasks for a specified container registry. |
| `Tasks_Create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, taskName` | Creates a task for a container registry with the specified parameters. |
| `Tasks_Delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, taskName` | Deletes a specified task. |
| `Tasks_GetDetails` | `EXEC` | `registryName, resourceGroupName, subscriptionId, taskName` | Returns a task with extended information that includes all secrets. |
| `Tasks_Update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, taskName` | Updates a task with the specified parameters. |
