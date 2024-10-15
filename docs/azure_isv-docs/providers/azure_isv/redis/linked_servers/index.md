---
title: linked_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_servers
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

Creates, updates, deletes, gets or lists a <code>linked_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linked_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.linked_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_servers', value: 'view', },
        { label: 'linked_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="geo_replicated_primary_host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkedServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_redis_cache_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_redis_cache_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a linked server to be returned in get/put response |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="linkedServerName, name, resourceGroupName, subscriptionId" /> | Gets the detailed information about a linked server of a redis cache (requires Premium SKU). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets the list of linked servers associated with this redis cache (requires Premium SKU). |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="linkedServerName, name, resourceGroupName, subscriptionId, data__properties" /> | Adds a linked server to the Redis cache (requires Premium SKU). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="linkedServerName, name, resourceGroupName, subscriptionId" /> | Deletes the linked server from a redis cache (requires Premium SKU). |

## `SELECT` examples

Gets the list of linked servers associated with this redis cache (requires Premium SKU).

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_servers', value: 'view', },
        { label: 'linked_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
geo_replicated_primary_host_name,
linkedServerName,
linked_redis_cache_id,
linked_redis_cache_location,
primary_host_name,
provisioning_state,
resourceGroupName,
server_role,
subscriptionId
FROM azure_isv.redis.vw_linked_servers
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.redis.linked_servers
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>linked_servers</code> resource.

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
INSERT INTO azure_isv.redis.linked_servers (
linkedServerName,
name,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ linkedServerName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: linkedRedisCacheId
          value: string
        - name: linkedRedisCacheLocation
          value: string
        - name: serverRole
          value: string
        - name: geoReplicatedPrimaryHostName
          value: string
        - name: primaryHostName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>linked_servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis.linked_servers
WHERE linkedServerName = '{{ linkedServerName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
