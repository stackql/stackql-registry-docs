---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - edge_order
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

Creates, updates, deletes, gets or lists a <code>orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order.orders" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_orders', value: 'view', },
        { label: 'orders', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="current_stage" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="orderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="order_item_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="order_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="order_stage_history" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Represents order details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, orderName, resourceGroupName, subscriptionId" /> | Get an order. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List orders at resource group level. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List orders at subscription level. |

## `SELECT` examples

List orders at subscription level.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_orders', value: 'view', },
        { label: 'orders', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
current_stage,
location,
orderName,
order_item_ids,
order_mode,
order_stage_history,
resourceGroupName,
subscriptionId
FROM azure_extras.edge_order.vw_orders
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.edge_order.orders
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

