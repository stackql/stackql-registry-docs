---
title: server_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - server_endpoints
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

Creates, updates, deletes, gets or lists a <code>server_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.server_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_endpoints', value: 'view', },
        { label: 'server_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloud_tiering" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_tiering_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="initial_download_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="initial_upload_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_operation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_workflow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_cache_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_data_transfer" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_data_transfer_share_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_data_transfer_storage_account_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_data_transfer_storage_account_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recall_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_endpoint_provisioning_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_local_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSyncServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tier_files_older_than_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_free_space_percent" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | ServerEndpoint Properties object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a ServerEndpoint. |
| <CopyableCode code="list_by_sync_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a ServerEndpoint list. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Create a new ServerEndpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Delete a given ServerEndpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Patch a given ServerEndpoint. |
| <CopyableCode code="recall_action" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Recall a server endpoint. |

## `SELECT` examples

Get a ServerEndpoint list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_endpoints', value: 'view', },
        { label: 'server_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cloud_tiering,
cloud_tiering_status,
friendly_name,
initial_download_policy,
initial_upload_policy,
last_operation_name,
last_workflow_id,
local_cache_mode,
offline_data_transfer,
offline_data_transfer_share_name,
offline_data_transfer_storage_account_resource_id,
offline_data_transfer_storage_account_tenant_id,
provisioning_state,
recall_status,
resourceGroupName,
serverEndpointName,
server_endpoint_provisioning_status,
server_local_path,
server_name,
server_resource_id,
storageSyncServiceName,
subscriptionId,
syncGroupName,
sync_status,
tier_files_older_than_days,
volume_free_space_percent
FROM azure.storage_sync.vw_server_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.storage_sync.server_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_endpoints</code> resource.

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
INSERT INTO azure.storage_sync.server_endpoints (
resourceGroupName,
serverEndpointName,
storageSyncServiceName,
subscriptionId,
syncGroupName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverEndpointName }}',
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
      value:
        - name: serverLocalPath
          value: []
        - name: cloudTiering
          value: []
        - name: volumeFreeSpacePercent
          value: integer
        - name: tierFilesOlderThanDays
          value: integer
        - name: friendlyName
          value: string
        - name: serverResourceId
          value: []
        - name: offlineDataTransferShareName
          value: string
        - name: initialDownloadPolicy
          value: []
        - name: localCacheMode
          value: []
        - name: initialUploadPolicy
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>server_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.storage_sync.server_endpoints
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serverEndpointName = '{{ serverEndpointName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```

## `DELETE` example

Deletes the specified <code>server_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_sync.server_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverEndpointName = '{{ serverEndpointName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
