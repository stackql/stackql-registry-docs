---
title: sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - sensitivity_labels
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

Creates, updates, deletes, gets or lists a <code>sensitivity_labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sensitivity_labels', value: 'view', },
        { label: 'sensitivity_labels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="columnName" /> | `text` | field from the `properties` object |
| <CopyableCode code="column_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Resource that manages the sensitivity label. |
| <CopyableCode code="properties" /> | `object` | Properties of a sensitivity label. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, databaseName, resourceGroupName, schemaName, sensitivityLabelSource, serverName, subscriptionId, tableName" /> | Gets the sensitivity label of a given column |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="columnName, databaseName, resourceGroupName, schemaName, sensitivityLabelSource, serverName, subscriptionId, tableName" /> | Creates or updates the sensitivity label of a given column |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="columnName, databaseName, resourceGroupName, schemaName, sensitivityLabelSource, serverName, subscriptionId, tableName" /> | Deletes the sensitivity label of a given column |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Update sensitivity labels of a given database using an operations batch. |
| <CopyableCode code="disable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, databaseName, resourceGroupName, schemaName, sensitivityLabelSource, serverName, subscriptionId, tableName" /> | Disables sensitivity recommendations on a given column |
| <CopyableCode code="enable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, databaseName, resourceGroupName, schemaName, sensitivityLabelSource, serverName, subscriptionId, tableName" /> | Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns) |

## `SELECT` examples

Gets the sensitivity label of a given column

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sensitivity_labels', value: 'view', },
        { label: 'sensitivity_labels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
columnName,
column_name,
databaseName,
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
serverName,
subscriptionId,
tableName,
table_name
FROM azure.sql.vw_sensitivity_labels
WHERE columnName = '{{ columnName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sensitivityLabelSource = '{{ sensitivityLabelSource }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
managedBy,
properties
FROM azure.sql.sensitivity_labels
WHERE columnName = '{{ columnName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sensitivityLabelSource = '{{ sensitivityLabelSource }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sensitivity_labels</code> resource.

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
INSERT INTO azure.sql.sensitivity_labels (
columnName,
databaseName,
resourceGroupName,
schemaName,
sensitivityLabelSource,
serverName,
subscriptionId,
tableName,
properties
)
SELECT 
'{{ columnName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ schemaName }}',
'{{ sensitivityLabelSource }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ tableName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: managedBy
      value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sensitivity_labels</code> resource.

```sql
/*+ update */
UPDATE azure.sql.sensitivity_labels
SET 
operations = '{{ operations }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sensitivity_labels</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.sensitivity_labels
WHERE columnName = '{{ columnName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND sensitivityLabelSource = '{{ sensitivityLabelSource }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}';
```
