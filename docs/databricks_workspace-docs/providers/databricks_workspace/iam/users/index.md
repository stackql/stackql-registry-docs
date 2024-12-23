---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - users
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

Operations on a <code>users</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `object` |
| <CopyableCode code="active" /> | `boolean` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="emails" /> | `array` |
| <CopyableCode code="entitlements" /> | `array` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="groups" /> | `array` |
| <CopyableCode code="roles" /> | `array` |
| <CopyableCode code="schemas" /> | `array` |
| <CopyableCode code="userName" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets information for a specific user in Databricks workspace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets details for all the users associated with a Databricks workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new user in the Databricks workspace. This new user will also be added to the Databricks account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Deletes a user. Deleting a user from a Databricks workspace also removes objects associated with the user. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Partially updates a user resource by applying the supplied operations on specific user attributes. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Replaces a user's information with the data supplied in request. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'users (list)', value: 'list' },
        { label: 'users (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
active,
displayName,
emails,
entitlements,
externalId,
groups,
roles,
schemas,
userName
FROM databricks_workspace.iam.users
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
active,
displayName,
emails,
entitlements,
externalId,
groups,
roles,
schemas,
userName
FROM databricks_workspace.iam.users
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'users', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.iam.users (
deployment_name,
data__schemas,
data__userName,
data__emails,
data__name,
data__displayName,
data__groups,
data__roles,
data__entitlements,
data__externalId,
data__active
)
SELECT 
'{{ deployment_name }}',
'{{ schemas }}',
'{{ userName }}',
'{{ emails }}',
'{{ name }}',
'{{ displayName }}',
'{{ groups }}',
'{{ roles }}',
'{{ entitlements }}',
'{{ externalId }}',
'{{ active }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: schemas
    value:
    - urn:ietf:params:scim:schemas:core:2.0:User
  - name: userName
    value: user@example.com
  - name: emails
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: name
    value:
      givenName: string
      familyName: string
  - name: displayName
    value: string
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
  - name: active
    value: true

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>users</code> resource.

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
UPDATE databricks_workspace.iam.users
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
UPDATE databricks_workspace.iam.users
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.iam.users
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
