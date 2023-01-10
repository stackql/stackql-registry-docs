---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties of volume. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Volumes_Get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName` | Returns the properties of the specified volume name. |
| `Volumes_ListByDevice` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the volumes in a device. |
| `Volumes_ListByVolumeContainer` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Retrieves all the volumes in a volume container. |
| `Volumes_CreateOrUpdate` | `INSERT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName, data__properties` | Creates or updates the volume. |
| `Volumes_Delete` | `DELETE` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName` | Deletes the volume. |
| `Volumes_ListMetricDefinition` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName` | Gets the metric definitions for the specified volume. |
| `Volumes_ListMetrics` | `EXEC` | `$filter, deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName` | Gets the metrics for the specified volume. |
