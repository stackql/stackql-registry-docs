---
title: monitoring_config
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_config
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
<tr><td><b>Name</b></td><td><code>monitoring_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.monitoring_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
| `properties` | `object` | Metrics properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MonitoringConfig_List` | `SELECT` | `deviceName, resourceGroupName, roleName, subscriptionId` |
| `MonitoringConfig_CreateOrUpdate` | `INSERT` | `deviceName, resourceGroupName, roleName, subscriptionId, data__properties` |
| `MonitoringConfig_Delete` | `DELETE` | `deviceName, resourceGroupName, roleName, subscriptionId` |
| `MonitoringConfig_Get` | `EXEC` | `deviceName, resourceGroupName, roleName, subscriptionId` |
