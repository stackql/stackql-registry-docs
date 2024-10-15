---
title: sql_pool_data_warehouse_user_activities
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_data_warehouse_user_activities
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_data_warehouse_user_activities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_data_warehouse_user_activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_data_warehouse_user_activities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_data_warehouse_user_activities', value: 'view', },
        { label: 'sql_pool_data_warehouse_user_activities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="active_queries_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataWarehouseUserActivityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | User activities of a data warehouse. This currently includes the count of running or suspended queries. For more information, please view the sys.dm_pdw_exec_requests dynamic management view (DMV). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataWarehouseUserActivityName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Gets the user activities of a SQL pool which includes running and suspended queries |

## `SELECT` examples

Gets the user activities of a SQL pool which includes running and suspended queries

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_data_warehouse_user_activities', value: 'view', },
        { label: 'sql_pool_data_warehouse_user_activities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
active_queries_count,
dataWarehouseUserActivityName,
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName
FROM azure.synapse.vw_sql_pool_data_warehouse_user_activities
WHERE dataWarehouseUserActivityName = '{{ dataWarehouseUserActivityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.sql_pool_data_warehouse_user_activities
WHERE dataWarehouseUserActivityName = '{{ dataWarehouseUserActivityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

