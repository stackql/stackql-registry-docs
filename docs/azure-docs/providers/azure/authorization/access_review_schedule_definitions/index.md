---
title: access_review_schedule_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions
  - authorization
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

Creates, updates, deletes, gets or lists a <code>access_review_schedule_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_schedule_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_schedule_definitions', value: 'view', },
        { label: 'access_review_schedule_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The access review schedule definition id. |
| <CopyableCode code="name" /> | `text` | The access review schedule definition unique id. |
| <CopyableCode code="backup_reviewers" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="description_for_admins" /> | `text` | field from the `properties` object |
| <CopyableCode code="description_for_reviewers" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="reviewers" /> | `text` | field from the `properties` object |
| <CopyableCode code="reviewers_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review schedule definition id. |
| <CopyableCode code="name" /> | `string` | The access review schedule definition unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Get single access review definition |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get access review schedule definitions |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Delete access review schedule definition |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Stop access review definition |

## `SELECT` examples

Get access review schedule definitions

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_schedule_definitions', value: 'view', },
        { label: 'access_review_schedule_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_reviewers,
created_by,
description_for_admins,
description_for_reviewers,
display_name,
instances,
reviewers,
reviewers_type,
scheduleDefinitionId,
scope,
settings,
status,
subscriptionId,
type
FROM azure.authorization.vw_access_review_schedule_definitions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.access_review_schedule_definitions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>access_review_schedule_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.authorization.access_review_schedule_definitions
WHERE scheduleDefinitionId = '{{ scheduleDefinitionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
