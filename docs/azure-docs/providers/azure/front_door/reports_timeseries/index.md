---
title: reports_timeseries
hide_title: false
hide_table_of_contents: false
keywords:
  - reports_timeseries
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

Creates, updates, deletes, gets or lists a <code>reports_timeseries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports_timeseries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.reports_timeseries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports_timeseries', value: 'view', },
        { label: 'reports_timeseries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="aggregationInterval" /> | `text` | field from the `properties` object |
| <CopyableCode code="aggregation_interval" /> | `text` | field from the `properties` object |
| <CopyableCode code="country" /> | `text` | field from the `properties` object |
| <CopyableCode code="endDateTimeUTC" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="experimentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="startDateTimeUTC" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="timeseriesType" /> | `text` | field from the `properties` object |
| <CopyableCode code="timeseries_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="timeseries_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Defines the properties of a timeseries |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aggregationInterval, endDateTimeUTC, experimentName, profileName, resourceGroupName, startDateTimeUTC, subscriptionId, timeseriesType" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports_timeseries', value: 'view', },
        { label: 'reports_timeseries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
aggregationInterval,
aggregation_interval,
country,
endDateTimeUTC,
end_date_time_utc,
endpoint,
experimentName,
location,
profileName,
resourceGroupName,
startDateTimeUTC,
start_date_time_utc,
subscriptionId,
tags,
timeseriesType,
timeseries_data,
timeseries_type,
type
FROM azure.front_door.vw_reports_timeseries
WHERE aggregationInterval = '{{ aggregationInterval }}'
AND endDateTimeUTC = '{{ endDateTimeUTC }}'
AND experimentName = '{{ experimentName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND startDateTimeUTC = '{{ startDateTimeUTC }}'
AND subscriptionId = '{{ subscriptionId }}'
AND timeseriesType = '{{ timeseriesType }}';
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
FROM azure.front_door.reports_timeseries
WHERE aggregationInterval = '{{ aggregationInterval }}'
AND endDateTimeUTC = '{{ endDateTimeUTC }}'
AND experimentName = '{{ experimentName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND startDateTimeUTC = '{{ startDateTimeUTC }}'
AND subscriptionId = '{{ subscriptionId }}'
AND timeseriesType = '{{ timeseriesType }}';
```
</TabItem></Tabs>

