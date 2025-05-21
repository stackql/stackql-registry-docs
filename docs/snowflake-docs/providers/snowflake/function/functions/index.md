---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
  - function
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

Creates, updates, deletes, gets or lists a <code>functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.function.functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Specifies the name for the function, must be unique for the schema in which the function is created |
| <CopyableCode code="arguments" /> | `array` |  |
| <CopyableCode code="body" /> | `string` | Function's body. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the function was created. |
| <CopyableCode code="function_type" /> | `string` |  |
| <CopyableCode code="language" /> | `string` | Function's language. |
| <CopyableCode code="max_batch_rows" /> | `integer` | Specifies the max rows for batch operation. |
| <CopyableCode code="returns" /> | `string` | Specifies the type for the function return value. |
| <CopyableCode code="signature" /> | `string` | Function's arguments. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_function" /> | `SELECT` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | Fetch a Function using the describe command output. |
| <CopyableCode code="list_functions" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | Lists the user functions under the database and schema. |
| <CopyableCode code="create_function" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__arguments, data__name, endpoint" /> | Create a function. |
| <CopyableCode code="delete_function" /> | `DELETE` | <CopyableCode code="database_name, nameWithArgs, schema_name, endpoint" /> | Delete a function with the given name and args. |
| <CopyableCode code="execute_function" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Execute a Function. |

## `SELECT` examples

Lists the user functions under the database and schema.


```sql
SELECT
name,
arguments,
body,
created_on,
function_type,
language,
max_batch_rows,
returns,
signature
FROM snowflake.function.functions
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>functions</code> resource.

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
INSERT INTO snowflake.function.functions (
data__function_type,
data__name,
data__arguments,
data__returns,
data__max_batch_rows,
data__created_on,
data__signature,
data__language,
data__body,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ function_type }}',
'{{ name }}',
'{{ arguments }}',
'{{ returns }}',
'{{ max_batch_rows }}',
'{{ created_on }}',
'{{ signature }}',
'{{ language }}',
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
INSERT INTO snowflake.function.functions (
data__name,
data__arguments,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ arguments }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: functions
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__arguments
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: function_type
      value: string
    - name: name
      value: string
    - name: arguments
      value: array
      props:
        - name: name
          value: string
        - name: datatype
          value: string
        - name: value
          value: string
    - name: returns
      value: string
    - name: max_batch_rows
      value: integer
    - name: created_on
      value: string
    - name: signature
      value: string
    - name: language
      value: string
    - name: body
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>functions</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.function.functions
WHERE database_name = '{{ database_name }}'
AND nameWithArgs = '{{ nameWithArgs }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
