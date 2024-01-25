---
title: storage_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_tasks
  - storageactions
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
<tr><td><b>Name</b></td><td><code>storage_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storageactions.storage_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the storage task. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, storageTaskName, subscriptionId` | Get the storage task properties |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the storage tasks available under the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the storage tasks available under the subscription. |
| `create` | `INSERT` | `resourceGroupName, storageTaskName, subscriptionId` | Asynchronously creates a new storage task resource with the specified parameters. If a storage task is already created and a subsequent create request is issued with different properties, the storage task properties will be updated. If a storage task is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed. |
| `delete` | `DELETE` | `resourceGroupName, storageTaskName, subscriptionId` | Delete the storage task resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the storage tasks available under the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the storage tasks available under the subscription. |
| `preview_actions` | `EXEC` | `location, subscriptionId, data__properties` | Runs the input conditions against input object metadata properties and designates matched objects in response. |
| `update` | `EXEC` | `resourceGroupName, storageTaskName, subscriptionId` | Update storage task properties |
