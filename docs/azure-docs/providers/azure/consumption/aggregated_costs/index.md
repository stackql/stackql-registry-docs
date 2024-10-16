---
title: aggregated_costs
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregated_costs
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

Creates, updates, deletes, gets or lists a <code>aggregated_costs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aggregated_costs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.aggregated_costs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_aggregated_costs', value: 'view', },
        { label: 'aggregated_costs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `text` | The ID that uniquely identifies an event. |
| <CopyableCode code="azure_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_period_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="charges_billed_separately" /> | `text` | field from the `properties` object |
| <CopyableCode code="children" /> | `text` | field from the `properties` object |
| <CopyableCode code="currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag for the resource. |
| <CopyableCode code="excluded_subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="included_subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="managementGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="usage_end" /> | `text` | field from the `properties` object |
| <CopyableCode code="usage_start" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event. |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the Management Group Aggregated Cost. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_management_group" /> | `SELECT` | <CopyableCode code="managementGroupId" /> | Provides the aggregate cost of a management group and all child management groups by current billing period. |

## `SELECT` examples

Provides the aggregate cost of a management group and all child management groups by current billing period.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_aggregated_costs', value: 'view', },
        { label: 'aggregated_costs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azure_charges,
billing_period_id,
charges_billed_separately,
children,
currency,
etag,
excluded_subscriptions,
included_subscriptions,
managementGroupId,
marketplace_charges,
tags,
type,
usage_end,
usage_start
FROM azure.consumption.vw_aggregated_costs
WHERE managementGroupId = '{{ managementGroupId }}';
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
FROM azure.consumption.aggregated_costs
WHERE managementGroupId = '{{ managementGroupId }}';
```
</TabItem></Tabs>

