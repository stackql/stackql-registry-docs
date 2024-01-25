---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
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
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `kind` | `string` | It specify the order api version. |
| `properties` | `object` | Order properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_data_box_edge_device` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `deviceName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` |
| `_list_by_data_box_edge_device` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |
| `exec_get` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |
