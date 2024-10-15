---
title: volume_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_containers
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

Creates, updates, deletes, gets or lists a <code>volume_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.volume_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_containers', value: 'view', },
        { label: 'volume_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="band_width_rate_in_mbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="bandwidth_setting_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner_ship_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_credential_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_cloud_storage_usage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="volumeContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of volume container. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName" /> | Gets the properties of the specified volume container name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the volume containers in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName, data__properties" /> | Creates or updates the volume container. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName" /> | Deletes the volume container. |

## `SELECT` examples

Gets all the volume containers in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_containers', value: 'view', },
        { label: 'volume_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
band_width_rate_in_mbps,
bandwidth_setting_id,
deviceName,
encryption_key,
encryption_status,
kind,
managerName,
owner_ship_status,
resourceGroupName,
storage_account_credential_id,
subscriptionId,
total_cloud_storage_usage_in_bytes,
type,
volumeContainerName,
volume_count
FROM azure_extras.storsimple_8000_series.vw_volume_containers
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
FROM azure_extras.storsimple_8000_series.volume_containers
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volume_containers</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.volume_containers (
deviceName,
managerName,
resourceGroupName,
subscriptionId,
volumeContainerName,
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
        - name: encryptionKey
          value:
            - name: value
              value: string
            - name: encryptionCertThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string
        - name: encryptionStatus
          value: string
        - name: volumeCount
          value: integer
        - name: storageAccountCredentialId
          value: string
        - name: ownerShipStatus
          value: string
        - name: bandWidthRateInMbps
          value: integer
        - name: bandwidthSettingId
          value: string
        - name: totalCloudStorageUsageInBytes
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volume_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.volume_containers
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeContainerName = '{{ volumeContainerName }}';
```
