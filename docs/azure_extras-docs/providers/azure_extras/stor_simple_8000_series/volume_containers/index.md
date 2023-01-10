---
title: volume_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_containers
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
<tr><td><b>Name</b></td><td><code>volume_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.volume_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of volume container. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VolumeContainers_Get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Gets the properties of the specified volume container name. |
| `VolumeContainers_ListByDevice` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the volume containers in a device. |
| `VolumeContainers_CreateOrUpdate` | `INSERT` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, data__properties` | Creates or updates the volume container. |
| `VolumeContainers_Delete` | `DELETE` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Deletes the volume container. |
| `VolumeContainers_ListMetricDefinition` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Gets the metric definitions for the specified volume container. |
| `VolumeContainers_ListMetrics` | `EXEC` | `$filter, deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` | Gets the metrics for the specified volume container. |
