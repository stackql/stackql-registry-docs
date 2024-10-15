---
title: managed_database_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_tables
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

Creates, updates, deletes, gets or lists a <code>managed_database_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_tables" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_tables', value: 'view', },
        { label: 'managed_database_tables', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_optimized" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="temporal_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Database table properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName" /> | Get managed database table |
| <CopyableCode code="list_by_schema" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId" /> | List managed database tables |

## `SELECT` examples

List managed database tables

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_tables', value: 'view', },
        { label: 'managed_database_tables', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
managedInstanceName,
memory_optimized,
resourceGroupName,
schemaName,
subscriptionId,
tableName,
temporal_type
FROM azure.sql.vw_managed_database_tables
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_database_tables
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

