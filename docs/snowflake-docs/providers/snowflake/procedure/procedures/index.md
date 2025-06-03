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
    defaultValue="list_procedures"
    values={[
        { label: 'list_procedures', value: 'list_procedures' },
        { label: 'fetch_procedure', value: 'fetch_procedure' }
    ]
}>
<TabItem value="list_procedures">

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
</TabItem>
<TabItem value="fetch_procedure">

Fetch a procedure

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
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

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
# Description fields below are for documentation purposes only and are not required in the manifest
- name: procedures
  props:
    - name: database_name
      value: string
      description: Required parameter for the procedures resource.
    - name: schema_name
      value: string
      description: Required parameter for the procedures resource.
    - name: endpoint
      value: string
      description: Required parameter for the procedures resource.
    - name: name
      value: string
      description: Name of the procedure
    - name: execute_as
      value: string
      description: >-
        What permissions should the procedure execution be called with (valid
        values: 'CALLER', 'OWNER')
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
      description: List of arguments for the function/procedure
    - name: return_type
      value:
        - name: type
          value: string
          description: Type of the return, can be either DATATYPE or TABLE
    - name: language_config
      value:
        - name: language
          value: string
          description: >-
            Language that the function/procedure is written in. Possible values
            include: JAVA, JAVASCRIPT, PYTHON, SCALA, SQL
        - name: called_on_null_input
          value: boolean
          description: Decide if the function/procedure can receive null input
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

Deletes the specified <code>procedures</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.procedure.procedures
WHERE database_name = '{{ database_name }}'
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
