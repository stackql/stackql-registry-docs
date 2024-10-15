---
title: storage_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_classes
  - k8s_runtime
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

Creates, updates, deletes, gets or lists a <code>storage_classes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.k8s_runtime.storage_classes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_classes', value: 'view', },
        { label: 'storage_classes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_modes" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_volume_expansion" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_resilience" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_speed" /> | `text` | field from the `properties` object |
| <CopyableCode code="limitations" /> | `text` | field from the `properties` object |
| <CopyableCode code="mount_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="performance" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioner" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageClassName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_binding_mode" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Details of the StorageClass StorageClass. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri, storageClassName" /> | Get a StorageClassResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List StorageClassResource resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, storageClassName" /> | Create a StorageClassResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri, storageClassName" /> | Delete a StorageClassResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceUri, storageClassName" /> | Update a StorageClassResource |

## `SELECT` examples

List StorageClassResource resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_classes', value: 'view', },
        { label: 'storage_classes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_modes,
allow_volume_expansion,
data_resilience,
failover_speed,
limitations,
mount_options,
performance,
priority,
provisioner,
provisioning_state,
resourceUri,
storageClassName,
type_properties,
volume_binding_mode
FROM azure.k8s_runtime.vw_storage_classes
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.k8s_runtime.storage_classes
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_classes</code> resource.

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
INSERT INTO azure.k8s_runtime.storage_classes (
resourceUri,
storageClassName,
properties
)
SELECT 
'{{ resourceUri }}',
'{{ storageClassName }}',
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
        - name: allowVolumeExpansion
          value: []
        - name: mountOptions
          value:
            - string
        - name: provisioner
          value: string
        - name: volumeBindingMode
          value: []
        - name: accessModes
          value:
            - []
        - name: dataResilience
          value: []
        - name: failoverSpeed
          value: []
        - name: limitations
          value:
            - string
        - name: performance
          value: []
        - name: priority
          value: integer
        - name: typeProperties
          value:
            - name: type
              value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>storage_classes</code> resource.

```sql
/*+ update */
UPDATE azure.k8s_runtime.storage_classes
SET 
properties = '{{ properties }}'
WHERE 
resourceUri = '{{ resourceUri }}'
AND storageClassName = '{{ storageClassName }}';
```

## `DELETE` example

Deletes the specified <code>storage_classes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.k8s_runtime.storage_classes
WHERE resourceUri = '{{ resourceUri }}'
AND storageClassName = '{{ storageClassName }}';
```
