---
title: redis
hide_title: false
hide_table_of_contents: false
keywords:
  - redis
  - redis
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

Creates, updates, deletes, gets or lists a <code>redis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>redis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.redis" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_redis', value: 'view', },
        { label: 'redis', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssl_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting where the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the redis cache. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets a Redis cache (resource description). |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Redis caches in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Redis caches in the specified subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes a Redis cache. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Update an existing Redis cache. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the redis cache name is valid and is not already in use. |
| <CopyableCode code="export_data" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__container, data__prefix" /> | Export data from the redis cache to blobs in a container. |
| <CopyableCode code="flush_cache" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Deletes all of the keys in a cache. |
| <CopyableCode code="force_reboot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss. |
| <CopyableCode code="import_data" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__files" /> | Import data into Redis cache. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__keyType" /> | Regenerate Redis cache's access keys. This operation requires write permission to the cache resource. |

## `SELECT` examples

Gets all Redis caches in the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_redis', value: 'view', },
        { label: 'redis', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
access_keys,
host_name,
identity,
instances,
linked_servers,
location,
port,
private_endpoint_connections,
provisioning_state,
resourceGroupName,
sku,
ssl_port,
static_ip,
subnet_id,
subscriptionId,
tags,
zones
FROM azure_isv.redis.vw_redis
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags,
zones
FROM azure_isv.redis.redis
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>redis</code> resource.

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
INSERT INTO azure_isv.redis.redis (
name,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
properties,
zones,
location,
tags,
identity
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ zones }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: sku
          value:
            - name: name
              value: string
            - name: family
              value: string
            - name: capacity
              value: integer
        - name: subnetId
          value: string
        - name: staticIP
          value: string
        - name: redisConfiguration
          value:
            - name: rdb-backup-enabled
              value: string
            - name: rdb-backup-frequency
              value: string
            - name: rdb-backup-max-snapshot-count
              value: string
            - name: rdb-storage-connection-string
              value: string
            - name: aof-backup-enabled
              value: string
            - name: aof-storage-connection-string-0
              value: string
            - name: aof-storage-connection-string-1
              value: string
            - name: maxfragmentationmemory-reserved
              value: string
            - name: maxmemory-policy
              value: string
            - name: maxmemory-reserved
              value: string
            - name: maxmemory-delta
              value: string
            - name: maxclients
              value: string
            - name: notify-keyspace-events
              value: string
            - name: preferred-data-archive-auth-method
              value: string
            - name: preferred-data-persistence-auth-method
              value: string
            - name: zonal-configuration
              value: string
            - name: authnotrequired
              value: string
            - name: storage-subscription-id
              value: string
            - name: aad-enabled
              value: string
        - name: redisVersion
          value: string
        - name: enableNonSslPort
          value: boolean
        - name: replicasPerMaster
          value: integer
        - name: replicasPerPrimary
          value: integer
        - name: tenantSettings
          value: object
        - name: shardCount
          value: integer
        - name: minimumTlsVersion
          value: string
        - name: publicNetworkAccess
          value: string
        - name: updateChannel
          value: string
        - name: disableAccessKeyAuthentication
          value: boolean
        - name: zonalAllocationPolicy
          value: string
    - name: zones
      value:
        - string
    - name: location
      value: string
    - name: tags
      value: object
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>redis</code> resource.

```sql
/*+ update */
UPDATE azure_isv.redis.redis
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>redis</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis.redis
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
