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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_user_defined_function" /> | `SELECT` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | Fetch a UDF |
| <CopyableCode code="list_user_defined_functions" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | List UDFs |
| <CopyableCode code="create_user_defined_function" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__arguments, data__language_config, data__name, data__return_type, endpoint" /> | Create a UDF |
| <CopyableCode code="delete_user_defined_function" /> | `DELETE` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | Delete a UDF |
| <CopyableCode code="rename_user_defined_function" /> | `EXEC` | <CopyableCode code="database_name, nameWithArgs, schema_name, targetDatabase, targetName, targetSchema, endpoint" /> | Rename a UDF |

## `SELECT` examples

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
WHERE database_name = '{{ database_name }}' AND schema_name = '{{ schema_name }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_defined_functions</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.user_defined_function.user_defined_functions (
data__return_type,
endpoint,
schema_name,
data__arguments,
data__language_config,
database_name,
data__name
)
SELECT 
'{ language_config }',
'{ database_name }',
'{ name }',
'{ schema_name }',
'{ arguments }',
'{ endpoint }',
'{ return_type }'
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>user_defined_functions</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{ database_name }' AND nameWithArgs = '{ nameWithArgs }' AND schema_name = '{ schema_name }' AND endpoint = '{ endpoint }';
```
