---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | The container properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId` |  |
| `list_by_storage_account` | `SELECT` | `deviceName, resourceGroupName, storageAccountName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId, data__properties` |  |
| `delete` | `DELETE` | `containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId` | Deletes the container on the Data Box Edge/Data Box Gateway device. |
| `_list_by_storage_account` | `EXEC` | `deviceName, resourceGroupName, storageAccountName, subscriptionId` |  |
| `refresh` | `EXEC` | `containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId` |  |
