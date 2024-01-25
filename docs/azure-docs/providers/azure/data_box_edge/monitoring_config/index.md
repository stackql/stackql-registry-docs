---
title: monitoring_config
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_config
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
<tr><td><b>Name</b></td><td><code>monitoring_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.monitoring_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | Metrics properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `deviceName, resourceGroupName, roleName, subscriptionId` |
| `create_or_update` | `INSERT` | `deviceName, resourceGroupName, roleName, subscriptionId, data__properties` |
| `delete` | `DELETE` | `deviceName, resourceGroupName, roleName, subscriptionId` |
| `_list` | `EXEC` | `deviceName, resourceGroupName, roleName, subscriptionId` |
| `exec_get` | `EXEC` | `deviceName, resourceGroupName, roleName, subscriptionId` |
