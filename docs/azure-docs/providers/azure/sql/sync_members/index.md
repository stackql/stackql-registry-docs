---
title: sync_members
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members
  - sql
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

Creates, updates, deletes, gets or lists a <code>sync_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_members" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sync_members', value: 'view', },
        { label: 'sync_members', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_server_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncMemberName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_agent_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_direction" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_member_azure_database_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_private_link_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a sync member. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Gets a sync member. |
| <CopyableCode code="list_by_sync_group" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Lists sync members in the given sync group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Creates or updates a sync member. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Deletes a sync member. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Updates an existing sync member. |
| <CopyableCode code="refresh_member_schema" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName" /> | Refreshes a sync member database schema. |

## `SELECT` examples

Lists sync members in the given sync group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sync_members', value: 'view', },
        { label: 'sync_members', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
database_name,
database_type,
password,
private_endpoint_name,
resourceGroupName,
serverName,
server_name,
sql_server_database_id,
subscriptionId,
syncGroupName,
syncMemberName,
sync_agent_id,
sync_direction,
sync_member_azure_database_resource_id,
sync_state,
use_private_link_connection,
user_name
FROM azure.sql.vw_sync_members
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.sync_members
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sync_members</code> resource.

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
INSERT INTO azure.sql.sync_members (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
syncGroupName,
syncMemberName,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ syncGroupName }}',
'{{ syncMemberName }}',
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
        - name: databaseType
          value: string
        - name: syncAgentId
          value: string
        - name: sqlServerDatabaseId
          value: string
        - name: syncMemberAzureDatabaseResourceId
          value: string
        - name: usePrivateLinkConnection
          value: boolean
        - name: privateEndpointName
          value: string
        - name: serverName
          value: string
        - name: databaseName
          value: string
        - name: userName
          value: string
        - name: password
          value: string
        - name: syncDirection
          value: string
        - name: syncState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sync_members</code> resource.

```sql
/*+ update */
UPDATE azure.sql.sync_members
SET 
properties = '{{ properties }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}'
AND syncMemberName = '{{ syncMemberName }}';
```

## `DELETE` example

Deletes the specified <code>sync_members</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.sync_members
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}'
AND syncMemberName = '{{ syncMemberName }}';
```
