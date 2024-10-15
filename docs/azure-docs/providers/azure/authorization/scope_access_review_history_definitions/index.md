---
title: scope_access_review_history_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_history_definitions
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

Creates, updates, deletes, gets or lists a <code>scope_access_review_history_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scope_access_review_history_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_history_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_access_review_history_definitions', value: 'view', },
        { label: 'scope_access_review_history_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The access review history definition id. |
| <CopyableCode code="name" /> | `text` | The access review history definition unique id. |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="decisions" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="historyDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="review_history_period_end_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="review_history_period_start_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review history definition id. |
| <CopyableCode code="name" /> | `string` | The access review history definition unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review History Instances. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="historyDefinitionId, scope" /> | Get access review history definition by definition Id |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Lists the accessReviewHistoryDefinitions available from this provider, definition instances are only available for 30 days after creation. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="historyDefinitionId, scope" /> | Create a scheduled or one-time Access Review History Definition |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="historyDefinitionId, scope" /> | Delete an access review history definition |

## `SELECT` examples

Lists the accessReviewHistoryDefinitions available from this provider, definition instances are only available for 30 days after creation.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_access_review_history_definitions', value: 'view', },
        { label: 'scope_access_review_history_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_by,
created_date_time,
decisions,
display_name,
historyDefinitionId,
instances,
review_history_period_end_date_time,
review_history_period_start_date_time,
scope,
scopes,
settings,
status,
type
FROM azure.authorization.vw_scope_access_review_history_definitions
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.scope_access_review_history_definitions
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scope_access_review_history_definitions</code> resource.

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
INSERT INTO azure.authorization.scope_access_review_history_definitions (
historyDefinitionId,
scope,
displayName,
decisions,
scopes,
settings,
instances
)
SELECT 
'{{ historyDefinitionId }}',
'{{ scope }}',
'{{ displayName }}',
'{{ decisions }}',
'{{ scopes }}',
'{{ settings }}',
'{{ instances }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: reviewHistoryPeriodStartDateTime
      value: string
    - name: reviewHistoryPeriodEndDateTime
      value: string
    - name: decisions
      value:
        - string
    - name: status
      value: string
    - name: createdDateTime
      value: string
    - name: createdBy
      value:
        - name: principalId
          value: string
        - name: principalType
          value: string
        - name: principalName
          value: string
        - name: userPrincipalName
          value: string
    - name: scopes
      value:
        - - name: resourceId
            value: string
          - name: roleDefinitionId
            value: string
          - name: principalType
            value: string
          - name: assignmentState
            value: string
          - name: inactiveDuration
            value: string
          - name: expandNestedMemberships
            value: boolean
          - name: includeInheritedAccess
            value: boolean
          - name: includeAccessBelowResource
            value: boolean
          - name: excludeResourceId
            value: string
          - name: excludeRoleDefinitionId
            value: string
    - name: settings
      value:
        - name: pattern
          value:
            - name: type
              value: string
            - name: interval
              value: integer
        - name: range
          value:
            - name: type
              value: string
            - name: numberOfOccurrences
              value: integer
            - name: startDate
              value: string
            - name: endDate
              value: string
    - name: instances
      value:
        - - name: id
            value: string
          - name: name
            value: string
          - name: type
            value: string
          - name: properties
            value:
              - name: reviewHistoryPeriodStartDateTime
                value: string
              - name: reviewHistoryPeriodEndDateTime
                value: string
              - name: displayName
                value: string
              - name: status
                value: string
              - name: runDateTime
                value: string
              - name: fulfilledDateTime
                value: string
              - name: downloadUri
                value: string
              - name: expiration
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>scope_access_review_history_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.authorization.scope_access_review_history_definitions
WHERE historyDefinitionId = '{{ historyDefinitionId }}'
AND scope = '{{ scope }}';
```
