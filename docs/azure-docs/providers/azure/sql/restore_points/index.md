---
title: restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_points
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

Creates, updates, deletes, gets or lists a <code>restore_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.restore_points" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restore_points', value: 'view', },
        { label: 'restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorePointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a database restore point |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, restorePointName, serverName, subscriptionId" /> | Gets a restore point. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of database restore points. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, data__restorePointLabel" /> | Creates a restore point for a data warehouse. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, restorePointName, serverName, subscriptionId" /> | Deletes a restore point. |

## `SELECT` examples

Gets a list of database restore points.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restore_points', value: 'view', },
        { label: 'restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
earliest_restore_date,
location,
resourceGroupName,
restorePointName,
restore_point_creation_date,
restore_point_label,
restore_point_type,
serverName,
subscriptionId
FROM azure.sql.vw_restore_points
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure.sql.restore_points
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>restore_points</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.sql.restore_points (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
data__restorePointLabel,
restorePointLabel
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__restorePointLabel }}',
'{{ restorePointLabel }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: restorePointLabel
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>restore_points</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.restore_points
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND restorePointName = '{{ restorePointName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
