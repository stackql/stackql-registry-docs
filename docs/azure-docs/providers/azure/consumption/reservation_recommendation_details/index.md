---
title: reservation_recommendation_details
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_recommendation_details
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

Creates, updates, deletes, gets or lists a <code>reservation_recommendation_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation_recommendation_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservation_recommendation_details" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservation_recommendation_details', value: 'view', },
        { label: 'reservation_recommendation_details', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `text` | The ID that uniquely identifies an event.  |
| <CopyableCode code="currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag for the resource. |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="lookBackPeriod" /> | `text` | field from the `properties` object |
| <CopyableCode code="product" /> | `text` | field from the `properties` object |
| <CopyableCode code="region" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceScope" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="savings" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Resource sku |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="usage" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event.  |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | The properties of the reservation recommendation. |
| <CopyableCode code="sku" /> | `string` | Resource sku |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="lookBackPeriod, product, region, resourceScope, scope, term" /> | Details of a reservation recommendation for what-if analysis of reserved instances. |

## `SELECT` examples

Details of a reservation recommendation for what-if analysis of reserved instances.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservation_recommendation_details', value: 'view', },
        { label: 'reservation_recommendation_details', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
currency,
etag,
location,
lookBackPeriod,
product,
region,
resource,
resourceScope,
resource_group,
savings,
scope,
sku,
tags,
term,
type,
usage
FROM azure.consumption.vw_reservation_recommendation_details
WHERE lookBackPeriod = '{{ lookBackPeriod }}'
AND product = '{{ product }}'
AND region = '{{ region }}'
AND resourceScope = '{{ resourceScope }}'
AND scope = '{{ scope }}'
AND term = '{{ term }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
sku,
tags,
type
FROM azure.consumption.reservation_recommendation_details
WHERE lookBackPeriod = '{{ lookBackPeriod }}'
AND product = '{{ product }}'
AND region = '{{ region }}'
AND resourceScope = '{{ resourceScope }}'
AND scope = '{{ scope }}'
AND term = '{{ term }}';
```
</TabItem></Tabs>

