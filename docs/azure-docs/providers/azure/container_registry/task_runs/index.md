---
title: task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - task_runs
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
<tr><td><b>Name</b></td><td><code>task_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.task_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties of task run. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
| `identity` | `object` | Managed identity for the resource. |
| `location` | `string` | The location of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TaskRuns_Get` | `SELECT` | `registryName, resourceGroupName, subscriptionId, taskRunName` | Gets the detailed information for a given task run. |
| `TaskRuns_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the task runs for a specified container registry. |
| `TaskRuns_Create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, taskRunName` | Creates a task run for a container registry with the specified parameters. |
| `TaskRuns_Delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, taskRunName` | Deletes a specified task run resource. |
| `TaskRuns_GetDetails` | `EXEC` | `registryName, resourceGroupName, subscriptionId, taskRunName` | Gets the detailed information for a given task run that includes all secrets. |
| `TaskRuns_Update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, taskRunName` | Updates a task run with the specified parameters. |
