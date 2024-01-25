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
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Managed identity for the resource. |
| `properties` | `object` | The properties of a task. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `registryName, resourceGroupName, subscriptionId, taskName` | Get the properties of a specified task. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the tasks for a specified container registry. |
| `create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, taskName` | Creates a task for a container registry with the specified parameters. |
| `delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, taskName` | Deletes a specified task. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all the tasks for a specified container registry. |
| `update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, taskName` | Updates a task with the specified parameters. |
