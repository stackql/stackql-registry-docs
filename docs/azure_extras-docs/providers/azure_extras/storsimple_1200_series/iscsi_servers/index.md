---
title: iscsi_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_servers
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

Creates, updates, deletes, gets or lists a <code>iscsi_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iscsi_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.iscsi_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iscsi_servers', value: 'view', },
        { label: 'iscsi_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_schedule_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="chap_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="iscsiServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="reverse_chap_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_domain_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The iSCSI server properties. |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified iSCSI server name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the iSCSI in a device. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the iSCSI servers in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the iSCSI server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Deletes the iSCSI server. |
| <CopyableCode code="backup_now" /> | `EXEC` | <CopyableCode code="deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId" /> | Backup the iSCSI server now. |

## `SELECT` examples

Retrieves all the iSCSI servers in a manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iscsi_servers', value: 'view', },
        { label: 'iscsi_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
backup_schedule_group_id,
chap_id,
deviceName,
iscsiServerName,
managerName,
resourceGroupName,
reverse_chap_id,
storage_domain_id,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_iscsi_servers
WHERE managerName = '{{ managerName }}'
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
FROM azure_extras.storsimple_1200_series.iscsi_servers
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iscsi_servers</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.iscsi_servers (
deviceName,
iscsiServerName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
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
        - name: storageDomainId
          value: string
        - name: backupScheduleGroupId
          value: string
        - name: description
          value: string
        - name: chapId
          value: string
        - name: reverseChapId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>iscsi_servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.iscsi_servers
WHERE deviceName = '{{ deviceName }}'
AND iscsiServerName = '{{ iscsiServerName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
