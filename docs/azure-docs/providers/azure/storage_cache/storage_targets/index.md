---
title: storage_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_targets
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>storage_targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.storage_targets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_targets', value: 'view', },
        { label: 'storage_targets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID of the Storage Target. |
| <CopyableCode code="name" /> | `text` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete resource id of the object. These names are case-preserving, but not case sensitive. |
| <CopyableCode code="allocation_percentage" /> | `text` | field from the `properties` object |
| <CopyableCode code="blob_nfs" /> | `text` | field from the `properties` object |
| <CopyableCode code="cacheName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clfs" /> | `text` | field from the `properties` object |
| <CopyableCode code="junctions" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Region name string. |
| <CopyableCode code="nfs3" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageTargetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget |
| <CopyableCode code="unknown" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID of the Storage Target. |
| <CopyableCode code="name" /> | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete resource id of the object. These names are case-preserving, but not case sensitive. |
| <CopyableCode code="location" /> | `string` | Region name string. |
| <CopyableCode code="properties" /> | `object` | Properties of the Storage Target. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Returns a Storage Target from a cache. |
| <CopyableCode code="list_by_cache" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Returns a list of Storage Targets for the specified cache. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Create or update a Storage Target. This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the cache is healthy again. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Removes a Storage Target from a cache. This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the cache is healthy again. Note that if the cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted. |
| <CopyableCode code="dns_refresh" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Tells a storage target to refresh its DNS information. |
| <CopyableCode code="flush" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Tells the cache to write all dirty data to the Storage Target's backend storage. Client requests to this storage target's namespace will return errors until the flush operation completes. |
| <CopyableCode code="invalidate" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Invalidate all cached data for a storage target. Cached files are discarded and fetched from the back end on the next request. |
| <CopyableCode code="restore_defaults" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Tells a storage target to restore its settings to their default values. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Resumes client access to a previously suspended storage target. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Suspends client access to a storage target. |

## `SELECT` examples

Returns a list of Storage Targets for the specified cache.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_targets', value: 'view', },
        { label: 'storage_targets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allocation_percentage,
blob_nfs,
cacheName,
clfs,
junctions,
location,
nfs3,
provisioning_state,
resourceGroupName,
state,
storageTargetName,
subscriptionId,
system_data,
target_type,
type,
unknown
FROM azure.storage_cache.vw_storage_targets
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.storage_cache.storage_targets
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_targets</code> resource.

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
INSERT INTO azure.storage_cache.storage_targets (
cacheName,
resourceGroupName,
storageTargetName,
subscriptionId,
properties
)
SELECT 
'{{ cacheName }}',
'{{ resourceGroupName }}',
'{{ storageTargetName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: []
    - name: id
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: junctions
          value:
            - - name: namespacePath
                value: string
              - name: targetPath
                value: string
              - name: nfsExport
                value: string
              - name: nfsAccessPolicy
                value: string
        - name: targetType
          value: string
        - name: provisioningState
          value: string
        - name: state
          value: string
        - name: nfs3
          value:
            - name: target
              value: string
            - name: usageModel
              value: string
            - name: verificationTimer
              value: integer
            - name: writeBackTimer
              value: integer
        - name: clfs
          value:
            - name: target
              value: []
        - name: unknown
          value:
            - name: attributes
              value: []
        - name: blobNfs
          value:
            - name: usageModel
              value: string
            - name: verificationTimer
              value: integer
            - name: writeBackTimer
              value: integer
        - name: allocationPercentage
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storage_targets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_cache.storage_targets
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageTargetName = '{{ storageTargetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
