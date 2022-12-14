---
title: reservations_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_summaries
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
<tr><td><b>Name</b></td><td><code>reservations_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.reservations_summaries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The full qualified ARM ID of an event. |
| `name` | `string` | The ID that uniquely identifies an event.  |
| `properties` | `object` | The properties of the reservation summary. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | The etag for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationsSummaries_List` | `SELECT` | `grain, resourceScope` | Lists the reservations summaries for the defined scope daily or monthly grain. |
| `ReservationsSummaries_ListByReservationOrder` | `SELECT` | `grain, reservationOrderId` | Lists the reservations summaries for daily or monthly grain. |
| `ReservationsSummaries_ListByReservationOrderAndReservation` | `SELECT` | `grain, reservationId, reservationOrderId` | Lists the reservations summaries for daily or monthly grain. |
