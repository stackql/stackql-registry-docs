---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
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

Creates, updates, deletes, gets or lists a <code>solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.solutions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions', value: 'view', },
        { label: 'solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `text` | Gets the name of this REST resource. |
| <CopyableCode code="cleanup_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets or sets the ETAG for optimistic concurrency control. |
| <CopyableCode code="goal" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrateProjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="purpose" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="tool" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the type of this REST resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of this REST resource. |
| <CopyableCode code="etag" /> | `string` | Gets or sets the ETAG for optimistic concurrency control. |
| <CopyableCode code="properties" /> | `object` | Class for solution properties. |
| <CopyableCode code="type" /> | `string` | Gets the type of this REST resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> | Delete the solution. Deleting non-existent project is a no-operation. |
| <CopyableCode code="cleanup_solution_data" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> |  |
| <CopyableCode code="enumerate_solutions" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="patch_solution" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> | Update a solution with specified name. Supports partial updates, for example only tags can be provided. |
| <CopyableCode code="put_solution" /> | `EXEC` | <CopyableCode code="migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions', value: 'view', },
        { label: 'solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cleanup_state,
details,
etag,
goal,
migrateProjectName,
purpose,
resourceGroupName,
solutionName,
status,
subscriptionId,
summary,
tool,
type
FROM azure.migrate_projects.vw_solutions
WHERE migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.migrate_projects.solutions
WHERE migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>solutions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate_projects.solutions
WHERE migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
