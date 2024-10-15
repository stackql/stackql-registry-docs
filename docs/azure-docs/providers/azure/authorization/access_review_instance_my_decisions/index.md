---
title: access_review_instance_my_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instance_my_decisions
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

Creates, updates, deletes, gets or lists a <code>access_review_instance_my_decisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_instance_my_decisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_instance_my_decisions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_instance_my_decisions', value: 'view', },
        { label: 'access_review_instance_my_decisions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The access review decision id. |
| <CopyableCode code="name" /> | `text` | The access review decision name. |
| <CopyableCode code="applied_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="apply_result" /> | `text` | field from the `properties` object |
| <CopyableCode code="decision" /> | `text` | field from the `properties` object |
| <CopyableCode code="decisionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="insights" /> | `text` | field from the `properties` object |
| <CopyableCode code="justification" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_resource_membership" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="reviewed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="reviewed_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review decision id. |
| <CopyableCode code="name" /> | `string` | The access review decision name. |
| <CopyableCode code="properties" /> | `object` | Approval Step. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="decisionId, id, scheduleDefinitionId" /> | Get my single access review instance decision. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="id, scheduleDefinitionId" /> | Get my access review instance decisions. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="decisionId, id, scheduleDefinitionId" /> | Record a decision. |

## `SELECT` examples

Get my access review instance decisions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_instance_my_decisions', value: 'view', },
        { label: 'access_review_instance_my_decisions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applied_by,
applied_date_time,
apply_result,
decision,
decisionId,
insights,
justification,
principal,
principal_resource_membership,
recommendation,
resource,
reviewed_by,
reviewed_date_time,
scheduleDefinitionId,
type
FROM azure.authorization.vw_access_review_instance_my_decisions
WHERE id = '{{ id }}'
AND scheduleDefinitionId = '{{ scheduleDefinitionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.access_review_instance_my_decisions
WHERE id = '{{ id }}'
AND scheduleDefinitionId = '{{ scheduleDefinitionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>access_review_instance_my_decisions</code> resource.

```sql
/*+ update */
UPDATE azure.authorization.access_review_instance_my_decisions
SET 
decision = '{{ decision }}',
justification = '{{ justification }}',
insights = '{{ insights }}'
WHERE 
decisionId = '{{ decisionId }}'
AND id = '{{ id }}'
AND scheduleDefinitionId = '{{ scheduleDefinitionId }}';
```
