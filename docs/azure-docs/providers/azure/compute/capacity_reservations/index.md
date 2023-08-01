---
title: capacity_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservations
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
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.capacity_reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties of the Capacity reservation. |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `zones` | `array` | Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CapacityReservations_Get` | `SELECT` | `capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId` | The operation that retrieves information about the capacity reservation. |
| `CapacityReservations_ListByCapacityReservationGroup` | `SELECT` | `capacityReservationGroupName, resourceGroupName, subscriptionId` | Lists all of the capacity reservations in the specified capacity reservation group. Use the nextLink property in the response to get the next page of capacity reservations. |
| `CapacityReservations_CreateOrUpdate` | `INSERT` | `capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId, data__sku` | The operation to create or update a capacity reservation. Please note some properties can be set only during capacity reservation creation. Please refer to https://aka.ms/CapacityReservation for more details. |
| `CapacityReservations_Delete` | `DELETE` | `capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId` | The operation to delete a capacity reservation. This operation is allowed only when all the associated resources are disassociated from the capacity reservation. Please refer to https://aka.ms/CapacityReservation for more details. |
| `CapacityReservations_Update` | `EXEC` | `capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId` | The operation to update a capacity reservation. |
