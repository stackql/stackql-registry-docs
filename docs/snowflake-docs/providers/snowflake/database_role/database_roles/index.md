---
title: database_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - database_roles
  - database_role
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

Creates, updates, deletes, gets or lists a <code>database_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.database_role.database_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the database role |
| <CopyableCode code="comment" /> | `string` | User comment associated to an object in the dictionary |
| <CopyableCode code="created_on" /> | `string` | Date and time when the database role was created |
| <CopyableCode code="granted_database_roles" /> | `integer` | How many database roles this database role has been granted |
| <CopyableCode code="granted_to_database_roles" /> | `integer` | How many database roles this database role has been granted to |
| <CopyableCode code="granted_to_roles" /> | `integer` | How many roles this database role has been granted to |
| <CopyableCode code="owner" /> | `string` | Role that owns the database role |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the database role |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_database_roles" /> | `SELECT` | <CopyableCode code="database_name, endpoint" /> | <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | List database roles |
| <CopyableCode code="create_database_role" /> | `INSERT` | <CopyableCode code="database_name, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a database role |
| <CopyableCode code="delete_database_role" /> | `DELETE` | <CopyableCode code="database_name, name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a database role |
| <CopyableCode code="clone_database_role" /> | `EXEC` | <CopyableCode code="database_name, name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="targetDatabase" /> | Create a new database role by cloning from the specified resource |

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="targetDatabase" /> | Database of the target resource. Defaults to the source's database | `string` | `-` |

</details>

## `SELECT` examples

List database roles


```sql
SELECT
name,
comment,
created_on,
granted_database_roles,
granted_to_database_roles,
granted_to_roles,
owner,
owner_role_type
FROM snowflake.database_role.database_roles
WHERE database_name = '{{ database_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_roles</code> resource.

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
INSERT INTO snowflake.database_role.database_roles (
data__name,
data__comment,
database_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ database_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.database_role.database_roles (
data__name,
database_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ database_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: database_roles
  props:
    - name: database_name
      value: string
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

Deletes the specified <code>database_roles</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.database_role.database_roles
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
