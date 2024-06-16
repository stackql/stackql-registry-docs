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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="kind" /> | `string` | Resource Provider type to be reserved. |
| <CopyableCode code="location" /> | `string` | The Azure region where the reserved resource lives. |
| <CopyableCode code="properties" /> | `object` | The properties of the reservations |
| <CopyableCode code="sku" /> | `object` | The name of sku |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reservationId, reservationOrderId" /> | Get specific `Reservation` details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reservationOrderId" /> | List `Reservation`s within a single `ReservationOrder`. |
| <CopyableCode code="archive" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Archiving a `Reservation` moves it to `Archived` state. |
| <CopyableCode code="available_scopes" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Check whether the scopes from request is valid for `Reservation`.<br /> |
| <CopyableCode code="merge" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Merge the specified `Reservation`s into a new `Reservation`. The two `Reservation`s being merged must have same properties. |
| <CopyableCode code="split" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Split a `Reservation` into two `Reservation`s with specified quantity distribution. |
| <CopyableCode code="unarchive" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Restores a `Reservation` to the state it was before archiving.<br /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Updates the applied scopes of the `Reservation`. |
