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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_functions"
    values={[
        { label: 'list_functions', value: 'list_functions' },
        { label: 'fetch_function', value: 'fetch_function' }
    ]}
>
<TabItem value="list_functions">

A Snowflake function

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name for the function, must be unique for the schema in which the function is created</td>
</tr>
<tr>
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>Function&#039;s body.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the function was created.</td>
</tr>
<tr>
    <td><CopyableCode code="function_type" /></td>
    <td><code>string</code></td>
    <td> (default: service-function)</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Function&#039;s language.</td>
</tr>
<tr>
    <td><CopyableCode code="max_batch_rows" /></td>
    <td><code>integer</code></td>
    <td>Specifies the max rows for batch operation.</td>
</tr>
<tr>
    <td><CopyableCode code="returns" /></td>
    <td><code>string</code></td>
    <td>Specifies the type for the function return value. (default: TEXT)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>Function&#039;s arguments.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_function">

A Snowflake function

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name for the function, must be unique for the schema in which the function is created</td>
</tr>
<tr>
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>Function&#039;s body.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the function was created.</td>
</tr>
<tr>
    <td><CopyableCode code="function_type" /></td>
    <td><code>string</code></td>
    <td> (default: service-function)</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Function&#039;s language.</td>
</tr>
<tr>
    <td><CopyableCode code="max_batch_rows" /></td>
    <td><code>integer</code></td>
    <td>Specifies the max rows for batch operation.</td>
</tr>
<tr>
    <td><CopyableCode code="returns" /></td>
    <td><code>string</code></td>
    <td>Specifies the type for the function return value. (default: TEXT)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>Function&#039;s arguments.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list_functions"><CopyableCode code="list_functions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a></td>
    <td>Lists the user functions under the database and schema.</td>
</tr>
<tr>
    <td><a href="#fetch_function"><CopyableCode code="fetch_function" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a Function using the describe command output.</td>
</tr>
<tr>
    <td><a href="#create_function"><CopyableCode code="create_function" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create a function.</td>
</tr>
<tr>
    <td><a href="#delete_function"><CopyableCode code="delete_function" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a function with the given name and args.</td>
</tr>
<tr>
    <td><a href="#execute_function"><CopyableCode code="execute_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Execute a Function.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the <code>/api/v2/databases</code> GET request to get a list of available databases.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource.</td>
</tr>
<tr id="parameter-nameWithArgs">
    <td><CopyableCode code="nameWithArgs" /></td>
    <td><code>string</code></td>
    <td>Function's name with Args</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the <code>/api/v2/databases/&#123;database&#125;/schemas</code> GET request to get a list of available schemas for the specified database.</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_functions"
    values={[
        { label: 'list_functions', value: 'list_functions' },
        { label: 'fetch_function', value: 'fetch_function' }
    ]}
>
<TabItem value="list_functions">

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
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_function">

Fetch a Function using the describe command output.

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
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND nameWithArgs = '{{ nameWithArgs }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_function"
    values={[
        { label: 'create_function', value: 'create_function' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_function">

Create a function.

```sql
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
endpoint,
createMode
)
SELECT 
'{{ function_type }}',
'{{ name }}',
'{{ arguments }}',
'{{ returns }}',
{{ max_batch_rows }},
'{{ created_on }}',
'{{ signature }}',
'{{ language }}',
'{{ body }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: functions
  props:
    - name: database_name
      value: string
      description: Required parameter for the functions resource.
    - name: schema_name
      value: string
      description: Required parameter for the functions resource.
    - name: endpoint
      value: string
      description: Required parameter for the functions resource.
    - name: function_type
      value: string
      default: service-function
    - name: name
      value: string
      description: >
        Specifies the name for the function, must be unique for the schema in which the function is created
        
    - name: arguments
      value: array
    - name: returns
      value: string
      description: >
        Specifies the type for the function return value.
        
      valid_values: ['FIXED', 'INT', 'REAL', 'NUMBER', 'TEXT', 'BOOLEAN', 'DATE', 'TIME', 'TIMESTAMP_TZ', 'TIMESTAMP_LTZ', 'TIMESTAMP_NTZ']
      default: TEXT
    - name: max_batch_rows
      value: integer
      description: >
        Specifies the max rows for batch operation.
        
    - name: created_on
      value: string
      description: >
        Date and time when the function was created.
        
    - name: signature
      value: string
      description: >
        Function's arguments.
        
    - name: language
      value: string
      description: >
        Function's language.
        
    - name: body
      value: string
      description: >
        Function's body.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_function"
    values={[
        { label: 'delete_function', value: 'delete_function' }
    ]}
>
<TabItem value="delete_function">

Delete a function with the given name and args.

```sql
DELETE FROM snowflake.function.functions
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND nameWithArgs = '{{ nameWithArgs }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute_function"
    values={[
        { label: 'execute_function', value: 'execute_function' }
    ]}
>
<TabItem value="execute_function">

Execute a Function.

```sql
EXEC snowflake.function.functions.execute_function 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
