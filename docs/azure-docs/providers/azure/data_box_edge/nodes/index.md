---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
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
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | This class represents the nodes in a highly available cluster |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_data_box_edge_device` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` |
| `_list_by_data_box_edge_device` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |
