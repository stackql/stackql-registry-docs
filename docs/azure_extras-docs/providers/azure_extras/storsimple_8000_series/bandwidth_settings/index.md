---
title: bandwidth_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - bandwidth_settings
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
<tr><td><b>Name</b></td><td><code>bandwidth_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.bandwidth_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of the bandwidth setting. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bandwidthSettingName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified bandwidth setting name. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the bandwidth setting in a manager. |
| `create_or_update` | `INSERT` | `bandwidthSettingName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the bandwidth setting |
| `delete` | `DELETE` | `bandwidthSettingName, managerName, resourceGroupName, subscriptionId` | Deletes the bandwidth setting |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the bandwidth setting in a manager. |
