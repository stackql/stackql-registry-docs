---
title: procedures
hide_title: false
hide_table_of_contents: false
keywords:
  - procedures
  - procedure
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

Creates, updates, deletes, gets or lists a <code>procedures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>procedures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.procedure.procedures" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the procedure |
| <CopyableCode code="arguments" /> | `array` | List of arguments for the function/procedure |
| <CopyableCode code="body" /> | `string` | Function/procedure definition |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the function/procedure |
| <CopyableCode code="created_on" /> | `string` | The date and time when the function/procedure was created |
| <CopyableCode code="database_name" /> | `string` | The name of the database in which the function/procedure exists. |
| <CopyableCode code="execute_as" /> | `string` | What permissions should the procedure execution be called with |
| <CopyableCode code="is_builtin" /> | `boolean` | If the function/procedure is built-in or not (user-defined) |
| <CopyableCode code="is_secure" /> | `boolean` | Specifies whether the function/procedure is secure or not |
| <CopyableCode code="language_config" /> | `object` |  |
| <CopyableCode code="max_num_arguments" /> | `integer` | The maximum number of arguments |
| <CopyableCode code="min_num_arguments" /> | `integer` | The minimum number of arguments |
| <CopyableCode code="owner" /> | `string` | Role that owns the function/procedure |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the function/procedure |
| <CopyableCode code="return_type" /> | `object` |  |
| <CopyableCode code="schema_name" /> | `string` | The name of the schema in which the function/procedure exists. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_procedure" /> | `SELECT` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | - | Fetch a procedure |
| <CopyableCode code="list_procedures" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" /> | List procedures |
| <CopyableCode code="create_procedure" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__arguments, data__body, data__language_config, data__name, data__return_type, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a procedure |
| <CopyableCode code="delete_procedure" /> | `DELETE` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a procedure |
| <CopyableCode code="call_procedure" /> | `EXEC` | <CopyableCode code="database_name, nameWithArgs, schema_name, data__call_arguments, endpoint" /> | - | Call a procedure |

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

List procedures


```sql
SELECT
name,
arguments,
body,
comment,
created_on,
database_name,
execute_as,
is_builtin,
is_secure,
language_config,
max_num_arguments,
min_num_arguments,
owner,
owner_role_type,
return_type,
schema_name
FROM snowflake.procedure.procedures
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>procedures</code> resource.

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
INSERT INTO snowflake.procedure.procedures (
data__name,
data__execute_as,
data__is_secure,
data__arguments,
data__return_type,
data__language_config,
data__comment,
data__body,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ execute_as }}',
'{{ is_secure }}',
'{{ arguments }}',
'{{ return_type }}',
'{{ language_config }}',
'{{ comment }}',
'{{ body }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.procedure.procedures (
data__name,
data__arguments,
data__return_type,
data__language_config,
data__body,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ arguments }}',
'{{ return_type }}',
'{{ language_config }}',
'{{ body }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: procedures
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__arguments
      value: string
    - name: data__body
      value: string
    - name: data__language_config
      value: string
    - name: data__name
      value: string
    - name: data__return_type
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: execute_as
      value: string
    - name: is_secure
      value: boolean
    - name: arguments
      value: array
      props:
        - name: name
          value: string
        - name: datatype
          value: string
        - name: default_value
          value: string
    - name: return_type
      props:
        - name: type
          value: string
    - name: language_config
      props:
        - name: language
          value: string
        - name: called_on_null_input
          value: boolean
    - name: comment
      value: string
    - name: body
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>procedures</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.procedure.procedures
WHERE database_name = '{{ database_name }}'
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
