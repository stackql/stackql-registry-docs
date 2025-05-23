---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - role
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.role.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the role. |
| <CopyableCode code="assigned_to_users" /> | `integer` | The number of users to whom this role has been assigned. |
| <CopyableCode code="comment" /> | `string` | Comment of the role. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the role was created. |
| <CopyableCode code="granted_roles" /> | `integer` | The number of roles that have been granted to this role. |
| <CopyableCode code="granted_to_roles" /> | `integer` | The number of roles to which this role has been granted. |
| <CopyableCode code="is_current" /> | `boolean` | Specifies whether the role being fetched is the user's current role. |
| <CopyableCode code="is_default" /> | `boolean` | Specifies whether the role being fetched is the user's default role. |
| <CopyableCode code="is_inherited" /> | `boolean` | Specifies whether the role used to run the command inherits the specified role. |
| <CopyableCode code="owner" /> | `string` | Specifies the role that owns this role. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_roles" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | List roles |
| <CopyableCode code="create_role" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a role |
| <CopyableCode code="delete_role" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a role |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

List roles


```sql
SELECT
name,
assigned_to_users,
comment,
created_on,
granted_roles,
granted_to_roles,
is_current,
is_default,
is_inherited,
owner
FROM snowflake.role.roles
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>roles</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.role.roles (
data__name,
data__comment,
endpoint
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.role.roles (
data__name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: roles
  props:
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: comment
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>roles</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.role.roles
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
