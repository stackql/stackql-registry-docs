---
title: tasks_resource_group_level_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks_resource_group_level_tasks
  - security
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

Creates, updates, deletes, gets or lists a <code>tasks_resource_group_level_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks_resource_group_level_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.tasks_resource_group_level_tasks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tasks_resource_group_level_tasks', value: 'view', },
        { label: 'tasks_resource_group_level_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="ascLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_state_change_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_task_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="sub_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="taskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of a task. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ascLocation, resourceGroupName, subscriptionId, taskName" /> | Recommended tasks that will help improve the security of the subscription proactively |

## `SELECT` examples

Recommended tasks that will help improve the security of the subscription proactively

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tasks_resource_group_level_tasks', value: 'view', },
        { label: 'tasks_resource_group_level_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ascLocation,
creation_time_utc,
last_state_change_time_utc,
resourceGroupName,
security_task_parameters,
state,
sub_state,
subscriptionId,
taskName,
type
FROM azure.security.vw_tasks_resource_group_level_tasks
WHERE ascLocation = '{{ ascLocation }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.tasks_resource_group_level_tasks
WHERE ascLocation = '{{ ascLocation }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```
</TabItem></Tabs>

