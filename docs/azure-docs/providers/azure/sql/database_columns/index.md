---
title: database_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - database_columns
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

Creates, updates, deletes, gets or lists a <code>database_columns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_columns" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_columns', value: 'view', },
        { label: 'database_columns', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="columnName" /> | `text` | field from the `properties` object |
| <CopyableCode code="column_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_computed" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_optimized" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="temporal_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Database column properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName" /> | Get database column |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | List database columns |
| <CopyableCode code="list_by_table" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName" /> | List database columns |

## `SELECT` examples

List database columns

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_columns', value: 'view', },
        { label: 'database_columns', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
columnName,
column_type,
databaseName,
is_computed,
memory_optimized,
resourceGroupName,
schemaName,
serverName,
subscriptionId,
tableName,
temporal_type
FROM azure.sql.vw_database_columns
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.database_columns
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

