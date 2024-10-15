---
title: role_management_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policy_assignments
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

Creates, updates, deletes, gets or lists a <code>role_management_policy_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_management_policy_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_management_policy_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_management_policy_assignments', value: 'view', },
        { label: 'role_management_policy_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The role management policy Id. |
| <CopyableCode code="name" /> | `text` | The role management policy name. |
| <CopyableCode code="effective_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_assignment_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleManagementPolicyAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The role management policy type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role management policy Id. |
| <CopyableCode code="name" /> | `string` | The role management policy name. |
| <CopyableCode code="properties" /> | `object` | Role management policy assignment properties with scope. |
| <CopyableCode code="type" /> | `string` | The role management policy type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleManagementPolicyAssignmentName, scope" /> | Get the specified role management policy assignment for a resource scope |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets role management assignment policies for a resource scope. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="roleManagementPolicyAssignmentName, scope" /> | Create a role management policy assignment |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleManagementPolicyAssignmentName, scope" /> | Delete a role management policy assignment |

## `SELECT` examples

Gets role management assignment policies for a resource scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_management_policy_assignments', value: 'view', },
        { label: 'role_management_policy_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
effective_rules,
policy_assignment_properties,
policy_id,
roleManagementPolicyAssignmentName,
role_definition_id,
scope,
type
FROM azure.authorization.vw_role_management_policy_assignments
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
FROM azure.authorization.role_management_policy_assignments
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_management_policy_assignments</code> resource.

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
INSERT INTO azure.authorization.role_management_policy_assignments (
roleManagementPolicyAssignmentName,
scope,
properties
)
SELECT 
'{{ roleManagementPolicyAssignmentName }}',
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
        - name: policyId
          value: string
        - name: effectiveRules
          value:
            - - name: id
                value: string
              - name: ruleType
                value: []
              - name: target
                value:
                  - name: caller
                    value: string
                  - name: operations
                    value:
                      - string
                  - name: level
                    value: string
                  - name: targetObjects
                    value:
                      - string
                  - name: inheritableSettings
                    value:
                      - string
                  - name: enforcedSettings
                    value:
                      - string
        - name: policyAssignmentProperties
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
            - name: policy
              value:
                - name: id
                  value: string
                - name: lastModifiedBy
                  value:
                    - name: id
                      value: string
                    - name: displayName
                      value: string
                    - name: type
                      value: string
                    - name: email
                      value: string
                - name: lastModifiedDateTime
                  value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>role_management_policy_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.authorization.role_management_policy_assignments
WHERE roleManagementPolicyAssignmentName = '{{ roleManagementPolicyAssignmentName }}'
AND scope = '{{ scope }}';
```
