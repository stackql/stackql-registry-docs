---
title: workload_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_classifiers
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

Creates, updates, deletes, gets or lists a <code>workload_classifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workload_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.workload_classifiers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workload_classifiers', value: 'view', },
        { label: 'workload_classifiers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="context" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="importance" /> | `text` | field from the `properties` object |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="member_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workloadClassifierName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workloadGroupName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Workload classifier definition. For more information look at sys.workload_management_workload_classifiers (DMV). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName" /> | Gets a workload classifier |
| <CopyableCode code="list_by_workload_group" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName" /> | Gets the list of workload classifiers for a workload group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName" /> | Creates or updates a workload classifier. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName" /> | Deletes a workload classifier. |

## `SELECT` examples

Gets the list of workload classifiers for a workload group

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workload_classifiers', value: 'view', },
        { label: 'workload_classifiers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
context,
databaseName,
end_time,
importance,
label,
member_name,
resourceGroupName,
serverName,
start_time,
subscriptionId,
workloadClassifierName,
workloadGroupName
FROM azure.sql.vw_workload_classifiers
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadGroupName = '{{ workloadGroupName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.workload_classifiers
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadGroupName = '{{ workloadGroupName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workload_classifiers</code> resource.

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
INSERT INTO azure.sql.workload_classifiers (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
workloadClassifierName,
workloadGroupName,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ workloadClassifierName }}',
'{{ workloadGroupName }}',
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

Deletes the specified <code>workload_classifiers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.workload_classifiers
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadClassifierName = '{{ workloadClassifierName }}'
AND workloadGroupName = '{{ workloadGroupName }}';
```
