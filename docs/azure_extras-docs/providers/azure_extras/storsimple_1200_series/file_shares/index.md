---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
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

Creates, updates, deletes, gets or lists a <code>file_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.file_shares" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_shares', value: 'view', },
        { label: 'file_shares', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_used_capacity_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_capacity_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shareName" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
| <CopyableCode code="used_capacity_in_bytes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The File Share. |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId" /> | Returns the properties of the specified file share name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file shares in a device. |
| <CopyableCode code="list_by_file_server" /> | `SELECT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file shares in a file server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId, data__properties" /> | Creates or updates the file share. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId" /> | Deletes the file share. |

## `SELECT` examples

Retrieves all the file shares in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_shares', value: 'view', },
        { label: 'file_shares', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
admin_user,
data_policy,
deviceName,
fileServerName,
local_used_capacity_in_bytes,
managerName,
monitoring_status,
provisioned_capacity_in_bytes,
resourceGroupName,
shareName,
share_status,
subscriptionId,
type,
used_capacity_in_bytes
FROM azure_extras.storsimple_1200_series.vw_file_shares
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
FROM azure_extras.storsimple_1200_series.file_shares
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>file_shares</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.file_shares (
deviceName,
fileServerName,
managerName,
resourceGroupName,
shareName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
'{{ fileServerName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ shareName }}',
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
        - name: shareStatus
          value: string
        - name: dataPolicy
          value: string
        - name: adminUser
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

Deletes the specified <code>file_shares</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.file_shares
WHERE deviceName = '{{ deviceName }}'
AND fileServerName = '{{ fileServerName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
