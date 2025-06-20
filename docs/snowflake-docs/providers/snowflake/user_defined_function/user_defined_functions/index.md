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

Create a UDF

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
{{ is_temporary }},
{{ is_aggregate }},
{{ is_memoizable }},
{{ is_secure }},
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
# Description fields below are for documentation purposes only and are not required in the manifest
- name: user_defined_functions
  props:
    - name: database_name
      value: string
      description: Required parameter for the user_defined_functions resource.
    - name: schema_name
      value: string
      description: Required parameter for the user_defined_functions resource.
    - name: endpoint
      value: string
      description: Required parameter for the user_defined_functions resource.
    - name: name
      value: string
      description: >-
        The name of the UDF (Required parameter for the user_defined_functions
        resource.)
    - name: is_temporary
      value: boolean
      description: Specifies whether the UDF is temporary or not
    - name: is_aggregate
      value: boolean
      description: >-
        Specifies whether the UDF is an aggregate function. Applicable only for
        Python language type
    - name: is_memoizable
      value: boolean
      description: >-
        Indicates whether the function is memoizable. Applicable only for Python
        language type.
    - name: is_secure
      value: boolean
      description: Specifies whether the function/procedure is secure or not
    - name: arguments
      value:
        - name: name
          value: string
          description: Argument name
        - name: datatype
          value: string
          description: >-
            Argument data type (valid values: 'ARRAY', 'BIGINT', 'BINARY',
            'BOOLEAN', 'BYTEINT', 'CHAR', 'CHARACTER', 'DATE', 'DATETIME',
            'DECIMAL', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT', 'FLOAT4',
            'FLOAT8', 'GEOGRAPHY', 'GEOMETRY', 'INT', 'INTEGER', 'NUMBER',
            'NUMERIC', 'OBJECT', 'REAL', 'STRING', 'SMALLINT', 'TEXT', 'TIME',
            'TIMESTAMP_LTZ', 'TIMESTAMP_NTZ', 'TIMESTAMP_TZ', 'TINYINT',
            'VARBINARY', 'VARCHAR', 'VARIANT', 'VECTOR')
        - name: default_value
          value: string
          description: Default value of the argument
      description: >-
        List of arguments for the function/procedure (Required parameter for the
        user_defined_functions resource.)
    - name: return_type
      value:
        type: string
      description: Required parameter for the user_defined_functions resource.
    - name: language_config
      value:
        language: string
        called_on_null_input: boolean
        is_volatile: boolean
      description: Required parameter for the user_defined_functions resource.
    - name: comment
      value: string
      description: Specifies a comment for the function/procedure
    - name: body
      value: string
      description: Function/procedure definition
```
</TabItem>
</Tabs>

## `DELETE` example

Delete a UDF

```sql
/*+ delete */
DELETE FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{{ database_name }}'
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
