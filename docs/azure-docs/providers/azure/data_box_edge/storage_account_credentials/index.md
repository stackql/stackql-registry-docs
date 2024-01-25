---
title: storage_account_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_account_credentials
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
<tr><td><b>Name</b></td><td><code>storage_account_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.storage_account_credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | The storage account credential properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` | Gets the properties of the specified storage account credential. |
| `list_by_data_box_edge_device` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `deviceName, name, resourceGroupName, subscriptionId, data__properties` | Creates or updates the storage account credential. |
| `delete` | `DELETE` | `deviceName, name, resourceGroupName, subscriptionId` | Deletes the storage account credential. |
| `_list_by_data_box_edge_device` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
