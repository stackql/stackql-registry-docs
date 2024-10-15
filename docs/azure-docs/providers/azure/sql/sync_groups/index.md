---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
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

Creates, updates, deletes, gets or lists a <code>sync_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_groups" /></td></tr>
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
| <CopyableCode code="conflict_logging_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="conflict_resolution_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_conflict_logging" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_database_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_database_user_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="interval" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_sync_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="syncGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_private_link_connection" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a sync group. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Gets a sync group. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Lists sync groups under a hub database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Creates or updates a sync group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Deletes a sync group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Updates a sync group. |
| <CopyableCode code="cancel_sync" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Cancels a sync group synchronization. |
| <CopyableCode code="refresh_hub_schema" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Refreshes a hub database schema. |
| <CopyableCode code="trigger_sync" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Triggers a sync group synchronization. |

## `SELECT` examples

Lists sync groups under a hub database.

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
conflict_logging_retention_in_days,
conflict_resolution_policy,
databaseName,
enable_conflict_logging,
hub_database_password,
hub_database_user_name,
interval,
last_sync_time,
private_endpoint_name,
resourceGroupName,
schema,
serverName,
sku,
subscriptionId,
syncGroupName,
sync_database_id,
sync_state,
use_private_link_connection
FROM azure.sql.vw_sync_groups
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku
FROM azure.sql.sync_groups
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
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
INSERT INTO azure.sql.sync_groups (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
syncGroupName,
sku,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ syncGroupName }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: interval
          value: integer
        - name: lastSyncTime
          value: string
        - name: conflictResolutionPolicy
          value: string
        - name: syncDatabaseId
          value: string
        - name: hubDatabaseUserName
          value: string
        - name: hubDatabasePassword
          value: string
        - name: syncState
          value: string
        - name: schema
          value:
            - name: tables
              value:
                - - name: columns
                    value:
                      - - name: quotedName
                          value: string
                        - name: dataSize
                          value: string
                        - name: dataType
                          value: string
                  - name: quotedName
                    value: string
            - name: masterSyncMemberName
              value: string
        - name: enableConflictLogging
          value: boolean
        - name: conflictLoggingRetentionInDays
          value: integer
        - name: usePrivateLinkConnection
          value: boolean
        - name: privateEndpointName
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sync_groups</code> resource.

```sql
/*+ update */
UPDATE azure.sql.sync_groups
SET 
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```

## `DELETE` example

Deletes the specified <code>sync_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.sync_groups
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}';
```
