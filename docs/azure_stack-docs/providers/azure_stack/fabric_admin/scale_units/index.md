---
title: scale_units
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>scale_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.scale_units</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | Properties of a scale unit. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, resourceGroupName, scaleUnit, subscriptionId` | Returns the requested scale unit. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all scale units at a location. |
| `create` | `INSERT` | `location, resourceGroupName, scaleUnit, subscriptionId` | Add a new scale unit. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns a list of all scale units at a location. |
| `scale_out` | `EXEC` | `location, resourceGroupName, scaleUnit, subscriptionId` | Scales out a scale unit. |
| `set_gpu_partition_size` | `EXEC` | `location, resourceGroupName, scaleUnit, subscriptionId` | Set GPU partition size. |
