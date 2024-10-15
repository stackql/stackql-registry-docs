---
title: applied_reservation_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - applied_reservation_lists
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

Creates, updates, deletes, gets or lists a <code>applied_reservation_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applied_reservation_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.applied_reservation_lists" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applied_reservation_lists', value: 'view', },
        { label: 'applied_reservation_lists', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Identifier of the applied reservations |
| <CopyableCode code="name" /> | `text` | Name of resource |
| <CopyableCode code="reservation_order_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. "Microsoft.Capacity/AppliedReservations" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the applied reservations |
| <CopyableCode code="name" /> | `string` | Name of resource |
| <CopyableCode code="properties" /> | `object` | Properties for applied reservations returned |
| <CopyableCode code="type" /> | `string` | Type of resource. "Microsoft.Capacity/AppliedReservations" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get applicable `Reservation`s that are applied to this subscription or a resource group under this subscription. |

## `SELECT` examples

Get applicable `Reservation`s that are applied to this subscription or a resource group under this subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applied_reservation_lists', value: 'view', },
        { label: 'applied_reservation_lists', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
reservation_order_ids,
subscriptionId,
type
FROM azure.reservations.vw_applied_reservation_lists
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.reservations.applied_reservation_lists
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

