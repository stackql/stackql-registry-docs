---
title: replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_links
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

Creates, updates, deletes, gets or lists a <code>replication_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.replication_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_links', value: 'view', },
        { label: 'replication_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_termination_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkId" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_database" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a replication link. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Gets a replication link. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of replication links on database. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of replication links. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Updates the replication link type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Deletes the replication link. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Updates the replication link type. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. |
| <CopyableCode code="failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="databaseName, linkId, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server allowing data loss. |

## `SELECT` examples

Gets a list of replication links.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_links', value: 'view', },
        { label: 'replication_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
is_termination_allowed,
linkId,
link_type,
partner_database,
partner_database_id,
partner_location,
partner_role,
partner_server,
percent_complete,
replication_mode,
replication_state,
resourceGroupName,
role,
serverName,
start_time,
subscriptionId
FROM azure.sql.vw_replication_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.replication_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_links</code> resource.

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
INSERT INTO azure.sql.replication_links (
databaseName,
linkId,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ databaseName }}',
'{{ linkId }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
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
        - name: partnerServer
          value: string
        - name: partnerDatabase
          value: string
        - name: partnerDatabaseId
          value: string
        - name: partnerLocation
          value: string
        - name: role
          value: string
        - name: partnerRole
          value: string
        - name: replicationMode
          value: string
        - name: startTime
          value: string
        - name: percentComplete
          value: integer
        - name: replicationState
          value: string
        - name: isTerminationAllowed
          value: boolean
        - name: linkType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_links</code> resource.

```sql
/*+ update */
UPDATE azure.sql.replication_links
SET 
properties = '{{ properties }}'
WHERE 
databaseName = '{{ databaseName }}'
AND linkId = '{{ linkId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.replication_links
WHERE databaseName = '{{ databaseName }}'
AND linkId = '{{ linkId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
