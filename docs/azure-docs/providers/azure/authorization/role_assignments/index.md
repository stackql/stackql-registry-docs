---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
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

Creates, updates, deletes, gets or lists a <code>role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role assignment ID. |
| <CopyableCode code="name" /> | `string` | The role assignment name. |
| <CopyableCode code="properties" /> | `object` | Role assignment properties. |
| <CopyableCode code="type" /> | `string` | The role assignment type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleAssignmentName, scope" /> | Get a role assignment by scope and name. |
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="roleAssignmentId" /> | Get a role assignment by ID. |
| <CopyableCode code="list_for_resource" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | List all role assignments that apply to a resource. |
| <CopyableCode code="list_for_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all role assignments that apply to a resource group. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | List all role assignments that apply to a scope. |
| <CopyableCode code="list_for_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all role assignments that apply to a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="roleAssignmentName, scope, data__properties" /> | Create or update a role assignment by scope and name. |
| <CopyableCode code="create_by_id" /> | `INSERT` | <CopyableCode code="roleAssignmentId, data__properties" /> | Create or update a role assignment by ID. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleAssignmentName, scope" /> | Delete a role assignment by scope and name. |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="roleAssignmentId" /> | Delete a role assignment by ID. |

## `SELECT` examples

List all role assignments that apply to a scope.


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.role_assignments
WHERE scope = '{{ scope }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_assignments</code> resource.

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
INSERT INTO azure.authorization.role_assignments (
roleAssignmentId,
data__properties,
properties
)
SELECT 
'{{ roleAssignmentId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
        - name: description
          value: string
        - name: condition
          value: string
        - name: conditionVersion
          value: string
        - name: createdOn
          value: string
        - name: updatedOn
          value: string
        - name: createdBy
          value: string
        - name: updatedBy
          value: string
        - name: delegatedManagedIdentityResourceId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>role_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.authorization.role_assignments
WHERE roleAssignmentId = '{{ roleAssignmentId }}';
```
