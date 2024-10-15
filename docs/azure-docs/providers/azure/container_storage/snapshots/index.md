---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - container_storage
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_storage.snapshots" /></td></tr>
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
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Volume Snapshot Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, snapshotName, subscriptionId" /> | Get a Snapshot |
| <CopyableCode code="list_by_pool" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | List Snapshot resources by Pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, resourceGroupName, snapshotName, subscriptionId" /> | Create a Snapshot |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, resourceGroupName, snapshotName, subscriptionId" /> | Delete a Snapshot |

## `SELECT` examples

List Snapshot resources by Pool

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
poolName,
provisioning_state,
resourceGroupName,
snapshotName,
source,
status,
subscriptionId
FROM azure.container_storage.vw_snapshots
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_storage.snapshots
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.container_storage.snapshots (
poolName,
resourceGroupName,
snapshotName,
subscriptionId,
properties
)
SELECT 
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ snapshotName }}',
'{{ subscriptionId }}',
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
        - name: provisioningState
          value: []
        - name: status
          value:
            - name: state
              value: []
            - name: message
              value: string
        - name: source
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_storage.snapshots
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
