---
title: reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation
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
<tr><td><b>Name</b></td><td><code>reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.reservations.reservation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the reservation |
| `name` | `string` | Name of the reservation |
| `location` | `string` | The Azure Region where the reserved resource lives. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of resource. "Microsoft.Capacity/reservationOrders/reservations" |
| `properties` | `object` | The properties of the reservations |
| `kind` | `string` | Resource Provider type to be reserved. |
| `etag` | `integer` |  |
| `sku` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Reservation_Get` | `SELECT` | `reservationId, reservationOrderId` | Get specific `Reservation` details. |
| `Reservation_List` | `SELECT` | `reservationOrderId` | List `Reservation`s within a single `ReservationOrder`. |
| `Reservation_ListAll` | `SELECT` |  | List the reservations and the roll up counts of reservations group by provisioning states that the user has access to in the current tenant. |
| `Reservation_Archive` | `EXEC` | `reservationId, reservationOrderId` | Archiving a `Reservation` moves it to `Archived` state. |
| `Reservation_AvailableScopes` | `EXEC` | `reservationId, reservationOrderId` | Get Available Scopes for `Reservation`.<br /> |
| `Reservation_ListRevisions` | `EXEC` | `reservationId, reservationOrderId` | List of all the revisions for the `Reservation`. |
| `Reservation_Merge` | `EXEC` | `reservationOrderId` | Merge the specified `Reservation`s into a new `Reservation`. The two `Reservation`s being merged must have same properties. |
| `Reservation_Split` | `EXEC` | `reservationOrderId` | Split a `Reservation` into two `Reservation`s with specified quantity distribution. |
| `Reservation_Unarchive` | `EXEC` | `reservationId, reservationOrderId` | Unarchiving a `Reservation` moves it to the state it was before archiving.<br /> |
| `Reservation_Update` | `EXEC` | `reservationId, reservationOrderId` | Updates the applied scopes of the `Reservation`. |
