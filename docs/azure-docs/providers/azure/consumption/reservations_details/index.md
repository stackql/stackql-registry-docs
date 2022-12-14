---
title: reservations_details
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_details
  - consumption
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
<tr><td><b>Name</b></td><td><code>reservations_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.reservations_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The full qualified ARM ID of an event. |
| `name` | `string` | The ID that uniquely identifies an event.  |
| `type` | `string` | Resource type. |
| `etag` | `string` | The etag for the resource. |
| `properties` | `object` | The properties of the reservation detail. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationsDetails_List` | `SELECT` | `resourceScope` | Lists the reservations details for the defined scope and provided date range. Note: ARM has a payload size limit of 12MB, so currently callers get 502 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
| `ReservationsDetails_ListByReservationOrder` | `SELECT` | `$filter, reservationOrderId` | Lists the reservations details for provided date range. Note: ARM has a payload size limit of 12MB, so currently callers get 502 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
| `ReservationsDetails_ListByReservationOrderAndReservation` | `SELECT` | `$filter, reservationId, reservationOrderId` | Lists the reservations details for provided date range. Note: ARM has a payload size limit of 12MB, so currently callers get 502 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
