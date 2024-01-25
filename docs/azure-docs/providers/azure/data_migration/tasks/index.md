---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - data_migration
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
<tr><td><b>Id</b></td><td><code>azure.data_migration.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| `properties` | `object` | Base class for all types of DMS (classic) task properties. If task is not supported by current client, this object is returned. |
| `systemData` | `object` |  |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The GET method retrieves information about a task. |
| `list` | `SELECT` | `api-version, groupName, projectName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task. |
| `create_or_update` | `INSERT` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one. |
| `delete` | `DELETE` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The DELETE method deletes a task, canceling it first if it's running. |
| `_list` | `EXEC` | `api-version, groupName, projectName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task. |
| `cancel` | `EXEC` | `api-version, groupName, projectName, serviceName, subscriptionId, taskName` | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method cancels a task if it's currently queued or running. |
| `command` | `EXEC` | `api-version, groupName, projectName, serviceName, subscriptionId, taskName, data__commandType` | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method executes a command on a running task. |
| `update` | `EXEC` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so. |
