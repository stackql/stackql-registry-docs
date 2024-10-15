---
title: sync_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_agents
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

Creates, updates, deletes, gets or lists a <code>sync_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_agents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sync_agents', value: 'view', },
        { label: 'sync_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_up_to_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_alive_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an Azure SQL Database sync agent. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, syncAgentName" /> | Gets a sync agent. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists sync agents in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, syncAgentName" /> | Creates or updates a sync agent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, syncAgentName" /> | Deletes a sync agent. |
| <CopyableCode code="generate_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, syncAgentName" /> | Generates a sync agent key. |

## `SELECT` examples

Lists sync agents in a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sync_agents', value: 'view', },
        { label: 'sync_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
expiry_time,
is_up_to_date,
last_alive_time,
resourceGroupName,
serverName,
state,
subscriptionId,
syncAgentName,
sync_database_id,
version
FROM azure.sql.vw_sync_agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.sync_agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sync_agents</code> resource.

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
INSERT INTO azure.sql.sync_agents (
resourceGroupName,
serverName,
subscriptionId,
syncAgentName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ syncAgentName }}',
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
        - name: name
          value: string
        - name: syncDatabaseId
          value: string
        - name: lastAliveTime
          value: string
        - name: state
          value: string
        - name: isUpToDate
          value: boolean
        - name: expiryTime
          value: string
        - name: version
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sync_agents</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.sync_agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncAgentName = '{{ syncAgentName }}';
```
