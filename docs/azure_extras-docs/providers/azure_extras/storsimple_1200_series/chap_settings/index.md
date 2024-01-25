---
title: chap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - chap_settings
  - storsimple_1200_series
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
<tr><td><b>Name</b></td><td><code>chap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.chap_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | Chap properties |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `chapUserName, deviceName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified chap setting name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the chap settings in a device. |
| `create_or_update` | `INSERT` | `chapUserName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the chap setting. |
| `delete` | `DELETE` | `chapUserName, deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the chap setting. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the chap settings in a device. |
