---
title: scope_access_review_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instances
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

Creates, updates, deletes, gets or lists a <code>scope_access_review_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scope_access_review_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_access_review_instances', value: 'view', },
        { label: 'scope_access_review_instances', value: 'resource', },
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
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | Get access review instances |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scheduleDefinitionId, scope" /> | Get access review instances |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | Update access review instance. |
| <CopyableCode code="apply_decisions" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to apply all decisions for an access review instance. |
| <CopyableCode code="record_all_decisions" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to approve/deny all decisions for a review with certain filters. |
| <CopyableCode code="reset_decisions" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to reset all decisions for an access review instance. |
| <CopyableCode code="send_reminders" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to send reminders for an access review instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to stop an access review instance. |

## `SELECT` examples

Get access review instances

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_access_review_instances', value: 'view', },
        { label: 'scope_access_review_instances', value: 'resource', },
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
scope,
start_date_time,
status,
type
FROM azure.authorization.vw_scope_access_review_instances
WHERE scheduleDefinitionId = '{{ scheduleDefinitionId }}'
AND scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.scope_access_review_instances
WHERE scheduleDefinitionId = '{{ scheduleDefinitionId }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scope_access_review_instances</code> resource.

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
INSERT INTO azure.authorization.scope_access_review_instances (
id,
scheduleDefinitionId,
scope,
startDateTime,
endDateTime,
reviewers,
backupReviewers
)
SELECT 
'{{ id }}',
'{{ scheduleDefinitionId }}',
'{{ scope }}',
'{{ startDateTime }}',
'{{ endDateTime }}',
'{{ reviewers }}',
'{{ backupReviewers }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: status
      value: string
    - name: startDateTime
      value: string
    - name: endDateTime
      value: string
    - name: reviewers
      value:
        - - name: principalId
            value: string
          - name: principalType
            value: string
    - name: backupReviewers
      value:
        - - name: principalId
            value: string
          - name: principalType
            value: string
    - name: reviewersType
      value: string

```
</TabItem>
</Tabs>
