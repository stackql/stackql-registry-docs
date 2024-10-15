---
title: migrate_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - migrate_projects
  - migrate_projects
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

Creates, updates, deletes, gets or lists a <code>migrate_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migrate_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.migrate_projects" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_migrate_projects', value: 'view', },
        { label: 'migrate_projects', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the relative URL to get this migrate project. |
| <CopyableCode code="name" /> | `text` | Gets the name of the migrate project. |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_summary_refreshed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Gets or sets the Azure location in which migrate project is created. |
| <CopyableCode code="migrateProjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="refresh_summary_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registered_tools" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the tags. |
| <CopyableCode code="type" /> | `text` | Handled by resource provider. Type = Microsoft.Migrate/MigrateProject. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the relative URL to get this migrate project. |
| <CopyableCode code="name" /> | `string` | Gets the name of the migrate project. |
| <CopyableCode code="eTag" /> | `string` | Gets or sets the eTag for concurrency control. |
| <CopyableCode code="location" /> | `string` | Gets or sets the Azure location in which migrate project is created. |
| <CopyableCode code="properties" /> | `object` | Class for migrate project properties. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the tags. |
| <CopyableCode code="type" /> | `string` | Handled by resource provider. Type = Microsoft.Migrate/MigrateProject. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> | Delete the migrate project. Deleting non-existent project is a no-operation. |
| <CopyableCode code="patch_migrate_project" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> | Update a migrate project with specified name. Supports partial updates, for example only tags can be provided. |
| <CopyableCode code="put_migrate_project" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="refresh_migrate_project_summary" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="register_tool" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_migrate_projects', value: 'view', },
        { label: 'migrate_projects', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
e_tag,
last_summary_refreshed_time,
location,
migrateProjectName,
provisioning_state,
refresh_summary_state,
registered_tools,
resourceGroupName,
subscriptionId,
summary,
tags,
type
FROM azure.migrate_projects.vw_migrate_projects
WHERE migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
location,
properties,
tags,
type
FROM azure.migrate_projects.migrate_projects
WHERE migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>migrate_projects</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate_projects.migrate_projects
WHERE migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
