---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - data_box_edge
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | It specify the order api version. |
| `properties` | `object` | Order properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Orders_ListByDataBoxEdgeDevice` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` |
| `Orders_CreateOrUpdate` | `INSERT` | `deviceName, resourceGroupName, subscriptionId` |
| `Orders_Delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` |
| `Orders_Get` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |
| `Orders_ListDCAccessCode` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |
