---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="incoming_traffic_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_operation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_workflow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSyncServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_sync_service_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_sync_service_uid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="use_identity" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Storage Sync Service Properties object. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Get a given StorageSyncService. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a StorageSyncService list by Resource group name. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a StorageSyncService list by subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, data__location" /> | Create a new StorageSyncService. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Delete a given StorageSyncService. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Patch a given StorageSyncService. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="locationName, subscriptionId, data__name, data__type" /> | Check the give namespace name availability. |

## `SELECT` examples

Get a StorageSyncService list by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
identity,
incoming_traffic_policy,
last_operation_name,
last_workflow_id,
location,
private_endpoint_connections,
provisioning_state,
resourceGroupName,
storageSyncServiceName,
storage_sync_service_status,
storage_sync_service_uid,
subscriptionId,
tags,
use_identity
FROM azure.storage_sync.vw_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.storage_sync.services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO azure.storage_sync.services (
resourceGroupName,
storageSyncServiceName,
subscriptionId,
data__location,
identity,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ storageSyncServiceName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ identity }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: incomingTrafficPolicy
          value: []
        - name: useIdentity
          value: boolean
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.storage_sync.services
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_sync.services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
