---
title: backup_schedule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedule_groups
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>backup_schedule_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_schedule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.backup_schedule_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_schedule_groups', value: 'view', },
        { label: 'backup_schedule_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The Backup Schedule Group Properties |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId" /> | Returns the properties of the specified backup schedule group name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backup schedule groups in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId, data__properties" /> | Creates or Updates the backup schedule Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId" /> | Deletes the backup schedule group. |

## `SELECT` examples

Retrieves all the backup schedule groups in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_schedule_groups', value: 'view', },
        { label: 'backup_schedule_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deviceName,
managerName,
resourceGroupName,
scheduleGroupName,
start_time,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_backup_schedule_groups
WHERE deviceName = '{{ deviceName }}'
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
properties,
type
FROM azure_extras.storsimple_1200_series.backup_schedule_groups
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_schedule_groups</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.backup_schedule_groups (
deviceName,
managerName,
resourceGroupName,
scheduleGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ scheduleGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: startTime
          value:
            - name: hour
              value: integer
            - name: minute
              value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backup_schedule_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.backup_schedule_groups
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleGroupName = '{{ scheduleGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
