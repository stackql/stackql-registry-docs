---
title: time_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - time_zones
  - sql
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

Creates, updates, deletes, gets or lists a <code>time_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>time_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.time_zones" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_time_zones', value: 'view', },
        { label: 'time_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="timeZoneId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a time zone. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId, timeZoneId" /> | Gets a managed instance time zone. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets a list of managed instance time zones by location. |

## `SELECT` examples

Gets a list of managed instance time zones by location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_time_zones', value: 'view', },
        { label: 'time_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
display_name,
locationName,
subscriptionId,
timeZoneId,
time_zone_id
FROM azure.sql.vw_time_zones
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.time_zones
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

