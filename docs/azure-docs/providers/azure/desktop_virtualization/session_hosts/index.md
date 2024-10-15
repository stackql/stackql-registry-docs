---
title: session_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - session_hosts
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>session_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.session_hosts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_hosts', value: 'view', },
        { label: 'session_hosts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_new_session" /> | `text` | field from the `properties` object |
| <CopyableCode code="assigned_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_heart_beat" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_session_host_update_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_update_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sessionHostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_host_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_host_health_check_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="sessions" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sx_s_stack_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="update_error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for SessionHost properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Get a session host. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List sessionHosts. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Remove a SessionHost. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Update a session host. |
| <CopyableCode code="retry_provisioning" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Retry provisioning on a SessionHost. |

## `SELECT` examples

List sessionHosts.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_hosts', value: 'view', },
        { label: 'session_hosts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agent_version,
allow_new_session,
assigned_user,
friendly_name,
hostPoolName,
last_heart_beat,
last_session_host_update_time,
last_update_time,
object_id,
os_version,
resourceGroupName,
resource_id,
sessionHostName,
session_host_configuration,
session_host_health_check_results,
sessions,
status,
status_timestamp,
subscriptionId,
sx_s_stack_version,
system_data,
type,
update_error_message,
update_state,
virtual_machine_id
FROM azure.desktop_virtualization.vw_session_hosts
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.desktop_virtualization.session_hosts
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>session_hosts</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.session_hosts
SET 
properties = '{{ properties }}'
WHERE 
hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sessionHostName = '{{ sessionHostName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>session_hosts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.session_hosts
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sessionHostName = '{{ sessionHostName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
