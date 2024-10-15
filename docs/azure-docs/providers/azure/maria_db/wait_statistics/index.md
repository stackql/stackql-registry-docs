---
title: wait_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - wait_statistics
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>wait_statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wait_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.wait_statistics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_wait_statistics', value: 'view', },
        { label: 'wait_statistics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="count" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_time_in_ms" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="waitStatisticsId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a wait statistic. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, waitStatisticsId" /> | Retrieve wait statistics for specified identifier. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__properties" /> | Retrieve wait statistics for specified aggregation window. |

## `SELECT` examples

Retrieve wait statistics for specified identifier.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_wait_statistics', value: 'view', },
        { label: 'wait_statistics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
count,
database_name,
end_time,
event_name,
event_type_name,
query_id,
resourceGroupName,
serverName,
start_time,
subscriptionId,
total_time_in_ms,
user_id,
waitStatisticsId
FROM azure.maria_db.vw_wait_statistics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND waitStatisticsId = '{{ waitStatisticsId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.maria_db.wait_statistics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND waitStatisticsId = '{{ waitStatisticsId }}';
```
</TabItem></Tabs>

