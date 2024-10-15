---
title: top_query_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - top_query_statistics
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

Creates, updates, deletes, gets or lists a <code>top_query_statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>top_query_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.top_query_statistics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_top_query_statistics', value: 'view', },
        { label: 'top_query_statistics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aggregation_function" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="metric_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="metric_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="metric_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="metric_value_unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="queryStatisticId" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_execution_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a query statistic. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="queryStatisticId, resourceGroupName, serverName, subscriptionId" /> | Retrieve the query statistic for specified identifier. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__properties" /> | Retrieve the Query-Store top queries for specified metric and aggregation. |

## `SELECT` examples

Retrieve the query statistic for specified identifier.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_top_query_statistics', value: 'view', },
        { label: 'top_query_statistics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aggregation_function,
database_names,
end_time,
metric_display_name,
metric_name,
metric_value,
metric_value_unit,
queryStatisticId,
query_execution_count,
query_id,
resourceGroupName,
serverName,
start_time,
subscriptionId
FROM azure.maria_db.vw_top_query_statistics
WHERE queryStatisticId = '{{ queryStatisticId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.maria_db.top_query_statistics
WHERE queryStatisticId = '{{ queryStatisticId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

