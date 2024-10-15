---
title: sql_pool_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_sensitivity_labels
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

Creates, updates, deletes, gets or lists a <code>sql_pool_sensitivity_labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_sensitivity_labels', value: 'view', },
        { label: 'sql_pool_sensitivity_labels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="columnName" /> | `text` | field from the `properties` object |
| <CopyableCode code="column_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="information_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="information_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_disabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="label_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="label_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="rank" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sensitivityLabelSource" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | managed by |
| <CopyableCode code="properties" /> | `object` | Properties of a sensitivity label. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Gets the sensitivity label of a given column |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Creates or updates the sensitivity label of a given column in a Sql pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Deletes the sensitivity label of a given column in a Sql pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Update sensitivity labels of a given SQL Pool using an operations batch. |
| <CopyableCode code="disable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Disables sensitivity recommendations on a given column |
| <CopyableCode code="enable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns) |

## `SELECT` examples

Gets the sensitivity label of a given column

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_sensitivity_labels', value: 'view', },
        { label: 'sql_pool_sensitivity_labels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
columnName,
column_name,
information_type,
information_type_id,
is_disabled,
label_id,
label_name,
managed_by,
rank,
resourceGroupName,
schemaName,
schema_name,
sensitivityLabelSource,
sqlPoolName,
subscriptionId,
tableName,
table_name,
workspaceName
FROM azure.synapse.vw_sql_pool_sensitivity_labels
WHERE columnName = '{{ columnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sensitivityLabelSource = '{{ sensitivityLabelSource }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
managedBy,
properties
FROM azure.synapse.sql_pool_sensitivity_labels
WHERE columnName = '{{ columnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sensitivityLabelSource = '{{ sensitivityLabelSource }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_sensitivity_labels</code> resource.

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
INSERT INTO azure.synapse.sql_pool_sensitivity_labels (
columnName,
resourceGroupName,
schemaName,
sensitivityLabelSource,
sqlPoolName,
subscriptionId,
tableName,
workspaceName,
properties
)
SELECT 
'{{ columnName }}',
'{{ resourceGroupName }}',
'{{ schemaName }}',
'{{ sensitivityLabelSource }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ tableName }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: schemaName
          value: string
        - name: tableName
          value: string
        - name: columnName
          value: string
        - name: labelName
          value: string
        - name: labelId
          value: string
        - name: informationType
          value: string
        - name: informationTypeId
          value: string
        - name: isDisabled
          value: boolean
        - name: rank
          value: string
    - name: managedBy
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_pool_sensitivity_labels</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.sql_pool_sensitivity_labels
SET 
operations = '{{ operations }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>sql_pool_sensitivity_labels</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.sql_pool_sensitivity_labels
WHERE columnName = '{{ columnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sensitivityLabelSource = '{{ sensitivityLabelSource }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```
