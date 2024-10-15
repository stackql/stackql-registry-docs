---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
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

Creates, updates, deletes, gets or lists a <code>reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.reservations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservations', value: 'view', },
        { label: 'reservations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applied_scope_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="archived" /> | `text` | field from the `properties` object |
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_scope_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="effective_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `integer` | field from the `properties` object |
| <CopyableCode code="expiry_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_status_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_flexibility" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the reservation. |
| <CopyableCode code="merge_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_sub_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservationOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="reserved_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="review_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The property of reservation sku object. |
| <CopyableCode code="sku_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="split_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="swap_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_friendly_applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_friendly_renew_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="utilization" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="location" /> | `string` | The location of the reservation. |
| <CopyableCode code="properties" /> | `object` | The property of reservation object. |
| <CopyableCode code="sku" /> | `object` | The property of reservation sku object. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_reservation_order" /> | `SELECT` | <CopyableCode code="billingAccountName, reservationId, reservationOrderId" /> | Get specific Reservation details in the billing account. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the reservations in the billing account and the roll up counts of reservations group by provisioning states. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the reservations for a billing profile and the roll up counts of reservations group by provisioning state. |
| <CopyableCode code="list_by_reservation_order" /> | `SELECT` | <CopyableCode code="billingAccountName, reservationOrderId" /> | List Reservations within a single ReservationOrder in the billing account. |
| <CopyableCode code="update_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, reservationId, reservationOrderId" /> | Update reservation by billing account. |

## `SELECT` examples

Lists the reservations in the billing account and the roll up counts of reservations group by provisioning states.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservations', value: 'view', },
        { label: 'reservations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
applied_scope_properties,
applied_scope_type,
applied_scopes,
archived,
benefit_start_time,
billingAccountName,
billing_plan,
billing_scope_id,
capabilities,
display_name,
display_provisioning_state,
effective_date_time,
etag,
expiry_date,
expiry_date_time,
extended_status_info,
instance_flexibility,
last_updated_date_time,
location,
merge_properties,
product_code,
provisioning_state,
provisioning_sub_state,
purchase_date,
purchase_date_time,
quantity,
renew,
renew_destination,
renew_properties,
renew_source,
reservationId,
reservationOrderId,
reserved_resource_type,
review_date_time,
sku,
sku_description,
split_properties,
swap_properties,
tags,
term,
user_friendly_applied_scope_type,
user_friendly_renew_state,
utilization
FROM azure.billing.vw_reservations
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
sku,
tags
FROM azure.billing.reservations
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

