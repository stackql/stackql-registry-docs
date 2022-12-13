---
title: capacity_reservation_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_groups
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
<tr><td><b>Name</b></td><td><code>capacity_reservation_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.capacity_reservation_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `zones` | `array` | Availability Zones to use for this capacity reservation group. The zones can be assigned only during creation. If not provided, the group supports only regional resources in the region. If provided, enforces each capacity reservation in the group to be in one of the zones. |
| `location` | `string` | Resource location |
| `properties` | `object` | capacity reservation group Properties. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CapacityReservationGroups_Get` | `SELECT` | `capacityReservationGroupName, resourceGroupName, subscriptionId` | The operation that retrieves information about a capacity reservation group. |
| `CapacityReservationGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the capacity reservation groups in the specified resource group. Use the nextLink property in the response to get the next page of capacity reservation groups. |
| `CapacityReservationGroups_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the capacity reservation groups in the subscription. Use the nextLink property in the response to get the next page of capacity reservation groups. |
| `CapacityReservationGroups_CreateOrUpdate` | `INSERT` | `capacityReservationGroupName, resourceGroupName, subscriptionId` | The operation to create or update a capacity reservation group. When updating a capacity reservation group, only tags may be modified. Please refer to https://aka.ms/CapacityReservation for more details. |
| `CapacityReservationGroups_Delete` | `DELETE` | `capacityReservationGroupName, resourceGroupName, subscriptionId` | The operation to delete a capacity reservation group. This operation is allowed only if all the associated resources are disassociated from the reservation group and all capacity reservations under the reservation group have also been deleted. Please refer to https://aka.ms/CapacityReservation for more details. |
| `CapacityReservationGroups_Update` | `EXEC` | `capacityReservationGroupName, resourceGroupName, subscriptionId` | The operation to update a capacity reservation group. When updating a capacity reservation group, only tags may be modified. |
