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
| `zones` | `array` | Specifies the Availability Zone where virtual machine, virtual machine scale set or availability set associated with the  proximity placement group can be created. |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a Proximity Placement Group. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProximityPlacementGroups_Get` | `SELECT` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Retrieves information about a proximity placement group . |
| `ProximityPlacementGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all proximity placement groups in a resource group. |
| `ProximityPlacementGroups_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all proximity placement groups in a subscription. |
| `ProximityPlacementGroups_CreateOrUpdate` | `INSERT` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Create or update a proximity placement group. |
| `ProximityPlacementGroups_Delete` | `DELETE` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Delete a proximity placement group. |
| `ProximityPlacementGroups_Update` | `EXEC` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Update a proximity placement group. |
