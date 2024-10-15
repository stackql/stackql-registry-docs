---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.volumes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="access_control_record_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="size_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="volumeContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of volume. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName" /> | Returns the properties of the specified volume name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the volumes in a device. |
| <CopyableCode code="list_by_volume_container" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName" /> | Retrieves all the volumes in a volume container. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName, data__properties" /> | Creates or updates the volume. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, volumeName" /> | Deletes the volume. |

## `SELECT` examples

Retrieves all the volumes in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_control_record_ids,
backup_policy_ids,
backup_status,
deviceName,
kind,
managerName,
monitoring_status,
operation_status,
resourceGroupName,
size_in_bytes,
subscriptionId,
type,
volumeContainerName,
volumeName,
volume_container_id,
volume_status,
volume_type
FROM azure_extras.storsimple_8000_series.vw_volumes
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
FROM azure_extras.storsimple_8000_series.volumes
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.volumes (
deviceName,
managerName,
resourceGroupName,
subscriptionId,
volumeContainerName,
volumeName,
data__properties,
kind,
properties
)
SELECT 
'{{ deviceName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeContainerName }}',
'{{ volumeName }}',
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
        - name: sizeInBytes
          value: integer
        - name: volumeType
          value: string
        - name: volumeContainerId
          value: string
        - name: accessControlRecordIds
          value:
            - string
        - name: volumeStatus
          value: string
        - name: operationStatus
          value: string
        - name: backupStatus
          value: string
        - name: monitoringStatus
          value: string
        - name: backupPolicyIds
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.volumes
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeContainerName = '{{ volumeContainerName }}'
AND volumeName = '{{ volumeName }}';
```
