---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volumes" /></td></tr>
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
| <CopyableCode code="creation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="elasticSanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="size_gib" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_target" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Volume response properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName" /> | Get an Volume. |
| <CopyableCode code="list_by_volume_group" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | List Volumes in a VolumeGroup. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName, data__properties" /> | Create a Volume. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName" /> | Delete an Volume. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName" /> | Update an Volume. |

## `SELECT` examples

List Volumes in a VolumeGroup.

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
creation_data,
elasticSanName,
managed_by,
provisioning_state,
resourceGroupName,
size_gib,
storage_target,
subscriptionId,
volumeGroupName,
volumeName,
volume_id
FROM azure.elastic_san.vw_volumes
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
FROM azure.elastic_san.volumes
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
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
INSERT INTO azure.elastic_san.volumes (
elasticSanName,
resourceGroupName,
subscriptionId,
volumeGroupName,
volumeName,
data__properties,
properties
)
SELECT 
'{{ elasticSanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeGroupName }}',
'{{ volumeName }}',
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
        - name: volumeId
          value: string
        - name: creationData
          value:
            - name: createSource
              value: string
            - name: sourceId
              value: string
        - name: sizeGiB
          value: integer
        - name: storageTarget
          value:
            - name: targetIqn
              value: string
            - name: targetPortalHostname
              value: string
            - name: targetPortalPort
              value: integer
            - name: provisioningState
              value: []
            - name: status
              value: []
        - name: managedBy
          value:
            - name: resourceId
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>volumes</code> resource.

```sql
/*+ update */
UPDATE azure.elastic_san.volumes
SET 
properties = '{{ properties }}'
WHERE 
elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}'
AND volumeName = '{{ volumeName }}';
```

## `DELETE` example

Deletes the specified <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.elastic_san.volumes
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}'
AND volumeName = '{{ volumeName }}';
```
