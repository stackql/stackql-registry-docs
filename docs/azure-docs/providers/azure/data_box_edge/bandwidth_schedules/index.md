---
title: bandwidth_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - bandwidth_schedules
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
<tr><td><b>Name</b></td><td><code>bandwidth_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.bandwidth_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | The properties of the bandwidth schedule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` | Gets the properties of the specified bandwidth schedule. |
| `list_by_data_box_edge_device` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Gets all the bandwidth schedules for a Data Box Edge/Data Box Gateway device. |
| `create_or_update` | `INSERT` | `deviceName, name, resourceGroupName, subscriptionId, data__properties` | Creates or updates a bandwidth schedule. |
| `delete` | `DELETE` | `deviceName, name, resourceGroupName, subscriptionId` | Deletes the specified bandwidth schedule. |
| `_list_by_data_box_edge_device` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Gets all the bandwidth schedules for a Data Box Edge/Data Box Gateway device. |
