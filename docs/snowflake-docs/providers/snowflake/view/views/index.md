--- 
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - view
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.view.views" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_views"
    values={[
        { label: 'list_views', value: 'list_views' },
        { label: 'fetch_view', value: 'fetch_view' }
    ]}
>
<TabItem value="list_views">

A Snowflake view

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
    <td>Name of the view</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the view is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the view is stored</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td>The columns of the view</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the view was created.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the view, permanent (default) or temporary</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the view</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the view</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>Query used to create the view</td>
</tr>
<tr>
    <td><CopyableCode code="recursive" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this view can refer to itself using recursive syntax withot requiring a CTE (common table expression)</td>
</tr>
<tr>
    <td><CopyableCode code="secure" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this view is secure</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_view">

A Snowflake view

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
    <td>Name of the view</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the view is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the view is stored</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td>The columns of the view</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the view was created.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the view, permanent (default) or temporary</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the view</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the view</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>Query used to create the view</td>
</tr>
<tr>
    <td><CopyableCode code="recursive" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this view can refer to itself using recursive syntax withot requiring a CTE (common table expression)</td>
</tr>
<tr>
    <td><CopyableCode code="secure" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this view is secure</td>
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
    <td><a href="#list_views"><CopyableCode code="list_views" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a>, <a href="#parameter-startsWith"><code>startsWith</code></a>, <a href="#parameter-showLimit"><code>showLimit</code></a>, <a href="#parameter-fromName"><code>fromName</code></a>, <a href="#parameter-deep"><code>deep</code></a></td>
    <td>List views</td>
</tr>
<tr>
    <td><a href="#fetch_view"><CopyableCode code="fetch_view" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a view</td>
</tr>
<tr>
    <td><a href="#create_view"><CopyableCode code="create_view" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a></td>
    <td>Create a view</td>
</tr>
<tr>
    <td><a href="#delete_view"><CopyableCode code="delete_view" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a view</td>
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
<tr id="parameter-deep">
    <td><CopyableCode code="deep" /></td>
    <td><code>boolean</code></td>
    <td>Optionally includes dependency information of the view.</td>
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
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters.</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_views"
    values={[
        { label: 'list_views', value: 'list_views' },
        { label: 'fetch_view', value: 'fetch_view' }
    ]}
>
<TabItem value="list_views">

List views

```sql
SELECT
name,
database_name,
schema_name,
columns,
comment,
created_on,
kind,
owner,
owner_role_type,
query,
recursive,
secure
FROM snowflake.view.views
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}'
AND deep = '{{ deep }}';
```
</TabItem>
<TabItem value="fetch_view">

Fetch a view

```sql
SELECT
name,
database_name,
schema_name,
columns,
comment,
created_on,
kind,
owner,
owner_role_type,
query,
recursive,
secure
FROM snowflake.view.views
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_view"
    values={[
        { label: 'create_view', value: 'create_view' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_view">

Create a view

```sql
INSERT INTO snowflake.view.views (
data__name,
data__secure,
data__kind,
data__recursive,
data__columns,
data__comment,
data__query,
database_name,
schema_name,
endpoint,
createMode,
copyGrants
)
SELECT 
'{{ name }}',
{{ secure }},
'{{ kind }}',
{{ recursive }},
'{{ columns }}',
'{{ comment }}',
'{{ query }}',
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
- name: views
  props:
    - name: database_name
      value: string
      description: Required parameter for the views resource.
    - name: schema_name
      value: string
      description: Required parameter for the views resource.
    - name: endpoint
      value: string
      description: Required parameter for the views resource.
    - name: name
      value: string
      description: >
        Name of the view
        
    - name: secure
      value: boolean
      description: >
        Whether or not this view is secure
        
    - name: kind
      value: string
      description: >
        Kind of the view, permanent (default) or temporary
        
      valid_values: ['PERMANENT', 'TEMPORARY']
    - name: recursive
      value: boolean
      description: >
        Whether or not this view can refer to itself using recursive syntax withot requiring a CTE (common table expression)
        
    - name: columns
      value: array
      description: >
        The columns of the view
        
    - name: comment
      value: string
      description: >
        user comment associated to an object in the dictionary
        
    - name: query
      value: string
      description: >
        Query used to create the view
        
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
    defaultValue="delete_view"
    values={[
        { label: 'delete_view', value: 'delete_view' }
    ]}
>
<TabItem value="delete_view">

Delete a view

```sql
DELETE FROM snowflake.view.views
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>
