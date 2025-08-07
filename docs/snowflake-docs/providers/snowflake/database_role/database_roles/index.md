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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_database_roles"
    values={[
        { label: 'list_database_roles', value: 'list_database_roles' }
    ]}
>
<TabItem value="list_database_roles">

A Snowflake database role

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
    <td>Name of the database role (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>User comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the database role was created</td>
</tr>
<tr>
    <td><CopyableCode code="granted_database_roles" /></td>
    <td><code>integer (int64)</code></td>
    <td>How many database roles this database role has been granted</td>
</tr>
<tr>
    <td><CopyableCode code="granted_to_database_roles" /></td>
    <td><code>integer (int64)</code></td>
    <td>How many database roles this database role has been granted to</td>
</tr>
<tr>
    <td><CopyableCode code="granted_to_roles" /></td>
    <td><code>integer (int64)</code></td>
    <td>How many roles this database role has been granted to</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the database role (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the database role (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
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
    <td><a href="#list_database_roles"><CopyableCode code="list_database_roles" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-showLimit"><code>showLimit</code></a>, <a href="#parameter-fromName"><code>fromName</code></a></td>
    <td>List database roles</td>
</tr>
<tr>
    <td><a href="#create_database_role"><CopyableCode code="create_database_role" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create a database role</td>
</tr>
<tr>
    <td><a href="#delete_database_role"><CopyableCode code="delete_database_role" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a database role</td>
</tr>
<tr>
    <td><a href="#clone_database_role"><CopyableCode code="clone_database_role" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-targetDatabase"><code>targetDatabase</code></a></td>
    <td>Create a new database role by cloning from the specified resource</td>
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
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
<tr id="parameter-targetDatabase">
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>string</code></td>
    <td>Database of the target resource. Defaults to the source's database</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_database_roles"
    values={[
        { label: 'list_database_roles', value: 'list_database_roles' }
    ]}
>
<TabItem value="list_database_roles">

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
WHERE database_name = '{{ database_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_database_role"
    values={[
        { label: 'create_database_role', value: 'create_database_role' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_database_role">

Create a database role

```sql
INSERT INTO snowflake.database_role.database_roles (
data__name,
data__comment,
database_name,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ database_name }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: database_roles
  props:
    - name: database_name
      value: string
      description: Required parameter for the database_roles resource.
    - name: endpoint
      value: string
      description: Required parameter for the database_roles resource.
    - name: name
      value: string
      description: >
        Name of the database role
        
    - name: comment
      value: string
      description: >
        User comment associated to an object in the dictionary
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_database_role"
    values={[
        { label: 'delete_database_role', value: 'delete_database_role' }
    ]}
>
<TabItem value="delete_database_role">

Delete a database role

```sql
DELETE FROM snowflake.database_role.database_roles
WHERE database_name = '{{ database_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="clone_database_role"
    values={[
        { label: 'clone_database_role', value: 'clone_database_role' }
    ]}
>
<TabItem value="clone_database_role">

Create a new database role by cloning from the specified resource

```sql
EXEC snowflake.database_role.database_roles.clone_database_role 
@database_name='{{ database_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@targetDatabase='{{ targetDatabase }}' 
@@json=
'{
"name": "{{ name }}"
}';
```
</TabItem>
</Tabs>
