---
title: reservation_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_orders
  - billing
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.reservation_orders" /></td></tr>
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
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `integer` | field from the `properties` object |
| <CopyableCode code="expiry_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_status_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="original_quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservationOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservations" /> | `text` | field from the `properties` object |
| <CopyableCode code="review_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="properties" /> | `object` | Properties of a reservation order. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, reservationOrderId" /> | Get the details of the ReservationOrder in the billing account. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | List all the `ReservationOrders in the billing account. |

## `SELECT` examples

List all the `ReservationOrders in the billing account.

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
benefit_start_time,
billingAccountName,
billing_account_id,
billing_plan,
billing_profile_id,
created_date_time,
customer_id,
display_name,
enrollment_id,
etag,
expiry_date,
expiry_date_time,
extended_status_info,
original_quantity,
plan_information,
product_code,
provisioning_state,
request_date_time,
reservationOrderId,
reservations,
review_date_time,
tags,
term
FROM azure.billing.vw_reservation_orders
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
tags
FROM azure.billing.reservation_orders
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

