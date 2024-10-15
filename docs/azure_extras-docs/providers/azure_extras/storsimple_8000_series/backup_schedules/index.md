---
title: backup_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedules
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>backup_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.backup_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_schedules', value: 'view', },
        { label: 'backup_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="backupPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backupScheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="last_successful_run" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_recurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the backup schedule. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPolicyName, backupScheduleName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified backup schedule name. |
| <CopyableCode code="list_by_backup_policy" /> | `SELECT` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the backup schedules in a backup policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backupPolicyName, backupScheduleName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the backup schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPolicyName, backupScheduleName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the backup schedule. |

## `SELECT` examples

Gets all the backup schedules in a backup policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_schedules', value: 'view', },
        { label: 'backup_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backupPolicyName,
backupScheduleName,
backup_type,
deviceName,
kind,
last_successful_run,
managerName,
resourceGroupName,
retention_count,
schedule_recurrence,
schedule_status,
start_time,
subscriptionId,
type
FROM azure_extras.storsimple_8000_series.vw_backup_schedules
WHERE backupPolicyName = '{{ backupPolicyName }}'
AND deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure_extras.storsimple_8000_series.backup_schedules
WHERE backupPolicyName = '{{ backupPolicyName }}'
AND deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_schedules</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.backup_schedules (
backupPolicyName,
backupScheduleName,
deviceName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
kind,
properties
)
SELECT 
'{{ backupPolicyName }}',
'{{ backupScheduleName }}',
'{{ deviceName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: scheduleRecurrence
          value:
            - name: recurrenceType
              value: string
            - name: recurrenceValue
              value: integer
            - name: weeklyDaysList
              value:
                - string
        - name: backupType
          value: string
        - name: retentionCount
          value: integer
        - name: startTime
          value: string
        - name: scheduleStatus
          value: string
        - name: lastSuccessfulRun
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backup_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.backup_schedules
WHERE backupPolicyName = '{{ backupPolicyName }}'
AND backupScheduleName = '{{ backupScheduleName }}'
AND deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
