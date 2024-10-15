---
title: price_sheets
hide_title: false
hide_table_of_contents: false
keywords:
  - price_sheets
  - consumption
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

Creates, updates, deletes, gets or lists a <code>price_sheets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>price_sheets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.price_sheets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_price_sheets', value: 'view', },
        { label: 'price_sheets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `text` | The ID that uniquely identifies an event.  |
| <CopyableCode code="billingPeriodName" /> | `text` | field from the `properties` object |
| <CopyableCode code="download" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag for the resource. |
| <CopyableCode code="next_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="pricesheets" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event.  |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="properties" /> | `object` | price sheet result. It contains the pricesheet associated with billing period |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the price sheet for a subscription. Price sheet is available via this API only for May 1, 2014 or later. |
| <CopyableCode code="get_by_billing_period" /> | `SELECT` | <CopyableCode code="billingPeriodName, subscriptionId" /> | Get the price sheet for a scope by subscriptionId and billing period. Price sheet is available via this API only for May 1, 2014 or later. |
| <CopyableCode code="download_by_billing_account_period" /> | `EXEC` | <CopyableCode code="billingAccountId, billingPeriodName" /> | Generates the pricesheet for the provided billing period asynchronously based on the enrollment id |

## `SELECT` examples

Gets the price sheet for a subscription. Price sheet is available via this API only for May 1, 2014 or later.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_price_sheets', value: 'view', },
        { label: 'price_sheets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
billingPeriodName,
download,
etag,
next_link,
pricesheets,
subscriptionId,
tags,
type
FROM azure.consumption.vw_price_sheets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
tags,
type
FROM azure.consumption.price_sheets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

