---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.snapshots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Snapshot properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName" /> | Get details of the specified snapshot |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | List all snapshots associated with the volume |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__location" /> | Create the specified snapshot within the given volume |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName" /> | Delete snapshot |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName" /> | Patch a snapshot |
| <CopyableCode code="restore_files" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__filePaths" /> | Restore the specified files from the specified snapshot to the active filesystem |

## `SELECT` examples

List all snapshots associated with the volume

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
created,
location,
poolName,
provisioning_state,
resourceGroupName,
snapshotName,
snapshot_id,
subscriptionId,
volumeName
FROM azure_isv.netapp.vw_snapshots
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
location,
properties
FROM azure_isv.netapp.snapshots
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshots</code> resource.

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
INSERT INTO azure_isv.netapp.snapshots (
accountName,
poolName,
resourceGroupName,
snapshotName,
subscriptionId,
volumeName,
data__location,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ snapshotName }}',
'{{ subscriptionId }}',
'{{ volumeName }}',
'{{ data__location }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: properties
      value:
        - name: snapshotId
          value: string
        - name: created
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>snapshots</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.snapshots
SET 

WHERE 
accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```

## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.snapshots
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
