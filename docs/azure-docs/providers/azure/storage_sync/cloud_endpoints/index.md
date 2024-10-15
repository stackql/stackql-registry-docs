---
title: cloud_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_endpoints
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

Creates, updates, deletes, gets or lists a <code>cloud_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.cloud_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_endpoints', value: 'view', },
        { label: 'cloud_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_file_share_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="change_enumeration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_operation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_workflow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partnership_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSyncServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncGroupName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | CloudEndpoint Properties object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a given CloudEndpoint. |
| <CopyableCode code="list_by_sync_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a CloudEndpoint List. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Create a new CloudEndpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Delete a given CloudEndpoint. |
| <CopyableCode code="afs_share_metadata_certificate_public_keys" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get the AFS file share metadata signing certificate public keys. |
| <CopyableCode code="post_backup" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Post Backup a given CloudEndpoint. |
| <CopyableCode code="post_restore" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Post Restore a given CloudEndpoint. |
| <CopyableCode code="pre_backup" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Pre Backup a given CloudEndpoint. |
| <CopyableCode code="pre_restore" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Pre Restore a given CloudEndpoint. |
| <CopyableCode code="restoreheartbeat" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Restore Heartbeat a given CloudEndpoint. |
| <CopyableCode code="trigger_change_detection" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint. |

## `SELECT` examples

Get a CloudEndpoint List.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_endpoints', value: 'view', },
        { label: 'cloud_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_file_share_name,
backup_enabled,
change_enumeration_status,
cloudEndpointName,
friendly_name,
last_operation_name,
last_workflow_id,
partnership_id,
provisioning_state,
resourceGroupName,
storageSyncServiceName,
storage_account_resource_id,
storage_account_tenant_id,
subscriptionId,
syncGroupName
FROM azure.storage_sync.vw_cloud_endpoints
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
FROM azure.storage_sync.cloud_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_endpoints</code> resource.

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
INSERT INTO azure.storage_sync.cloud_endpoints (
cloudEndpointName,
resourceGroupName,
storageSyncServiceName,
subscriptionId,
syncGroupName,
properties
)
SELECT 
'{{ cloudEndpointName }}',
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
      value:
        - name: storageAccountResourceId
          value: string
        - name: azureFileShareName
          value: string
        - name: storageAccountTenantId
          value: string
        - name: friendlyName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cloud_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_sync.cloud_endpoints
WHERE cloudEndpointName = '{{ cloudEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
