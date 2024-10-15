---
title: disk_migration_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_migration_jobs
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>disk_migration_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_migration_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.disk_migration_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_migration_jobs', value: 'view', },
        { label: 'disk_migration_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="migrationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subtasks" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_share" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Disk migration job properties. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, migrationId, subscriptionId" /> | Returns the requested disk migration job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of disk migration jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, migrationId, subscriptionId" /> | Create a disk migration job. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="location, migrationId, subscriptionId" /> | Cancel a disk migration job. |

## `SELECT` examples

Returns a list of disk migration jobs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_migration_jobs', value: 'view', },
        { label: 'disk_migration_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
creation_time,
end_time,
location,
migrationId,
migration_id,
start_time,
status,
subscriptionId,
subtasks,
target_share,
type
FROM azure_stack.compute_admin.vw_disk_migration_jobs
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.compute_admin.disk_migration_jobs
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disk_migration_jobs</code> resource.

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
INSERT INTO azure_stack.compute_admin.disk_migration_jobs (
location,
migrationId,
subscriptionId
)
SELECT 
'{{ location }}',
'{{ migrationId }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>
