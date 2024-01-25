---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of volume. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName` | Returns the properties of the specified volume name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the volumes in a device. |
| `list_by_volume_container` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Retrieves all the volumes in a volume container. |
| `create_or_update` | `INSERT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName, data__properties` | Creates or updates the volume. |
| `delete` | `DELETE` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName` | Deletes the volume. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the volumes in a device. |
| `_list_by_volume_container` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Retrieves all the volumes in a volume container. |
