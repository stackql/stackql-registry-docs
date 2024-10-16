---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
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

Creates, updates, deletes, gets or lists a <code>reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservations" /></td></tr>
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
| <CopyableCode code="kind" /> | `text` | Resource Provider type to be reserved. |
| <CopyableCode code="last_updated_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The Azure region where the reserved resource lives. |
| <CopyableCode code="merge_properties" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="sku" /> | `text` | The name of sku |
| <CopyableCode code="sku_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="split_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="swap_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_friendly_applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_friendly_renew_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="utilization" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `integer` |  |
| <CopyableCode code="kind" /> | `string` | Resource Provider type to be reserved. |
| <CopyableCode code="location" /> | `string` | The Azure region where the reserved resource lives. |
| <CopyableCode code="properties" /> | `object` | The properties of the reservations |
| <CopyableCode code="sku" /> | `object` | The name of sku |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reservationId, reservationOrderId" /> | Get specific `Reservation` details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reservationOrderId" /> | List `Reservation`s within a single `ReservationOrder`. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="" /> | List the reservations and the roll up counts of reservations group by provisioning states that the user has access to in the current tenant. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="reservationId, reservationOrderId" /> | Updates the applied scopes of the `Reservation`. |
| <CopyableCode code="archive" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Archiving a `Reservation` moves it to `Archived` state. |
| <CopyableCode code="available_scopes" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Check whether the scopes from request is valid for `Reservation`. |
| <CopyableCode code="merge" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Merge the specified `Reservation`s into a new `Reservation`. The two `Reservation`s being merged must have same properties. |
| <CopyableCode code="split" /> | `EXEC` | <CopyableCode code="reservationOrderId" /> | Split a `Reservation` into two `Reservation`s with specified quantity distribution. |
| <CopyableCode code="unarchive" /> | `EXEC` | <CopyableCode code="reservationId, reservationOrderId" /> | Restores a `Reservation` to the state it was before archiving. |

## `SELECT` examples

List the reservations and the roll up counts of reservations group by provisioning states that the user has access to in the current tenant.

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
kind,
last_updated_date_time,
location,
merge_properties,
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
term,
user_friendly_applied_scope_type,
user_friendly_renew_state,
utilization
FROM azure.reservations.vw_reservations
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
kind,
location,
properties,
sku
FROM azure.reservations.reservations
;
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>reservations</code> resource.

```sql
/*+ update */
UPDATE azure.reservations.reservations
SET 
properties = '{{ properties }}'
WHERE 
reservationId = '{{ reservationId }}'
AND reservationOrderId = '{{ reservationOrderId }}';
```
