---
title: subvolumes
hide_title: false
hide_table_of_contents: false
keywords:
  - subvolumes
  - netapp
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

Creates, updates, deletes, gets or lists a <code>subvolumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subvolumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.subvolumes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subvolumes', value: 'view', },
        { label: 'subvolumes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subvolumeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | This represents path associated with the subvolume |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Returns the path associated with the subvolumeName provided |
| <CopyableCode code="list_by_volume" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Returns a list of the subvolumes in the volume |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Creates a subvolume in the path or clones the subvolume mentioned in the parentPath |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Delete subvolume |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Patch a subvolume |

## `SELECT` examples

Returns a list of the subvolumes in the volume

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subvolumes', value: 'view', },
        { label: 'subvolumes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
parent_path,
path,
poolName,
provisioning_state,
resourceGroupName,
size,
subscriptionId,
subvolumeName,
volumeName
FROM azure_isv.netapp.vw_subvolumes
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.netapp.subvolumes
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subvolumes</code> resource.

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
INSERT INTO azure_isv.netapp.subvolumes (
accountName,
poolName,
resourceGroupName,
subscriptionId,
subvolumeName,
volumeName,
properties
)
SELECT 
'{{ accountName }}',
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ subvolumeName }}',
'{{ volumeName }}',
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
        - name: path
          value: string
        - name: size
          value: integer
        - name: parentPath
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>subvolumes</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.subvolumes
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND subvolumeName = '{{ subvolumeName }}'
AND volumeName = '{{ volumeName }}';
```

## `DELETE` example

Deletes the specified <code>subvolumes</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.subvolumes
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND subvolumeName = '{{ subvolumeName }}'
AND volumeName = '{{ volumeName }}';
```
