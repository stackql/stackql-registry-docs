---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
  - storage_sync
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

Creates, updates, deletes, gets or lists a <code>sync_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.sync_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sync_groups', value: 'view', },
        { label: 'sync_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSyncServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_group_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SyncGroup Properties object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a given SyncGroup. |
| <CopyableCode code="list_by_storage_sync_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Get a SyncGroup List. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Create a new SyncGroup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Delete a given SyncGroup. |

## `SELECT` examples

Get a SyncGroup List.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sync_groups', value: 'view', },
        { label: 'sync_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
resourceGroupName,
storageSyncServiceName,
subscriptionId,
syncGroupName,
sync_group_status,
unique_id
FROM azure.storage_sync.vw_sync_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.storage_sync.sync_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sync_groups</code> resource.

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
INSERT INTO azure.storage_sync.sync_groups (
resourceGroupName,
storageSyncServiceName,
subscriptionId,
syncGroupName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ storageSyncServiceName }}',
'{{ subscriptionId }}',
'{{ syncGroupName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sync_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_sync.sync_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
