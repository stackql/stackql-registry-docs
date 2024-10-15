---
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
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

Creates, updates, deletes, gets or lists a <code>role_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_definitions', value: 'view', },
        { label: 'role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The role definition ID. |
| <CopyableCode code="name" /> | `text` | The role definition name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignable_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The role definition type. |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_on" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role definition ID. |
| <CopyableCode code="name" /> | `string` | The role definition name. |
| <CopyableCode code="properties" /> | `object` | Role definition properties. |
| <CopyableCode code="type" /> | `string` | The role definition type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleDefinitionId, scope" /> | Get role definition by ID (GUID). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get all role definitions that are applicable at scope and above. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="roleDefinitionId, scope" /> | Creates or updates a role definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleDefinitionId, scope" /> | Deletes a role definition. |

## `SELECT` examples

Get all role definitions that are applicable at scope and above.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_definitions', value: 'view', },
        { label: 'role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assignable_scopes,
created_by,
created_on,
permissions,
roleDefinitionId,
role_name,
scope,
type,
updated_by,
updated_on
FROM azure.authorization.vw_role_definitions
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
FROM azure.authorization.role_definitions
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_definitions</code> resource.

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
INSERT INTO azure.authorization.role_definitions (
roleDefinitionId,
scope,
properties
)
SELECT 
'{{ roleDefinitionId }}',
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
        - name: roleName
          value: string
        - name: description
          value: string
        - name: type
          value: string
        - name: permissions
          value:
            - - name: actions
                value:
                  - string
              - name: notActions
                value:
                  - string
              - name: dataActions
                value:
                  - string
              - name: notDataActions
                value:
                  - string
        - name: assignableScopes
          value:
            - string
        - name: createdOn
          value: string
        - name: updatedOn
          value: string
        - name: createdBy
          value: string
        - name: updatedBy
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>role_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.authorization.role_definitions
WHERE roleDefinitionId = '{{ roleDefinitionId }}'
AND scope = '{{ scope }}';
```
