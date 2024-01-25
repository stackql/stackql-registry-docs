---
title: proximity_placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - proximity_placement_groups
  - compute
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
<tr><td><b>Name</b></td><td><code>proximity_placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.proximity_placement_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a Proximity Placement Group. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `zones` | `array` | Specifies the Availability Zone where virtual machine, virtual machine scale set or availability set associated with the  proximity placement group can be created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Retrieves information about a proximity placement group . |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all proximity placement groups in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all proximity placement groups in a subscription. |
| `create_or_update` | `INSERT` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Create or update a proximity placement group. |
| `delete` | `DELETE` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Delete a proximity placement group. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all proximity placement groups in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all proximity placement groups in a subscription. |
| `update` | `EXEC` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Update a proximity placement group. |
