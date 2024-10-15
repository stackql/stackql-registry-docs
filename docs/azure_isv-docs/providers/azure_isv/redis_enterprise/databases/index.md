---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - redis_enterprise
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_databases', value: 'view', },
        { label: 'databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_keys_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clustering_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="defer_upgrade" /> | `text` | field from the `properties` object |
| <CopyableCode code="eviction_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="geo_replication" /> | `text` | field from the `properties` object |
| <CopyableCode code="modules" /> | `text` | field from the `properties` object |
| <CopyableCode code="persistence" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="redis_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of Redis Enterprise databases, as opposed to general resource properties like location, tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Gets information about a database in a Redis Enterprise cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets all databases in the specified Redis Enterprise cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Creates a database |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Deletes a single database |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Updates a database |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUri" /> | Exports a database file from target database. |
| <CopyableCode code="flush" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Flushes all the keys in this database and also from its linked databases. |
| <CopyableCode code="force_link_to_replication_group" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__groupNickname, data__linkedDatabases" /> | Forcibly recreates an existing database on the specified cluster, and rejoins it to an existing replication group. **IMPORTANT NOTE:** All data in this database will be discarded, and the database will temporarily be unavailable while rejoining the replication group. |
| <CopyableCode code="force_unlink" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__ids" /> | Forcibly removes the link to the specified database resource. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUris" /> | Imports database files to target database. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the Redis Enterprise database's access keys. |
| <CopyableCode code="upgrade_db_redis_version" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Upgrades the database Redis version to the latest available. |

## `SELECT` examples

Gets all databases in the specified Redis Enterprise cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_databases', value: 'view', },
        { label: 'databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_keys_authentication,
client_protocol,
clusterName,
clustering_policy,
databaseName,
defer_upgrade,
eviction_policy,
geo_replication,
modules,
persistence,
port,
provisioning_state,
redis_version,
resourceGroupName,
resource_state,
subscriptionId
FROM azure_isv.redis_enterprise.vw_databases
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.redis_enterprise.databases
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

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
INSERT INTO azure_isv.redis_enterprise.databases (
clusterName,
databaseName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
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
        - name: clientProtocol
          value: string
        - name: port
          value: integer
        - name: provisioningState
          value: []
        - name: resourceState
          value: []
        - name: clusteringPolicy
          value: string
        - name: evictionPolicy
          value: string
        - name: persistence
          value:
            - name: aofEnabled
              value: boolean
            - name: rdbEnabled
              value: boolean
            - name: aofFrequency
              value: string
            - name: rdbFrequency
              value: string
        - name: modules
          value:
            - - name: name
                value: string
              - name: args
                value: string
              - name: version
                value: string
        - name: geoReplication
          value:
            - name: groupNickname
              value: string
            - name: linkedDatabases
              value:
                - - name: id
                    value: string
                  - name: state
                    value: string
        - name: redisVersion
          value: string
        - name: deferUpgrade
          value: string
        - name: accessKeysAuthentication
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE azure_isv.redis_enterprise.databases
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis_enterprise.databases
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
