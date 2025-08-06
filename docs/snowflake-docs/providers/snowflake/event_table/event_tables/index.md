--- 
title: event_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - event_tables
  - event_table
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

Creates, updates, deletes, gets or lists an <code>event_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.event_table.event_tables" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_event_tables"
    values={[
        { label: 'list_event_tables', value: 'list_event_tables' },
        { label: 'fetch_event_table', value: 'fetch_event_table' }
    ]}
>
<TabItem value="list_event_tables">

A Snowflake event table

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
    <td>Name of the event table</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the event table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the event table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_clustering" /></td>
    <td><code>boolean</code></td>
    <td>If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table.</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of bytes that will be scanned if the entire table is scanned in a query.Note that this number may be different than the number of actual physical bytes stored on-disk for the table</td>
</tr>
<tr>
    <td><CopyableCode code="change_tracking" /></td>
    <td><code>boolean</code></td>
    <td>True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Cluster key column(s) or expression</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the event table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>number of days to retain the old version of deleted/updated data</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Collation that is used for all the new columns created by the DDL statements (if not specified)</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the event table</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the event table</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the table.</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization" /></td>
    <td><code>boolean</code></td>
    <td>If ON, the table has the search optimization service enabled</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of additional bytes of storage that the search optimization service consumes for this table</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_progress" /></td>
    <td><code>integer (int64)</code></td>
    <td>Percentage of the table that has been optimized for search</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_event_table">

A Snowflake event table

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
    <td>Name of the event table</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the event table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the event table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_clustering" /></td>
    <td><code>boolean</code></td>
    <td>If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table.</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of bytes that will be scanned if the entire table is scanned in a query.Note that this number may be different than the number of actual physical bytes stored on-disk for the table</td>
</tr>
<tr>
    <td><CopyableCode code="change_tracking" /></td>
    <td><code>boolean</code></td>
    <td>True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Cluster key column(s) or expression</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the event table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>number of days to retain the old version of deleted/updated data</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Collation that is used for all the new columns created by the DDL statements (if not specified)</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the event table</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the event table</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the table.</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization" /></td>
    <td><code>boolean</code></td>
    <td>If ON, the table has the search optimization service enabled</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of additional bytes of storage that the search optimization service consumes for this table</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_progress" /></td>
    <td><code>integer (int64)</code></td>
    <td>Percentage of the table that has been optimized for search</td>
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
    <td><a href="#list_event_tables"><CopyableCode code="list_event_tables" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a></td>
    <td>List event tables</td>
</tr>
<tr>
    <td><a href="#fetch_event_table"><CopyableCode code="fetch_event_table" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch an event table</td>
</tr>
<tr>
    <td><a href="#create_event_table"><CopyableCode code="create_event_table" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create an event table</td>
</tr>
<tr>
    <td><a href="#delete_event_table"><CopyableCode code="delete_event_table" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete an event table</td>
</tr>
<tr>
    <td><a href="#rename_event_table"><CopyableCode code="rename_event_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-targetName">targetName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Rename the event table</td>
</tr>
</tbody>
</table>## Parameters

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
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/{database}/schemas` GET request to get a list of available schemas for the specified database. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetName">
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>Specify the name of the target resource to be renamed to.</td>
</tr>
<tr id="parameter-copyGrants">
    <td><CopyableCode code="copyGrants" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter to enable copy grants when creating the object. (example: false, default: false)</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. (example: from_test)</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. (example: true, default: false)</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command. (example: 10, minimum: 1, maximum: 10000)</td>
</tr>
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. (example: test)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_event_tables"
    values={[
        { label: 'list_event_tables', value: 'list_event_tables' },
        { label: 'fetch_event_table', value: 'fetch_event_table' }
    ]}
>
<TabItem value="list_event_tables">

List event tables

```sql
SELECT
name,
database_name,
schema_name,
automatic_clustering,
bytes,
change_tracking,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
default_ddl_collation,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
search_optimization,
search_optimization_bytes,
search_optimization_progress
FROM snowflake.event_table.event_tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}';
```
</TabItem>
<TabItem value="fetch_event_table">

Fetch an event table

```sql
SELECT
name,
database_name,
schema_name,
automatic_clustering,
bytes,
change_tracking,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
default_ddl_collation,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
search_optimization,
search_optimization_bytes,
search_optimization_progress
FROM snowflake.event_table.event_tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_event_table"
    values={[
        { label: 'create_event_table', value: 'create_event_table' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_event_table">

Create an event table

```sql
INSERT INTO snowflake.event_table.event_tables (
data__name,
data__cluster_by,
data__data_retention_time_in_days,
data__max_data_extension_time_in_days,
data__change_tracking,
data__default_ddl_collation,
data__comment,
database_name,
schema_name,
endpoint,
createMode,
copyGrants
)
SELECT 
'{{ name }}',
'{{ cluster_by }}',
{{ data_retention_time_in_days }},
{{ max_data_extension_time_in_days }},
{{ change_tracking }},
'{{ default_ddl_collation }}',
'{{ comment }}',
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
- name: event_tables
  props:
    - name: database_name
      value: string
      description: Required parameter for the event_tables resource.
    - name: schema_name
      value: string
      description: Required parameter for the event_tables resource.
    - name: endpoint
      value: string
      description: Required parameter for the event_tables resource.
    - name: name
      value: string
      description: >
        Name of the event table
        
    - name: cluster_by
      value: array
      description: >
        Cluster key column(s) or expression
        
    - name: data_retention_time_in_days
      value: integer
      description: >
        number of days to retain the old version of deleted/updated data
        
    - name: max_data_extension_time_in_days
      value: integer
      description: >
        Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.
        
    - name: change_tracking
      value: boolean
      description: >
        True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.
        
    - name: default_ddl_collation
      value: string
      description: >
        Collation that is used for all the new columns created by the DDL statements (if not specified)
        
    - name: comment
      value: string
      description: >
        user comment associated to an object in the dictionary
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
    - name: copyGrants
      value: boolean
      description: Query parameter to enable copy grants when creating the object. (example: false, default: false)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_event_table"
    values={[
        { label: 'delete_event_table', value: 'delete_event_table' }
    ]}
>
<TabItem value="delete_event_table">

Delete an event table

```sql
DELETE FROM snowflake.event_table.event_tables
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_event_table"
    values={[
        { label: 'rename_event_table', value: 'rename_event_table' }
    ]}
>
<TabItem value="rename_event_table">

Rename the event table

```sql
EXEC snowflake.event_table.event_tables.rename_event_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@targetName='{{ targetName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
</Tabs>
