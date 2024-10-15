---
title: sql_pool_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_columns
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

Creates, updates, deletes, gets or lists a <code>sql_pool_columns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_columns" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_columns', value: 'view', },
        { label: 'sql_pool_columns', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="columnName" /> | `text` | field from the `properties` object |
| <CopyableCode code="column_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_computed" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Sql pool column properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, resourceGroupName, schemaName, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Get Sql pool column |

## `SELECT` examples

Get Sql pool column

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_columns', value: 'view', },
        { label: 'sql_pool_columns', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
columnName,
column_type,
is_computed,
resourceGroupName,
schemaName,
sqlPoolName,
subscriptionId,
tableName,
workspaceName
FROM azure.synapse.vw_sql_pool_columns
WHERE columnName = '{{ columnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.sql_pool_columns
WHERE columnName = '{{ columnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

