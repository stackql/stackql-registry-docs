---
title: reservation_order
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_order
  - reservations
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
<tr><td><b>Name</b></td><td><code>reservation_order</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.reservations.reservation_order</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the reservation |
| `name` | `string` | Name of the reservation |
| `etag` | `integer` |  |
| `properties` | `object` | Properties of a reservation order. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of resource. "Microsoft.Capacity/reservations" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `reservationOrderId` | Get the details of the `ReservationOrder`. |
| `list` | `SELECT` |  | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| `_list` | `EXEC` |  | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| `calculate` | `EXEC` |  | Calculate price for placing a `ReservationOrder`. |
| `change_directory` | `EXEC` | `reservationOrderId` | Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id |
| `purchase` | `EXEC` | `reservationOrderId` | Purchase `ReservationOrder` and create resource under the specified URI. |
