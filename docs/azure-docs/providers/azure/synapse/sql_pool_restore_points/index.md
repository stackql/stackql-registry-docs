---
title: sql_pool_restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_restore_points
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

Creates, updates, deletes, gets or lists a <code>sql_pool_restore_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_restore_points" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_restore_points', value: 'view', },
        { label: 'sql_pool_restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorePointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointName, sqlPoolName, subscriptionId, workspaceName" /> | Gets a restore point. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get SQL pool backup information |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__restorePointLabel" /> | Creates a restore point for a data warehouse. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, restorePointName, sqlPoolName, subscriptionId, workspaceName" /> | Deletes a restore point. |

## `SELECT` examples

Get SQL pool backup information

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_restore_points', value: 'view', },
        { label: 'sql_pool_restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
earliest_restore_date,
location,
resourceGroupName,
restorePointName,
restore_point_creation_date,
restore_point_label,
restore_point_type,
sqlPoolName,
subscriptionId,
workspaceName
FROM azure.synapse.vw_sql_pool_restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure.synapse.sql_pool_restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_restore_points</code> resource.

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
INSERT INTO azure.synapse.sql_pool_restore_points (
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
data__restorePointLabel,
restorePointLabel
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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

Deletes the specified <code>sql_pool_restore_points</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.sql_pool_restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointName = '{{ restorePointName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
