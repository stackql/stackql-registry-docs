---
title: user_defined_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_defined_functions
  - user_defined_function
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

Creates, updates, deletes, gets or lists a <code>user_defined_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_defined_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.user_defined_function.user_defined_functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the UDF |
| <CopyableCode code="arguments" /> | `array` | List of arguments for the function/procedure |
| <CopyableCode code="body" /> | `string` | Function/procedure definition |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the function/procedure |
| <CopyableCode code="created_on" /> | `string` | The date and time when the function/procedure was created |
| <CopyableCode code="database_name" /> | `string` | The name of the database in which the function/procedure exists. |
| <CopyableCode code="is_aggregate" /> | `boolean` | Specifies whether the UDF is an aggregate function. Applicable only for Python language type |
| <CopyableCode code="is_builtin" /> | `boolean` | If the function/procedure is built-in or not (user-defined) |
| <CopyableCode code="is_memoizable" /> | `boolean` | Indicates whether the function is memoizable. Applicable only for Python language type. |
| <CopyableCode code="is_secure" /> | `boolean` | Specifies whether the function/procedure is secure or not |
| <CopyableCode code="is_table_function" /> | `boolean` | True if the UDF is a table function; false otherwise. |
| <CopyableCode code="is_temporary" /> | `boolean` | Specifies whether the UDF is temporary or not |
| <CopyableCode code="language_config" /> | `object` |  |
| <CopyableCode code="max_num_arguments" /> | `integer` | The maximum number of arguments |
| <CopyableCode code="min_num_arguments" /> | `integer` | The minimum number of arguments |
| <CopyableCode code="owner" /> | `string` | Role that owns the function/procedure |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the function/procedure |
| <CopyableCode code="return_type" /> | `object` |  |
| <CopyableCode code="schema_name" /> | `string` | The name of the schema in which the function/procedure exists. |
| <CopyableCode code="valid_for_clustering" /> | `boolean` | True if the UDF is valid for clustering; false otherwise. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_user_defined_function" /> | `SELECT` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | - | Fetch a UDF |
| <CopyableCode code="list_user_defined_functions" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" /> | List UDFs |
| <CopyableCode code="create_user_defined_function" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__arguments, data__language_config, data__name, data__return_type, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a UDF |
| <CopyableCode code="delete_user_defined_function" /> | `DELETE` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a UDF |
| <CopyableCode code="rename_user_defined_function" /> | `EXEC` | <CopyableCode code="database_name, nameWithArgs, schema_name, targetDatabase, targetName, targetSchema, endpoint" /> | <CopyableCode code="ifExists" /> | Rename a UDF |

<br />


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

<Tabs
    defaultValue="list_user_defined_functions"
    values={[
        { label: 'list_user_defined_functions', value: 'list_user_defined_functions' },
        { label: 'fetch_user_defined_function', value: 'fetch_user_defined_function' }
    ]
}>
<TabItem value="list_user_defined_functions">

List UDFs

```sql
SELECT
name,
arguments,
body,
comment,
created_on,
database_name,
is_aggregate,
is_builtin,
is_memoizable,
is_secure,
is_table_function,
is_temporary,
language_config,
max_num_arguments,
min_num_arguments,
owner,
owner_role_type,
return_type,
schema_name,
valid_for_clustering
FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_user_defined_function">

Fetch a UDF

```sql
SELECT
name,
arguments,
body,
comment,
created_on,
database_name,
is_aggregate,
is_builtin,
is_memoizable,
is_secure,
is_table_function,
is_temporary,
language_config,
max_num_arguments,
min_num_arguments,
owner,
owner_role_type,
return_type,
schema_name,
valid_for_clustering
FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{{ database_name }}'
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_defined_functions</code> resource.

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
INSERT INTO snowflake.user_defined_function.user_defined_functions (
data__name,
data__is_temporary,
data__is_aggregate,
data__is_memoizable,
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
'{{ is_temporary }}',
'{{ is_aggregate }}',
'{{ is_memoizable }}',
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
INSERT INTO snowflake.user_defined_function.user_defined_functions (
data__name,
data__arguments,
data__return_type,
data__language_config,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ arguments }}',
'{{ return_type }}',
'{{ language_config }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: user_defined_functions
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__arguments
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
    - name: is_temporary
      value: boolean
    - name: is_aggregate
      value: boolean
    - name: is_memoizable
      value: boolean
    - name: is_secure
      value: boolean
    - name: arguments
      value:
        - name: name
          value: string
        - name: datatype
          value: string
        - name: default_value
          value: string
    - name: return_type
      value:
        - name: type
          value: string
    - name: language_config
      value:
        - name: language
          value: string
        - name: called_on_null_input
          value: boolean
        - name: is_volatile
          value: boolean
    - name: comment
      value: string
    - name: body
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>user_defined_functions</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{{ database_name }}'
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
