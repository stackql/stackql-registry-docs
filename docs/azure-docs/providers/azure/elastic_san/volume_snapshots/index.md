---
title: volume_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_snapshots
  - elastic_san
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

Creates, updates, deletes, gets or lists a <code>volume_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volume_snapshots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_snapshots', value: 'view', },
        { label: 'volume_snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="elasticSanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_volume_size_gib" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties for Snapshot. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName" /> | Get a Volume Snapshot. |
| <CopyableCode code="list_by_volume_group" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName, data__properties" /> | Create a Volume Snapshot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName" /> | Delete a Volume Snapshot. |

## `SELECT` examples

List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_snapshots', value: 'view', },
        { label: 'volume_snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_data,
elasticSanName,
provisioning_state,
resourceGroupName,
snapshotName,
source_volume_size_gib,
subscriptionId,
volumeGroupName,
volume_name
FROM azure.elastic_san.vw_volume_snapshots
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.elastic_san.volume_snapshots
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volume_snapshots</code> resource.

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
INSERT INTO azure.elastic_san.volume_snapshots (
elasticSanName,
resourceGroupName,
snapshotName,
subscriptionId,
volumeGroupName,
data__properties,
properties
)
SELECT 
'{{ elasticSanName }}',
'{{ resourceGroupName }}',
'{{ snapshotName }}',
'{{ subscriptionId }}',
'{{ volumeGroupName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: creationData
          value:
            - name: sourceId
              value: string
        - name: provisioningState
          value: []
        - name: sourceVolumeSizeGiB
          value: integer
        - name: volumeName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volume_snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.elastic_san.volume_snapshots
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
```
