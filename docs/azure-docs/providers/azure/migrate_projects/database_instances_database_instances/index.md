---
title: database_instances_database_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - database_instances_database_instances
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

Creates, updates, deletes, gets or lists a <code>database_instances_database_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_instances_database_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.database_instances_database_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_instances_database_instances', value: 'view', },
        { label: 'database_instances_database_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of this REST resource. |
| <CopyableCode code="databaseInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrateProjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the type of this REST resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of this REST resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the database instance resource. |
| <CopyableCode code="type" /> | `string` | Gets the type of this REST resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseInstanceName, migrateProjectName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_instances_database_instances', value: 'view', },
        { label: 'database_instances_database_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
databaseInstanceName,
discovery_data,
last_updated_time,
migrateProjectName,
resourceGroupName,
subscriptionId,
summary,
type
FROM azure.migrate_projects.vw_database_instances_database_instances
WHERE databaseInstanceName = '{{ databaseInstanceName }}'
AND migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.migrate_projects.database_instances_database_instances
WHERE databaseInstanceName = '{{ databaseInstanceName }}'
AND migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

