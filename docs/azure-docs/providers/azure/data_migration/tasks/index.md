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
| `properties` | `object` | Base class for all types of DMS task properties. If task is not supported by current client, this object is returned. |
| `systemData` | `object` |  |
| `type` | `string` | Resource type. |
| `etag` | `string` | HTTP strong entity tag value. This is ignored if submitted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tasks_Get` | `SELECT` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The GET method retrieves information about a task. |
| `Tasks_List` | `SELECT` | `api-version, groupName, projectName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Database Migration Service. This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task. |
| `Tasks_CreateOrUpdate` | `INSERT` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one. |
| `Tasks_Delete` | `DELETE` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The DELETE method deletes a task, canceling it first if it's running. |
| `Tasks_Cancel` | `EXEC` | `api-version, groupName, projectName, serviceName, subscriptionId, taskName` | The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. This method cancels a task if it's currently queued or running. |
| `Tasks_Command` | `EXEC` | `api-version, groupName, projectName, serviceName, subscriptionId, taskName, data__commandType` | The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. This method executes a command on a running task. |
| `Tasks_Update` | `EXEC` |  | The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so. |
