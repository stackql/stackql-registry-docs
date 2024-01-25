---
title: device_settings_network_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - device_settings_network_settings
  - storsimple_8000_series
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
<tr><td><b>Name</b></td><td><code>device_settings_network_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.device_settings_network_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of the network settings of device. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets the network settings of the specified device. |
| `update` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Updates the network settings on the specified device. |
