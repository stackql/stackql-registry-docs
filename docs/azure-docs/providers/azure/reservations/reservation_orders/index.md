---
title: reservation_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_orders
  - reservations
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>reservation_orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation_orders" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservation_orders', value: 'view', },
        { label: 'reservation_orders', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Identifier of the reservation |
| <CopyableCode code="name" /> | `text` | Name of the reservation |
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `integer` | field from the `properties` object |
| <CopyableCode code="expiry_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="original_quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservationOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservations" /> | `text` | field from the `properties` object |
| <CopyableCode code="review_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. "Microsoft.Capacity/reservations" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the reservation |
| <CopyableCode code="name" /> | `string` | Name of the reservation |
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="properties" /> | `object` | Properties of a reservation order. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of resource. "Microsoft.Capacity/reservations" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reservationOrderId" /> | Get the details of the `ReservationOrder`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| <CopyableCode code="calculate" /> | `EXEC` | <CopyableCode code="" /> | Calculate price for placing a `ReservationOrder`. |
| <CopyableCode code="change_directory" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id |
| <CopyableCode code="purchase" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Purchase `ReservationOrder` and create resource under the specified URI. |

## `SELECT` examples

List of all the `ReservationOrder`s that the user has access to in the current tenant.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservation_orders', value: 'view', },
        { label: 'reservation_orders', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
benefit_start_time,
billing_plan,
created_date_time,
display_name,
etag,
expiry_date,
expiry_date_time,
original_quantity,
plan_information,
provisioning_state,
request_date_time,
reservationOrderId,
reservations,
review_date_time,
system_data,
term,
type
FROM azure.reservations.vw_reservation_orders
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.reservations.reservation_orders
;
```
</TabItem></Tabs>

