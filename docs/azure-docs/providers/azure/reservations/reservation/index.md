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
| `etag` | `integer` |  |
| `kind` | `string` | Resource Provider type to be reserved. |
| `location` | `string` | The Azure region where the reserved resource lives. |
| `properties` | `object` | The properties of the reservations |
| `sku` | `object` | The name of sku |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `reservationId, reservationOrderId` | Get specific `Reservation` details. |
| `list` | `SELECT` | `reservationOrderId` | List `Reservation`s within a single `ReservationOrder`. |
| `_list` | `EXEC` | `reservationOrderId` | List `Reservation`s within a single `ReservationOrder`. |
| `archive` | `EXEC` | `reservationId, reservationOrderId` | Archiving a `Reservation` moves it to `Archived` state. |
| `available_scopes` | `EXEC` | `reservationId, reservationOrderId` | Check whether the scopes from request is valid for `Reservation`.<br /> |
| `merge` | `EXEC` | `reservationOrderId` | Merge the specified `Reservation`s into a new `Reservation`. The two `Reservation`s being merged must have same properties. |
| `split` | `EXEC` | `reservationOrderId` | Split a `Reservation` into two `Reservation`s with specified quantity distribution. |
| `unarchive` | `EXEC` | `reservationId, reservationOrderId` | Restores a `Reservation` to the state it was before archiving.<br /> |
| `update` | `EXEC` | `reservationId, reservationOrderId` | Updates the applied scopes of the `Reservation`. |
