--- 
title: dynamic_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - dynamic_tables
  - dynamic_table
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

Creates, updates, deletes, gets or lists a <code>dynamic_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dynamic_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.dynamic_table.dynamic_tables" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_dynamic_tables"
    values={[
        { label: 'list_dynamic_tables', value: 'list_dynamic_tables' },
        { label: 'fetch_dynamic_table', value: 'fetch_dynamic_table' }
    ]}
>
<TabItem value="list_dynamic_tables">

A Snowflake dynamic table object.

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
    <td>Specifies the name for the dynamic table, must be unique for the schema in which the dynamic table is created</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the dynamic table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the dynamic table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_clustering" /></td>
    <td><code>boolean</code></td>
    <td>If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the object is monitored by a budget</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more columns or column expressions in the dynamic table as the clustering key</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the dynamic table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="initialize" /></td>
    <td><code>string</code></td>
    <td>Specifies the behavior of the initial refresh of the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Specifies the dynamic table type, permanent (default) or transient. (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the table</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the object.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>Specifies the query whose results the dynamic table should contain (example: SELECT * FROM foo)</td>
</tr>
<tr>
    <td><CopyableCode code="refresh_mode" /></td>
    <td><code>string</code></td>
    <td>Specifies the refresh type for the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduling_state" /></td>
    <td><code>string</code></td>
    <td>Scheduling state (RUNNING or SUSPENDED)</td>
</tr>
<tr>
    <td><CopyableCode code="target_lag" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically refreshing the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table (example: test_wh)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_dynamic_table">

A Snowflake dynamic table object.

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
    <td>Specifies the name for the dynamic table, must be unique for the schema in which the dynamic table is created</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the dynamic table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the dynamic table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_clustering" /></td>
    <td><code>boolean</code></td>
    <td>If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the object is monitored by a budget</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more columns or column expressions in the dynamic table as the clustering key</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the dynamic table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="initialize" /></td>
    <td><code>string</code></td>
    <td>Specifies the behavior of the initial refresh of the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Specifies the dynamic table type, permanent (default) or transient. (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the table</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the object.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>Specifies the query whose results the dynamic table should contain (example: SELECT * FROM foo)</td>
</tr>
<tr>
    <td><CopyableCode code="refresh_mode" /></td>
    <td><code>string</code></td>
    <td>Specifies the refresh type for the dynamic table</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduling_state" /></td>
    <td><code>string</code></td>
    <td>Scheduling state (RUNNING or SUSPENDED)</td>
</tr>
<tr>
    <td><CopyableCode code="target_lag" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically refreshing the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table (example: test_wh)</td>
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
    <td><a href="#list_dynamic_tables"><CopyableCode code="list_dynamic_tables" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a>, <a href="#parameter-deep">deep</a></td>
    <td>Lists the dynamic tables under the database and schema.</td>
</tr>
<tr>
    <td><a href="#fetch_dynamic_table"><CopyableCode code="fetch_dynamic_table" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch a Dynamic Table.</td>
</tr>
<tr>
    <td><a href="#create_dynamic_table"><CopyableCode code="create_dynamic_table" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create a dynamic table, with standard create modifiers as query parameters. See the Dynamic Table component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#delete_dynamic_table"><CopyableCode code="delete_dynamic_table" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete a dynamic table with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#clone_dynamic_table"><CopyableCode code="clone_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a>, <a href="#parameter-targetDatabase">targetDatabase</a>, <a href="#parameter-targetSchema">targetSchema</a></td>
    <td>Create a new dynamic table by cloning from the specified resource</td>
</tr>
<tr>
    <td><a href="#undrop_dynamic_table"><CopyableCode code="undrop_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Undrop specified dynamic table</td>
</tr>
<tr>
    <td><a href="#suspend_dynamic_table"><CopyableCode code="suspend_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Suspend refreshes on the dynamic table</td>
</tr>
<tr>
    <td><a href="#resume_dynamic_table"><CopyableCode code="resume_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Resume refreshes on the dynamic table</td>
</tr>
<tr>
    <td><a href="#refresh_dynamic_table"><CopyableCode code="refresh_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Specifies that the dynamic table should be manually refreshed</td>
</tr>
<tr>
    <td><a href="#suspend_recluster_dynamic_table"><CopyableCode code="suspend_recluster_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Suspend recluster of a dynamic table</td>
</tr>
<tr>
    <td><a href="#resume_recluster_dynamic_table"><CopyableCode code="resume_recluster_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Resume recluster of a dynamic table</td>
</tr>
<tr>
    <td><a href="#swap_with_dynamic_table"><CopyableCode code="swap_with_dynamic_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-targetName">targetName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a>, <a href="#parameter-targetDatabase">targetDatabase</a>, <a href="#parameter-targetSchema">targetSchema</a></td>
    <td>Swap with another dynamic table</td>
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
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/{database}/schemas` GET request to get a list of available schemas for the specified database. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetName">
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>The name of the target dynamic table to be swapped with. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
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
<tr id="parameter-deep">
    <td><CopyableCode code="deep" /></td>
    <td><code>boolean</code></td>
    <td>Optionally includes dependency information of the dynamic table.</td>
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
<tr id="parameter-targetDatabase">
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>string</code></td>
    <td>Database of the target dynamic table. Defaults to the source table's database. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetSchema">
    <td><CopyableCode code="targetSchema" /></td>
    <td><code>string</code></td>
    <td>Schema of the target dynamic table. Defaults to the source table's schema. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_dynamic_tables"
    values={[
        { label: 'list_dynamic_tables', value: 'list_dynamic_tables' },
        { label: 'fetch_dynamic_table', value: 'fetch_dynamic_table' }
    ]}
>
<TabItem value="list_dynamic_tables">

Lists the dynamic tables under the database and schema.

```sql
SELECT
name,
database_name,
schema_name,
automatic_clustering,
budget,
bytes,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
initialize,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
query,
refresh_mode,
rows,
scheduling_state,
target_lag,
warehouse
FROM snowflake.dynamic_table.dynamic_tables
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
<TabItem value="fetch_dynamic_table">

Fetch a Dynamic Table.

```sql
SELECT
name,
database_name,
schema_name,
automatic_clustering,
budget,
bytes,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
initialize,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
query,
refresh_mode,
rows,
scheduling_state,
target_lag,
warehouse
FROM snowflake.dynamic_table.dynamic_tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_dynamic_table"
    values={[
        { label: 'create_dynamic_table', value: 'create_dynamic_table' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_dynamic_table">

Create a dynamic table, with standard create modifiers as query parameters. See the Dynamic Table component definition for what is required to be provided in the request body.

```sql
INSERT INTO snowflake.dynamic_table.dynamic_tables (
data__name,
data__kind,
data__columns,
data__target_lag,
data__refresh_mode,
data__initialize,
data__warehouse,
data__cluster_by,
data__query,
data__data_retention_time_in_days,
data__max_data_extension_time_in_days,
data__comment,
database_name,
schema_name,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ columns }}',
'{{ target_lag }}',
'{{ refresh_mode }}',
'{{ initialize }}',
'{{ warehouse }}',
'{{ cluster_by }}',
'{{ query }}',
{{ data_retention_time_in_days }},
{{ max_data_extension_time_in_days }},
'{{ comment }}',
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
- name: dynamic_tables
  props:
    - name: database_name
      value: string
      description: Required parameter for the dynamic_tables resource.
    - name: schema_name
      value: string
      description: Required parameter for the dynamic_tables resource.
    - name: endpoint
      value: string
      description: Required parameter for the dynamic_tables resource.
    - name: name
      value: string
      description: >
        Specifies the name for the dynamic table, must be unique for the schema in which the dynamic table is created
        
    - name: kind
      value: string
      description: >
        Specifies the dynamic table type, permanent (default) or transient.
        
      valid_values: ['PERMANENT', 'TRANSIENT']
      default: PERMANENT
    - name: columns
      value: array
    - name: target_lag
      value: object
      description: >
        Specifies the schedule for periodically refreshing the dynamic table.
        
    - name: refresh_mode
      value: string
      description: >
        Specifies the refresh type for the dynamic table
        
      valid_values: ['AUTO', 'FULL', 'INCREMENTAL']
    - name: initialize
      value: string
      description: >
        Specifies the behavior of the initial refresh of the dynamic table
        
      valid_values: ['ON_CREATE', 'ON_SCHEDULE']
    - name: warehouse
      value: string
      description: >
        Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table
        
    - name: cluster_by
      value: array
      description: >
        Specifies one or more columns or column expressions in the dynamic table as the clustering key
        
    - name: query
      value: string
      description: >
        Specifies the query whose results the dynamic table should contain
        
    - name: data_retention_time_in_days
      value: integer
      description: >
        Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table
        
    - name: max_data_extension_time_in_days
      value: integer
      description: >
        Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table
        
    - name: comment
      value: string
      description: >
        Specifies a comment for the dynamic table.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_dynamic_table"
    values={[
        { label: 'delete_dynamic_table', value: 'delete_dynamic_table' }
    ]}
>
<TabItem value="delete_dynamic_table">

Delete a dynamic table with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

```sql
DELETE FROM snowflake.dynamic_table.dynamic_tables
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
    defaultValue="clone_dynamic_table"
    values={[
        { label: 'clone_dynamic_table', value: 'clone_dynamic_table' },
        { label: 'undrop_dynamic_table', value: 'undrop_dynamic_table' },
        { label: 'suspend_dynamic_table', value: 'suspend_dynamic_table' },
        { label: 'resume_dynamic_table', value: 'resume_dynamic_table' },
        { label: 'refresh_dynamic_table', value: 'refresh_dynamic_table' },
        { label: 'suspend_recluster_dynamic_table', value: 'suspend_recluster_dynamic_table' },
        { label: 'resume_recluster_dynamic_table', value: 'resume_recluster_dynamic_table' },
        { label: 'swap_with_dynamic_table', value: 'swap_with_dynamic_table' }
    ]}
>
<TabItem value="clone_dynamic_table">

Create a new dynamic table by cloning from the specified resource

```sql
EXEC snowflake.dynamic_table.dynamic_tables.clone_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }}, 
@targetDatabase='{{ targetDatabase }}', 
@targetSchema='{{ targetSchema }}' 
@@json=
'{
"name": "{{ name }}", 
"target_lag": "{{ target_lag }}", 
"warehouse": "{{ warehouse }}", 
"point_of_time": "{{ point_of_time }}"
}';
```
</TabItem>
<TabItem value="undrop_dynamic_table">

Undrop specified dynamic table

```sql
EXEC snowflake.dynamic_table.dynamic_tables.undrop_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="suspend_dynamic_table">

Suspend refreshes on the dynamic table

```sql
EXEC snowflake.dynamic_table.dynamic_tables.suspend_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="resume_dynamic_table">

Resume refreshes on the dynamic table

```sql
EXEC snowflake.dynamic_table.dynamic_tables.resume_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="refresh_dynamic_table">

Specifies that the dynamic table should be manually refreshed

```sql
EXEC snowflake.dynamic_table.dynamic_tables.refresh_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="suspend_recluster_dynamic_table">

Suspend recluster of a dynamic table

```sql
EXEC snowflake.dynamic_table.dynamic_tables.suspend_recluster_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="resume_recluster_dynamic_table">

Resume recluster of a dynamic table

```sql
EXEC snowflake.dynamic_table.dynamic_tables.resume_recluster_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="swap_with_dynamic_table">

Swap with another dynamic table

```sql
EXEC snowflake.dynamic_table.dynamic_tables.swap_with_dynamic_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@targetName='{{ targetName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }}, 
@targetDatabase='{{ targetDatabase }}', 
@targetSchema='{{ targetSchema }}';
```
</TabItem>
</Tabs>
