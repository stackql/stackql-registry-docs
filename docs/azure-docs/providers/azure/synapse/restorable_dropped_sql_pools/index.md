---
title: restorable_dropped_sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_sql_pools
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

Creates, updates, deletes, gets or lists a <code>restorable_dropped_sql_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restorable_dropped_sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.restorable_dropped_sql_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_dropped_sql_pools', value: 'view', },
        { label: 'restorable_dropped_sql_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="elastic_pool_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorableDroppedSqlPoolId" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level_objective" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a restorable dropped Sql pool |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorableDroppedSqlPoolId, subscriptionId, workspaceName" /> | Gets a deleted sql pool that can be restored |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets a list of deleted Sql pools that can be restored |

## `SELECT` examples

Gets a list of deleted Sql pools that can be restored

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_dropped_sql_pools', value: 'view', },
        { label: 'restorable_dropped_sql_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_date,
database_name,
deletion_date,
earliest_restore_date,
edition,
elastic_pool_name,
location,
max_size_bytes,
resourceGroupName,
restorableDroppedSqlPoolId,
service_level_objective,
subscriptionId,
workspaceName
FROM azure.synapse.vw_restorable_dropped_sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure.synapse.restorable_dropped_sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

