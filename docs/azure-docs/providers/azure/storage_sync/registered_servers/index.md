---
title: registered_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_servers
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

Creates, updates, deletes, gets or lists a <code>registered_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.registered_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registered_servers', value: 'view', },
        { label: 'registered_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="active_auth_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_version_expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_version_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_endpoint_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_heart_beat" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_operation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_workflow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_endpoint_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_endpoint_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverId" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_management_error_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_os_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSyncServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_sync_service_uid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | RegisteredServer Properties object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Get a given registered server. |
| <CopyableCode code="list_by_storage_sync_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Get a given registered server list. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Add a new registered server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Delete the given registered server. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Update registered server. |
| <CopyableCode code="trigger_rollover" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Triggers Server certificate rollover. |

## `SELECT` examples

Get a given registered server list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registered_servers', value: 'view', },
        { label: 'registered_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
active_auth_type,
agent_version,
agent_version_expiration_date,
agent_version_status,
application_id,
cluster_id,
cluster_name,
discovery_endpoint_uri,
friendly_name,
identity,
last_heart_beat,
last_operation_name,
last_workflow_id,
latest_application_id,
management_endpoint_uri,
monitoring_configuration,
monitoring_endpoint_uri,
provisioning_state,
resourceGroupName,
resource_location,
serverId,
server_certificate,
server_id,
server_management_error_code,
server_name,
server_os_version,
server_role,
service_location,
storageSyncServiceName,
storage_sync_service_uid,
subscriptionId
FROM azure.storage_sync.vw_registered_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.storage_sync.registered_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registered_servers</code> resource.

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
INSERT INTO azure.storage_sync.registered_servers (
resourceGroupName,
serverId,
storageSyncServiceName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverId }}',
'{{ storageSyncServiceName }}',
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
        - name: serverCertificate
          value: string
        - name: agentVersion
          value: string
        - name: serverOSVersion
          value: string
        - name: lastHeartBeat
          value: string
        - name: serverRole
          value: string
        - name: clusterId
          value: string
        - name: clusterName
          value: string
        - name: serverId
          value: string
        - name: friendlyName
          value: string
        - name: applicationId
          value: string
        - name: identity
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>registered_servers</code> resource.

```sql
/*+ update */
UPDATE azure.storage_sync.registered_servers
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serverId = '{{ serverId }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>registered_servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_sync.registered_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverId = '{{ serverId }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
