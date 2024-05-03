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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation_order</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation_order" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the reservation |
| <CopyableCode code="name" /> | `string` | Name of the reservation |
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="properties" /> | `object` | Properties of a reservation order. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of resource. "Microsoft.Capacity/reservations" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reservationOrderId" /> | Get the details of the `ReservationOrder`. |
| <CopyableCode code="list" /> | `SELECT` |  | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| <CopyableCode code="_list" /> | `EXEC` |  | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| <CopyableCode code="calculate" /> | `EXEC` |  | Calculate price for placing a `ReservationOrder`. |
| <CopyableCode code="change_directory" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id |
| <CopyableCode code="purchase" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Purchase `ReservationOrder` and create resource under the specified URI. |
