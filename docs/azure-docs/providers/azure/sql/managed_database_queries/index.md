---
title: managed_database_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_queries
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

Creates, updates, deletes, gets or lists a <code>managed_database_queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_queries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_queries', value: 'view', },
        { label: 'managed_database_queries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="queryId" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_text" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a database query. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId" /> | Get query by query id. |
| <CopyableCode code="list_by_query" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId" /> | Get query execution statistics by query id. |

## `SELECT` examples

Get query by query id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_queries', value: 'view', },
        { label: 'managed_database_queries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
managedInstanceName,
queryId,
query_text,
resourceGroupName,
subscriptionId
FROM azure.sql.vw_managed_database_queries
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND queryId = '{{ queryId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_database_queries
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND queryId = '{{ queryId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

