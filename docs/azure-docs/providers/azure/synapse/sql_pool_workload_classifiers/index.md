---
title: sql_pool_workload_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_workload_classifiers
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

Creates, updates, deletes, gets or lists a <code>sql_pool_workload_classifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_workload_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_workload_classifiers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_workload_classifiers', value: 'view', },
        { label: 'sql_pool_workload_classifiers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="context" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="importance" /> | `text` | field from the `properties` object |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="member_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workloadClassifierName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workloadGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Workload classifier definition. For more information look at sys.workload_management_workload_classifiers (DMV). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName" /> | Get a workload classifier of Sql pool's workload group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName" /> | Get list of  Sql pool's workload classifier for workload groups. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName" /> | Create Or Update workload classifier for a Sql pool's workload group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName" /> | Remove workload classifier of a Sql pool's workload group. |

## `SELECT` examples

Get list of  Sql pool's workload classifier for workload groups.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_workload_classifiers', value: 'view', },
        { label: 'sql_pool_workload_classifiers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
context,
end_time,
importance,
label,
member_name,
resourceGroupName,
sqlPoolName,
start_time,
subscriptionId,
workloadClassifierName,
workloadGroupName,
workspaceName
FROM azure.synapse.vw_sql_pool_workload_classifiers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadGroupName = '{{ workloadGroupName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.sql_pool_workload_classifiers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadGroupName = '{{ workloadGroupName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_workload_classifiers</code> resource.

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
INSERT INTO azure.synapse.sql_pool_workload_classifiers (
resourceGroupName,
sqlPoolName,
subscriptionId,
workloadClassifierName,
workloadGroupName,
workspaceName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workloadClassifierName }}',
'{{ workloadGroupName }}',
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
        - name: memberName
          value: string
        - name: label
          value: string
        - name: context
          value: string
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: importance
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sql_pool_workload_classifiers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.sql_pool_workload_classifiers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadClassifierName = '{{ workloadClassifierName }}'
AND workloadGroupName = '{{ workloadGroupName }}'
AND workspaceName = '{{ workspaceName }}';
```
