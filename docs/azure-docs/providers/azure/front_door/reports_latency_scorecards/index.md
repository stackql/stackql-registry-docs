---
title: reports_latency_scorecards
hide_title: false
hide_table_of_contents: false
keywords:
  - reports_latency_scorecards
  - front_door
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

Creates, updates, deletes, gets or lists a <code>reports_latency_scorecards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports_latency_scorecards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.reports_latency_scorecards" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports_latency_scorecards', value: 'view', },
        { label: 'reports_latency_scorecards', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="aggregationInterval" /> | `text` | field from the `properties` object |
| <CopyableCode code="country" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointa" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointb" /> | `text` | field from the `properties` object |
| <CopyableCode code="experimentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="latency_metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Defines a the properties of a Latency Scorecard |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aggregationInterval, experimentName, profileName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports_latency_scorecards', value: 'view', },
        { label: 'reports_latency_scorecards', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
aggregationInterval,
country,
end_date_time_utc,
endpointa,
endpointb,
experimentName,
latency_metrics,
location,
profileName,
resourceGroupName,
start_date_time_utc,
subscriptionId,
tags,
type
FROM azure.front_door.vw_reports_latency_scorecards
WHERE aggregationInterval = '{{ aggregationInterval }}'
AND experimentName = '{{ experimentName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.front_door.reports_latency_scorecards
WHERE aggregationInterval = '{{ aggregationInterval }}'
AND experimentName = '{{ experimentName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

