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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_user_defined_functions"
    values={[
        { label: 'list_user_defined_functions', value: 'list_user_defined_functions' },
        { label: 'fetch_user_defined_function', value: 'fetch_user_defined_function' }
    ]}
>
<TabItem value="list_user_defined_functions">

A snowflake UDF

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
    <td>The name of the UDF (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database in which the function/procedure exists. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the schema in which the function/procedure exists. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td>List of arguments for the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>Function/procedure definition</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the function/procedure was created</td>
</tr>
<tr>
    <td><CopyableCode code="is_aggregate" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the UDF is an aggregate function. Applicable only for Python language type</td>
</tr>
<tr>
    <td><CopyableCode code="is_builtin" /></td>
    <td><code>boolean</code></td>
    <td>If the function/procedure is built-in or not (user-defined)</td>
</tr>
<tr>
    <td><CopyableCode code="is_memoizable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the function is memoizable. Applicable only for Python language type.</td>
</tr>
<tr>
    <td><CopyableCode code="is_secure" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the function/procedure is secure or not</td>
</tr>
<tr>
    <td><CopyableCode code="is_table_function" /></td>
    <td><code>boolean</code></td>
    <td>True if the UDF is a table function; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="is_temporary" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the UDF is temporary or not</td>
</tr>
<tr>
    <td><CopyableCode code="language_config" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_num_arguments" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of arguments</td>
</tr>
<tr>
    <td><CopyableCode code="min_num_arguments" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of arguments</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the function/procedure (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the function/procedure (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="return_type" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="valid_for_clustering" /></td>
    <td><code>boolean</code></td>
    <td>True if the UDF is valid for clustering; false otherwise.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_user_defined_function">

A snowflake UDF

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
    <td>The name of the UDF (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database in which the function/procedure exists. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the schema in which the function/procedure exists. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td>List of arguments for the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>Function/procedure definition</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the function/procedure was created</td>
</tr>
<tr>
    <td><CopyableCode code="is_aggregate" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the UDF is an aggregate function. Applicable only for Python language type</td>
</tr>
<tr>
    <td><CopyableCode code="is_builtin" /></td>
    <td><code>boolean</code></td>
    <td>If the function/procedure is built-in or not (user-defined)</td>
</tr>
<tr>
    <td><CopyableCode code="is_memoizable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the function is memoizable. Applicable only for Python language type.</td>
</tr>
<tr>
    <td><CopyableCode code="is_secure" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the function/procedure is secure or not</td>
</tr>
<tr>
    <td><CopyableCode code="is_table_function" /></td>
    <td><code>boolean</code></td>
    <td>True if the UDF is a table function; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="is_temporary" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the UDF is temporary or not</td>
</tr>
<tr>
    <td><CopyableCode code="language_config" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_num_arguments" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of arguments</td>
</tr>
<tr>
    <td><CopyableCode code="min_num_arguments" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of arguments</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the function/procedure (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the function/procedure (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="return_type" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="valid_for_clustering" /></td>
    <td><code>boolean</code></td>
    <td>True if the UDF is valid for clustering; false otherwise.</td>
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
    <td><a href="#list_user_defined_functions"><CopyableCode code="list_user_defined_functions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a></td>
    <td>List UDFs</td>
</tr>
<tr>
    <td><a href="#fetch_user_defined_function"><CopyableCode code="fetch_user_defined_function" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a UDF</td>
</tr>
<tr>
    <td><a href="#create_user_defined_function"><CopyableCode code="create_user_defined_function" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a></td>
    <td>Create a UDF</td>
</tr>
<tr>
    <td><a href="#delete_user_defined_function"><CopyableCode code="delete_user_defined_function" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a UDF</td>
</tr>
<tr>
    <td><a href="#rename_user_defined_function"><CopyableCode code="rename_user_defined_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-targetDatabase"><code>targetDatabase</code></a>, <a href="#parameter-targetSchema"><code>targetSchema</code></a>, <a href="#parameter-targetName"><code>targetName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Rename a UDF</td>
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
<tr id="parameter-targetDatabase">
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>string</code></td>
    <td>Database of the target resource. Defaults to the source's database</td>
</tr>
<tr id="parameter-targetName">
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>Name of the target resource.</td>
</tr>
<tr id="parameter-targetSchema">
    <td><CopyableCode code="targetSchema" /></td>
    <td><code>string</code></td>
    <td>Schema of the target resource. Defaults to the source's schema</td>
</tr>
<tr id="parameter-copyGrants">
    <td><CopyableCode code="copyGrants" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter to enable copy grants when creating the object.</td>
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
    defaultValue="list_user_defined_functions"
    values={[
        { label: 'list_user_defined_functions', value: 'list_user_defined_functions' },
        { label: 'fetch_user_defined_function', value: 'fetch_user_defined_function' }
    ]}
>
<TabItem value="list_user_defined_functions">

List UDFs

```sql
SELECT
name,
database_name,
schema_name,
arguments,
body,
comment,
created_on,
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
valid_for_clustering
FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_user_defined_function">

Fetch a UDF

```sql
SELECT
name,
database_name,
schema_name,
arguments,
body,
comment,
created_on,
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
valid_for_clustering
FROM snowflake.user_defined_function.user_defined_functions
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND nameWithArgs = '{{ nameWithArgs }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_user_defined_function"
    values={[
        { label: 'create_user_defined_function', value: 'create_user_defined_function' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_user_defined_function">

Create a UDF

```sql
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
endpoint,
createMode,
copyGrants
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
'{{ endpoint }}',
'{{ createMode }}',
'{{ copyGrants }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
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
      description: >
        The name of the UDF
        
    - name: is_temporary
      value: boolean
      description: >
        Specifies whether the UDF is temporary or not
        
    - name: is_aggregate
      value: boolean
      description: >
        Specifies whether the UDF is an aggregate function. Applicable only for Python language type
        
    - name: is_memoizable
      value: boolean
      description: >
        Indicates whether the function is memoizable. Applicable only for Python language type.
        
    - name: is_secure
      value: boolean
      description: >
        Specifies whether the function/procedure is secure or not
        
    - name: arguments
      value: array
      description: >
        List of arguments for the function/procedure
        
    - name: return_type
      value: object
    - name: language_config
      value: object
    - name: comment
      value: string
      description: >
        Specifies a comment for the function/procedure
        
    - name: body
      value: string
      description: >
        Function/procedure definition
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
    - name: copyGrants
      value: boolean
      description: Query parameter to enable copy grants when creating the object.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_user_defined_function"
    values={[
        { label: 'delete_user_defined_function', value: 'delete_user_defined_function' }
    ]}
>
<TabItem value="delete_user_defined_function">

Delete a UDF

```sql
DELETE FROM snowflake.user_defined_function.user_defined_functions
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
    defaultValue="rename_user_defined_function"
    values={[
        { label: 'rename_user_defined_function', value: 'rename_user_defined_function' }
    ]}
>
<TabItem value="rename_user_defined_function">

Rename a UDF

```sql
EXEC snowflake.user_defined_function.user_defined_functions.rename_user_defined_function 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@nameWithArgs='{{ nameWithArgs }}' --required, 
@targetDatabase='{{ targetDatabase }}' --required, 
@targetSchema='{{ targetSchema }}' --required, 
@targetName='{{ targetName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
</Tabs>
