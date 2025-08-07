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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_procedures"
    values={[
        { label: 'list_procedures', value: 'list_procedures' },
        { label: 'fetch_procedure', value: 'fetch_procedure' }
    ]}
>
<TabItem value="list_procedures">

A Snowflake procedure

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
    <td>Name of the procedure (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
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
    <td><CopyableCode code="execute_as" /></td>
    <td><code>string</code></td>
    <td>What permissions should the procedure execution be called with</td>
</tr>
<tr>
    <td><CopyableCode code="is_builtin" /></td>
    <td><code>boolean</code></td>
    <td>If the function/procedure is built-in or not (user-defined)</td>
</tr>
<tr>
    <td><CopyableCode code="is_secure" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the function/procedure is secure or not</td>
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
    <td>Role that owns the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="return_type" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_procedure">

A Snowflake procedure

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
    <td>Name of the procedure (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
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
    <td><CopyableCode code="execute_as" /></td>
    <td><code>string</code></td>
    <td>What permissions should the procedure execution be called with</td>
</tr>
<tr>
    <td><CopyableCode code="is_builtin" /></td>
    <td><code>boolean</code></td>
    <td>If the function/procedure is built-in or not (user-defined)</td>
</tr>
<tr>
    <td><CopyableCode code="is_secure" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the function/procedure is secure or not</td>
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
    <td>Role that owns the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the function/procedure</td>
</tr>
<tr>
    <td><CopyableCode code="return_type" /></td>
    <td><code>object</code></td>
    <td></td>
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
    <td><a href="#list_procedures"><CopyableCode code="list_procedures" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a></td>
    <td>List procedures</td>
</tr>
<tr>
    <td><a href="#fetch_procedure"><CopyableCode code="fetch_procedure" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a procedure</td>
</tr>
<tr>
    <td><a href="#create_procedure"><CopyableCode code="create_procedure" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a></td>
    <td>Create a procedure</td>
</tr>
<tr>
    <td><a href="#delete_procedure"><CopyableCode code="delete_procedure" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a procedure</td>
</tr>
<tr>
    <td><a href="#call_procedure"><CopyableCode code="call_procedure" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-nameWithArgs"><code>nameWithArgs</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Call a procedure</td>
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
    defaultValue="list_procedures"
    values={[
        { label: 'list_procedures', value: 'list_procedures' },
        { label: 'fetch_procedure', value: 'fetch_procedure' }
    ]}
>
<TabItem value="list_procedures">

List procedures

```sql
SELECT
name,
database_name,
schema_name,
arguments,
body,
comment,
created_on,
execute_as,
is_builtin,
is_secure,
language_config,
max_num_arguments,
min_num_arguments,
owner,
owner_role_type,
return_type
FROM snowflake.procedure.procedures
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_procedure">

Fetch a procedure

```sql
SELECT
name,
database_name,
schema_name,
arguments,
body,
comment,
created_on,
execute_as,
is_builtin,
is_secure,
language_config,
max_num_arguments,
min_num_arguments,
owner,
owner_role_type,
return_type
FROM snowflake.procedure.procedures
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND nameWithArgs = '{{ nameWithArgs }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_procedure"
    values={[
        { label: 'create_procedure', value: 'create_procedure' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_procedure">

Create a procedure

```sql
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
endpoint,
createMode,
copyGrants
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
'{{ endpoint }}',
'{{ createMode }}',
'{{ copyGrants }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
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
      description: >
        Name of the procedure
        
    - name: execute_as
      value: string
      description: >
        What permissions should the procedure execution be called with
        
      valid_values: ['CALLER', 'OWNER']
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
    defaultValue="delete_procedure"
    values={[
        { label: 'delete_procedure', value: 'delete_procedure' }
    ]}
>
<TabItem value="delete_procedure">

Delete a procedure

```sql
DELETE FROM snowflake.procedure.procedures
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
    defaultValue="call_procedure"
    values={[
        { label: 'call_procedure', value: 'call_procedure' }
    ]}
>
<TabItem value="call_procedure">

Call a procedure

```sql
EXEC snowflake.procedure.procedures.call_procedure 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@nameWithArgs='{{ nameWithArgs }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"call_arguments": "{{ call_arguments }}"
}';
```
</TabItem>
</Tabs>
