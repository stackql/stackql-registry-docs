---
title: machines_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_machines
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

Creates, updates, deletes, gets or lists a <code>machines_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>machines_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.machines_machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_machines_machines', value: 'view', },
        { label: 'machines_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of this REST resource. |
| <CopyableCode code="assessment_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrateProjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the type of this REST resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of this REST resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the machine resource. |
| <CopyableCode code="type" /> | `string` | Gets the type of this REST resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, migrateProjectName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_machines_machines', value: 'view', },
        { label: 'machines_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
assessment_data,
discovery_data,
last_updated_time,
machineName,
migrateProjectName,
migration_data,
resourceGroupName,
subscriptionId,
type
FROM azure.migrate_projects.vw_machines_machines
WHERE machineName = '{{ machineName }}'
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
FROM azure.migrate_projects.machines_machines
WHERE machineName = '{{ machineName }}'
AND migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

