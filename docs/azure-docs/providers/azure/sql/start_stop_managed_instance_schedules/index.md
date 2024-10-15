---
title: start_stop_managed_instance_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - start_stop_managed_instance_schedules
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

Creates, updates, deletes, gets or lists a <code>start_stop_managed_instance_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>start_stop_managed_instance_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.start_stop_managed_instance_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_start_stop_managed_instance_schedules', value: 'view', },
        { label: 'start_stop_managed_instance_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_execution_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_run_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="startStopScheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of managed instance's Start/Stop schedule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId" /> | Gets the managed instance's Start/Stop schedule. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId" /> | Creates or updates the managed instance's Start/Stop schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId" /> | Deletes the managed instance's Start/Stop schedule. |

## `SELECT` examples

Gets the managed instance's Start/Stop schedule.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_start_stop_managed_instance_schedules', value: 'view', },
        { label: 'start_stop_managed_instance_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
managedInstanceName,
next_execution_time,
next_run_action,
resourceGroupName,
schedule_list,
startStopScheduleName,
subscriptionId,
system_data,
time_zone_id
FROM azure.sql.vw_start_stop_managed_instance_schedules
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND startStopScheduleName = '{{ startStopScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.sql.start_stop_managed_instance_schedules
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND startStopScheduleName = '{{ startStopScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>start_stop_managed_instance_schedules</code> resource.

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
INSERT INTO azure.sql.start_stop_managed_instance_schedules (
managedInstanceName,
resourceGroupName,
startStopScheduleName,
subscriptionId,
properties
)
SELECT 
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ startStopScheduleName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: description
          value: string
        - name: timeZoneId
          value: string
        - name: scheduleList
          value:
            - - name: startDay
                value: string
              - name: startTime
                value: string
              - name: stopDay
                value: string
              - name: stopTime
                value: string
        - name: nextRunAction
          value: string
        - name: nextExecutionTime
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>start_stop_managed_instance_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.start_stop_managed_instance_schedules
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND startStopScheduleName = '{{ startStopScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
