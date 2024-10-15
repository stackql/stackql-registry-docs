---
title: user_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_sessions
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

Creates, updates, deletes, gets or lists a <code>user_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.user_sessions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_sessions', value: 'view', },
        { label: 'user_sessions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="active_directory_user_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sessionHostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="userSessionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_principal_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for UserSession properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Get a userSession. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | List userSessions. |
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List userSessions. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Remove a userSession. |
| <CopyableCode code="disconnect" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Disconnect a userSession. |
| <CopyableCode code="send_message" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Send a message to a user. |

## `SELECT` examples

List userSessions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_sessions', value: 'view', },
        { label: 'user_sessions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
active_directory_user_name,
application_type,
create_time,
hostPoolName,
object_id,
resourceGroupName,
sessionHostName,
session_state,
subscriptionId,
system_data,
type,
userSessionId,
user_principal_name
FROM azure.desktop_virtualization.vw_user_sessions
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
FROM azure.desktop_virtualization.user_sessions
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>user_sessions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.user_sessions
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sessionHostName = '{{ sessionHostName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userSessionId = '{{ userSessionId }}';
```
