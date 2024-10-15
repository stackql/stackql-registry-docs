---
title: patch_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_schedules
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

Creates, updates, deletes, gets or lists a <code>patch_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.patch_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_patch_schedules', value: 'view', },
        { label: 'patch_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="" /> | `text` | field from the `properties` object |
| <CopyableCode code="cacheName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_entries" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | List of patch schedules for a Redis cache. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="default, name, resourceGroupName, subscriptionId" /> | Gets the patching schedule of a redis cache. |
| <CopyableCode code="list_by_redis_resource" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Gets all patch schedules in the specified redis cache (there is only one). |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="default, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace the patching schedule for Redis cache. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="default, name, resourceGroupName, subscriptionId" /> | Deletes the patching schedule of a redis cache. |

## `SELECT` examples

Gets all patch schedules in the specified redis cache (there is only one).

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_patch_schedules', value: 'view', },
        { label: 'patch_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
,
cacheName,
location,
resourceGroupName,
schedule_entries,
subscriptionId
FROM azure_isv.redis.vw_patch_schedules
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure_isv.redis.patch_schedules
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>patch_schedules</code> resource.

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
INSERT INTO azure_isv.redis.patch_schedules (
default,
name,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ default }}',
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
        - name: scheduleEntries
          value:
            - - name: dayOfWeek
                value: string
              - name: startHourUtc
                value: integer
              - name: maintenanceWindow
                value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>patch_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis.patch_schedules
WHERE default = '{{ default }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
