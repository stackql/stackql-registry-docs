---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - groups
  - iam
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>groups</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="entitlements" /> | `array` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="groups" /> | `array` |
| <CopyableCode code="members" /> | `array` |
| <CopyableCode code="roles" /> | `array` |
| <CopyableCode code="schemas" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets the information for a specific group in the Databricks workspace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets all details of the groups associated with the Databricks workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a group in the Databricks workspace with a unique name, using the supplied group details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Deletes a group from the Databricks workspace. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Partially updates the details of a group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Updates the details of a group by replacing the entire group entity. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'groups (list)', value: 'list' },
        { label: 'groups (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
displayName,
entitlements,
externalId,
groups,
members,
roles,
schemas
FROM databricks_workspace.iam.groups
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
displayName,
entitlements,
externalId,
groups,
members,
roles,
schemas
FROM databricks_workspace.iam.groups
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'groups', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.iam.groups (
deployment_name,
data__schemas,
data__displayName,
data__members,
data__groups,
data__roles,
data__entitlements,
data__externalId
)
SELECT 
'{{ deployment_name }}',
'{{ schemas }}',
'{{ displayName }}',
'{{ members }}',
'{{ groups }}',
'{{ roles }}',
'{{ entitlements }}',
'{{ externalId }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: schemas
    value:
    - urn:ietf:params:scim:schemas:core:2.0:Group
  - name: displayName
    value: string
  - name: members
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: groups
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: roles
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: entitlements
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: externalId
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>groups</code> resource.

<Tabs
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' },
        { label: 'update', value: 'update' }
    ]
}>
<TabItem value="patch">

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.iam.groups
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
<TabItem value="update">

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.iam.groups
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.iam.groups
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
