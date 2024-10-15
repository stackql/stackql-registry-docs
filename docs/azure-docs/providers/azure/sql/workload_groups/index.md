---
title: workload_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_groups
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

Creates, updates, deletes, gets or lists a <code>workload_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workload_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.workload_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workload_groups', value: 'view', },
        { label: 'workload_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="importance" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_resource_percent" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_resource_percent_per_request" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_resource_percent" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_resource_percent_per_request" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_execution_timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workloadGroupName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Workload group definition. For more information look at sys.workload_management_workload_groups (DMV). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName" /> | Gets a workload group |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets the list of workload groups |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName" /> | Creates or updates a workload group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName" /> | Deletes a workload group. |

## `SELECT` examples

Gets the list of workload groups

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workload_groups', value: 'view', },
        { label: 'workload_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
importance,
max_resource_percent,
max_resource_percent_per_request,
min_resource_percent,
min_resource_percent_per_request,
query_execution_timeout,
resourceGroupName,
serverName,
subscriptionId,
workloadGroupName
FROM azure.sql.vw_workload_groups
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
FROM azure.sql.workload_groups
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workload_groups</code> resource.

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
INSERT INTO azure.sql.workload_groups (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
workloadGroupName,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
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
        - name: minResourcePercent
          value: integer
        - name: maxResourcePercent
          value: integer
        - name: minResourcePercentPerRequest
          value: number
        - name: maxResourcePercentPerRequest
          value: number
        - name: importance
          value: string
        - name: queryExecutionTimeout
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workload_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.workload_groups
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workloadGroupName = '{{ workloadGroupName }}';
```
