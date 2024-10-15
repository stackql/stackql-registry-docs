---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
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

Creates, updates, deletes, gets or lists a <code>failover_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.failover_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_failover_groups', value: 'view', },
        { label: 'failover_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databases" /> | `text` | field from the `properties` object |
| <CopyableCode code="failoverGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="partner_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_only_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_write_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a failover group. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Gets a failover group. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists the failover groups in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a failover group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Deletes a failover group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Updates a failover group. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. |
| <CopyableCode code="force_failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. This operation might result in data loss. |
| <CopyableCode code="try_planned_before_forced_failover" /> | `EXEC` | <CopyableCode code="failoverGroupName, resourceGroupName, serverName, subscriptionId" /> | Fails over from the current primary server to this server. This operation tries planned before forced failover but might still result in data loss. |

## `SELECT` examples

Lists the failover groups in a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_failover_groups', value: 'view', },
        { label: 'failover_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databases,
failoverGroupName,
location,
partner_servers,
read_only_endpoint,
read_write_endpoint,
replication_role,
replication_state,
resourceGroupName,
secondary_type,
serverName,
subscriptionId,
tags
FROM azure.sql.vw_failover_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.sql.failover_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>failover_groups</code> resource.

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
INSERT INTO azure.sql.failover_groups (
failoverGroupName,
resourceGroupName,
serverName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ failoverGroupName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: readWriteEndpoint
          value:
            - name: failoverPolicy
              value: string
            - name: failoverWithDataLossGracePeriodMinutes
              value: integer
        - name: readOnlyEndpoint
          value:
            - name: failoverPolicy
              value: string
            - name: targetServer
              value: string
        - name: replicationRole
          value: string
        - name: replicationState
          value: string
        - name: partnerServers
          value:
            - - name: id
                value: string
              - name: location
                value: string
              - name: replicationRole
                value: string
        - name: databases
          value:
            - string
        - name: secondaryType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>failover_groups</code> resource.

```sql
/*+ update */
UPDATE azure.sql.failover_groups
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
failoverGroupName = '{{ failoverGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>failover_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.failover_groups
WHERE failoverGroupName = '{{ failoverGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
