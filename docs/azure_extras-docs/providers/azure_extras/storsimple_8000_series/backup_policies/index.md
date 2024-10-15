---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
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

Creates, updates, deletes, gets or lists a <code>backup_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.backup_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_policies', value: 'view', },
        { label: 'backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="backupPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy_creation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="last_backup_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_backup_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_backup_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedules_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssm_host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="volume_ids" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the backup policy. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified backup policy name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the backup policies in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the backup policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the backup policy. |
| <CopyableCode code="backup_now" /> | `EXEC` | <CopyableCode code="backupPolicyName, backupType, deviceName, managerName, resourceGroupName, subscriptionId" /> | Backup the backup policy now. |

## `SELECT` examples

Gets all the backup policies in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_policies', value: 'view', },
        { label: 'backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backupPolicyName,
backup_policy_creation_type,
deviceName,
kind,
last_backup_time,
managerName,
next_backup_time,
resourceGroupName,
scheduled_backup_status,
schedules_count,
ssm_host_name,
subscriptionId,
type,
volume_ids
FROM azure_extras.storsimple_8000_series.vw_backup_policies
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
kind,
properties,
type
FROM azure_extras.storsimple_8000_series.backup_policies
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_policies</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.backup_policies (
backupPolicyName,
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
        - name: volumeIds
          value:
            - string
        - name: nextBackupTime
          value: string
        - name: lastBackupTime
          value: string
        - name: schedulesCount
          value: integer
        - name: scheduledBackupStatus
          value: string
        - name: backupPolicyCreationType
          value: string
        - name: ssmHostName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backup_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.backup_policies
WHERE backupPolicyName = '{{ backupPolicyName }}'
AND deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
