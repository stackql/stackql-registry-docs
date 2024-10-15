---
title: access_review_instances_assigned_for_my_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instances_assigned_for_my_approval
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

Creates, updates, deletes, gets or lists a <code>access_review_instances_assigned_for_my_approval</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_instances_assigned_for_my_approval</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_instances_assigned_for_my_approval" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_instances_assigned_for_my_approval', value: 'view', },
        { label: 'access_review_instances_assigned_for_my_approval', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The access review instance id. |
| <CopyableCode code="name" /> | `text` | The access review instance name. |
| <CopyableCode code="backup_reviewers" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reviewers" /> | `text` | field from the `properties` object |
| <CopyableCode code="reviewers_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review instance id. |
| <CopyableCode code="name" /> | `string` | The access review instance name. |
| <CopyableCode code="properties" /> | `object` | Access Review Instance properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="id, scheduleDefinitionId" /> | Get single access review instance assigned for my approval. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scheduleDefinitionId" /> | Get access review instances assigned for my approval. |

## `SELECT` examples

Get access review instances assigned for my approval.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_instances_assigned_for_my_approval', value: 'view', },
        { label: 'access_review_instances_assigned_for_my_approval', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_reviewers,
end_date_time,
reviewers,
reviewers_type,
scheduleDefinitionId,
start_date_time,
status,
type
FROM azure.authorization.vw_access_review_instances_assigned_for_my_approval
WHERE scheduleDefinitionId = '{{ scheduleDefinitionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.access_review_instances_assigned_for_my_approval
WHERE scheduleDefinitionId = '{{ scheduleDefinitionId }}';
```
</TabItem></Tabs>

