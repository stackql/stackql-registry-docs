---
title: database_automatic_tunings
hide_title: false
hide_table_of_contents: false
keywords:
  - database_automatic_tunings
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

Creates, updates, deletes, gets or lists a <code>database_automatic_tunings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_automatic_tunings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_automatic_tunings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_automatic_tunings', value: 'view', },
        { label: 'database_automatic_tunings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actual_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="desired_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="options" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Database-level Automatic Tuning properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's automatic tuning. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Update automatic tuning properties for target database. |

## `SELECT` examples

Gets a database's automatic tuning.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_automatic_tunings', value: 'view', },
        { label: 'database_automatic_tunings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actual_state,
databaseName,
desired_state,
options,
resourceGroupName,
serverName,
subscriptionId
FROM azure.sql.vw_database_automatic_tunings
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
FROM azure.sql.database_automatic_tunings
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>database_automatic_tunings</code> resource.

```sql
/*+ update */
UPDATE azure.sql.database_automatic_tunings
SET 
properties = '{{ properties }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
