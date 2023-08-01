---
title: hardware_component_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - hardware_component_groups
  - stor_simple_8000_series
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
<tr><td><b>Name</b></td><td><code>hardware_component_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.hardware_component_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties of hardware component group. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HardwareComponentGroups_ListByDevice` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Lists the hardware component groups at device-level. |
| `HardwareComponentGroups_ChangeControllerPowerState` | `EXEC` | `deviceName, hardwareComponentGroupName, managerName, resourceGroupName, subscriptionId, data__properties` | Changes the power state of the controller. |
