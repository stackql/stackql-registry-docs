---
title: iscsi_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_disks
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

Creates, updates, deletes, gets or lists a <code>iscsi_disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iscsi_disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.iscsi_disks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iscsi_disks', value: 'view', },
        { label: 'iscsi_disks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_control_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="iscsiServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_used_capacity_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_capacity_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
| <CopyableCode code="used_capacity_in_bytes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The iSCSI disk properties. |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified iSCSI disk name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the iSCSI disks in a device. |
| <CopyableCode code="list_by_iscsi_server" /> | `SELECT` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the disks in a iSCSI server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the iSCSI disk. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Deletes the iSCSI disk. |

## `SELECT` examples

Retrieves all the iSCSI disks in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iscsi_disks', value: 'view', },
        { label: 'iscsi_disks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
access_control_records,
data_policy,
deviceName,
diskName,
disk_status,
iscsiServerName,
local_used_capacity_in_bytes,
managerName,
monitoring_status,
provisioned_capacity_in_bytes,
resourceGroupName,
subscriptionId,
type,
used_capacity_in_bytes
FROM azure_extras.storsimple_1200_series.vw_iscsi_disks
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
FROM azure_extras.storsimple_1200_series.iscsi_disks
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iscsi_disks</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.iscsi_disks (
deviceName,
diskName,
iscsiServerName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
'{{ diskName }}',
'{{ iscsiServerName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
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
        - name: description
          value: string
        - name: diskStatus
          value: string
        - name: accessControlRecords
          value:
            - string
        - name: dataPolicy
          value: string
        - name: provisionedCapacityInBytes
          value: integer
        - name: usedCapacityInBytes
          value: integer
        - name: localUsedCapacityInBytes
          value: integer
        - name: monitoringStatus
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>iscsi_disks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.iscsi_disks
WHERE deviceName = '{{ deviceName }}'
AND diskName = '{{ diskName }}'
AND iscsiServerName = '{{ iscsiServerName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
