---
title: role_assignment_schedule_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignment_schedule_requests
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

Creates, updates, deletes, gets or lists a <code>role_assignment_schedule_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignment_schedule_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignment_schedule_requests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignment_schedule_requests', value: 'view', },
        { label: 'role_assignment_schedule_requests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The role assignment schedule request ID. |
| <CopyableCode code="name" /> | `text` | The role assignment schedule request name. |
| <CopyableCode code="approval_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="condition" /> | `text` | field from the `properties` object |
| <CopyableCode code="condition_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="expanded_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="justification" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_role_eligibility_schedule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="requestor_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleAssignmentScheduleRequestName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_role_assignment_schedule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_role_assignment_schedule_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="ticket_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The role assignment schedule request type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role assignment schedule request ID. |
| <CopyableCode code="name" /> | `string` | The role assignment schedule request name. |
| <CopyableCode code="properties" /> | `object` | Role assignment schedule request properties with scope. |
| <CopyableCode code="type" /> | `string` | The role assignment schedule request type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Get the specified role assignment schedule request. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets role assignment schedule requests for a scope. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Creates a role assignment schedule request. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Cancels a pending role assignment schedule request. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Validates a new role assignment schedule request. |

## `SELECT` examples

Gets role assignment schedule requests for a scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignment_schedule_requests', value: 'view', },
        { label: 'role_assignment_schedule_requests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
approval_id,
condition,
condition_version,
created_on,
expanded_properties,
justification,
linked_role_eligibility_schedule_id,
principal_id,
principal_type,
request_type,
requestor_id,
roleAssignmentScheduleRequestName,
role_definition_id,
schedule_info,
scope,
status,
target_role_assignment_schedule_id,
target_role_assignment_schedule_instance_id,
ticket_info,
type
FROM azure.authorization.vw_role_assignment_schedule_requests
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
FROM azure.authorization.role_assignment_schedule_requests
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_assignment_schedule_requests</code> resource.

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
INSERT INTO azure.authorization.role_assignment_schedule_requests (
roleAssignmentScheduleRequestName,
scope,
properties
)
SELECT 
'{{ roleAssignmentScheduleRequestName }}',
'{{ scope }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: scope
          value: string
        - name: roleDefinitionId
          value: string
        - name: principalId
          value: string
        - name: principalType
          value: string
        - name: requestType
          value: string
        - name: status
          value: string
        - name: approvalId
          value: string
        - name: targetRoleAssignmentScheduleId
          value: string
        - name: targetRoleAssignmentScheduleInstanceId
          value: string
        - name: scheduleInfo
          value:
            - name: startDateTime
              value: string
            - name: expiration
              value:
                - name: type
                  value: string
                - name: endDateTime
                  value: string
                - name: duration
                  value: string
        - name: linkedRoleEligibilityScheduleId
          value: string
        - name: justification
          value: string
        - name: ticketInfo
          value:
            - name: ticketNumber
              value: string
            - name: ticketSystem
              value: string
        - name: condition
          value: string
        - name: conditionVersion
          value: string
        - name: createdOn
          value: string
        - name: requestorId
          value: string
        - name: expandedProperties
          value:
            - name: scope
              value:
                - name: id
                  value: string
                - name: displayName
                  value: string
                - name: type
                  value: string
            - name: roleDefinition
              value:
                - name: id
                  value: string
                - name: displayName
                  value: string
                - name: type
                  value: string
            - name: principal
              value:
                - name: id
                  value: string
                - name: displayName
                  value: string
                - name: email
                  value: string
                - name: type
                  value: string

```
</TabItem>
</Tabs>
