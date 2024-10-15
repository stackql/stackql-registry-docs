---
title: events_events
hide_title: false
hide_table_of_contents: false
keywords:
  - events_events
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

Creates, updates, deletes, gets or lists a <code>events_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.events_events" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_events_events', value: 'view', },
        { label: 'events_events', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of this REST resource. |
| <CopyableCode code="client_request_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="eventName" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrateProjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="possible_causes" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the type of this REST resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of this REST resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the error resource. |
| <CopyableCode code="type" /> | `string` | Gets the type of this REST resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventName, migrateProjectName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventName, migrateProjectName, resourceGroupName, subscriptionId" /> | Delete the migrate event. Deleting non-existent migrate event is a no-operation. |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_events_events', value: 'view', },
        { label: 'events_events', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
client_request_id,
error_code,
error_message,
eventName,
instance_type,
migrateProjectName,
possible_causes,
recommendation,
resourceGroupName,
solution,
subscriptionId,
type
FROM azure.migrate_projects.vw_events_events
WHERE eventName = '{{ eventName }}'
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
FROM azure.migrate_projects.events_events
WHERE eventName = '{{ eventName }}'
AND migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>events_events</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate_projects.events_events
WHERE eventName = '{{ eventName }}'
AND migrateProjectName = '{{ migrateProjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
