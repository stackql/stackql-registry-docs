--- 
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - schema
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.schema.schemas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_schemas"
    values={[
        { label: 'list_schemas', value: 'list_schemas' },
        { label: 'fetch_schema', value: 'fetch_schema' }
    ]}
>
<TabItem value="list_schemas">

Snowflake schema definition.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database that the schema belongs to</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Budget that defines a monthly spending limit on the compute costs  for a Snowflake account or a custom group of Snowflake objects.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional comment in which to store information related to the schema.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the schema was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the default Time Travel retention time for all tables created in the schema</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Specifies a default collation specification for all tables added to the schema. You an override the default at the schema and individual table levels.</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the schema was dropped.</td>
</tr>
<tr>
    <td><CopyableCode code="is_current" /></td>
    <td><code>boolean</code></td>
    <td>Current schema for the session.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Default schema for a user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Schema type, permanent (default) or transient. (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="log_level" /></td>
    <td><code>string</code></td>
    <td>Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.</td>
</tr>
<tr>
    <td><CopyableCode code="managed_access" /></td>
    <td><code>boolean</code></td>
    <td>Whether this schema is a managed access schema that centralizes privilege management with the schema owner.</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days for which Snowflake can extend the data retention period for tables in the schema to prevent streams on the tables from becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Name of the role that owns the schema.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>Type of role that owns the object, either `ROLE` or `DATABASE_ROLE`.</td>
</tr>
<tr>
    <td><CopyableCode code="pipe_execution_paused" /></td>
    <td><code>boolean</code></td>
    <td>Whether pipe execution is paused.</td>
</tr>
<tr>
    <td><CopyableCode code="retention_time" /></td>
    <td><code>integer</code></td>
    <td>Number of days that historical data is retained for Time Travel.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_max_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_min_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend_task_after_num_failures" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of consecutive failed task runs after which the current task is suspended automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="trace_level" /></td>
    <td><code>string</code></td>
    <td>How trace events are ingested into the event table. Currently, Snowflake supports only `ALWAYS`, `ON_EVENT`, and `OFF`.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_managed_initial_warehouse_size" /></td>
    <td><code>string</code></td>
    <td>Size of the compute resources to provision for the first run of the serverless task, before a task history is available for Snowflake to determine an ideal size.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_timeout_ms" /></td>
    <td><code>integer</code></td>
    <td>Time limit, in milliseconds, for a single run of the task before it times out.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_schema">

Snowflake schema definition.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database that the schema belongs to</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Budget that defines a monthly spending limit on the compute costs  for a Snowflake account or a custom group of Snowflake objects.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional comment in which to store information related to the schema.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the schema was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the default Time Travel retention time for all tables created in the schema</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Specifies a default collation specification for all tables added to the schema. You an override the default at the schema and individual table levels.</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the schema was dropped.</td>
</tr>
<tr>
    <td><CopyableCode code="is_current" /></td>
    <td><code>boolean</code></td>
    <td>Current schema for the session.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Default schema for a user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Schema type, permanent (default) or transient. (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="log_level" /></td>
    <td><code>string</code></td>
    <td>Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.</td>
</tr>
<tr>
    <td><CopyableCode code="managed_access" /></td>
    <td><code>boolean</code></td>
    <td>Whether this schema is a managed access schema that centralizes privilege management with the schema owner.</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days for which Snowflake can extend the data retention period for tables in the schema to prevent streams on the tables from becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Name of the role that owns the schema.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>Type of role that owns the object, either `ROLE` or `DATABASE_ROLE`.</td>
</tr>
<tr>
    <td><CopyableCode code="pipe_execution_paused" /></td>
    <td><code>boolean</code></td>
    <td>Whether pipe execution is paused.</td>
</tr>
<tr>
    <td><CopyableCode code="retention_time" /></td>
    <td><code>integer</code></td>
    <td>Number of days that historical data is retained for Time Travel.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_max_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_min_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend_task_after_num_failures" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of consecutive failed task runs after which the current task is suspended automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="trace_level" /></td>
    <td><code>string</code></td>
    <td>How trace events are ingested into the event table. Currently, Snowflake supports only `ALWAYS`, `ON_EVENT`, and `OFF`.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_managed_initial_warehouse_size" /></td>
    <td><code>string</code></td>
    <td>Size of the compute resources to provision for the first run of the serverless task, before a task history is available for Snowflake to determine an ideal size.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_timeout_ms" /></td>
    <td><code>integer</code></td>
    <td>Time limit, in milliseconds, for a single run of the task before it times out.</td>
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
    <td><a href="#list_schemas"><CopyableCode code="list_schemas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a>, <a href="#parameter-history">history</a></td>
    <td>Lists the accessible schemas.</td>
</tr>
<tr>
    <td><a href="#fetch_schema"><CopyableCode code="fetch_schema" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetches a schema.</td>
</tr>
<tr>
    <td><a href="#create_schema"><CopyableCode code="create_schema" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-kind">kind</a></td>
    <td>Creates a schema, with modifiers as query parameters. You must provide the full schema definition when creating a schema.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_schema"><CopyableCode code="create_or_alter_schema" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-kind">kind</a></td>
    <td>Creates a new, or alters an existing, schema. You must provide the full schema definition even when altering an existing schema.</td>
</tr>
<tr>
    <td><a href="#delete_schema"><CopyableCode code="delete_schema" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a>, <a href="#parameter-restrict">restrict</a></td>
    <td>Deletes the specified schema. If you enable the `ifExists` parameter, the operation succeeds even if the schema does not exist. Otherwise, a 404 failure is returned if the schema does not exist. if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#clone_schema"><CopyableCode code="clone_schema" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-kind">kind</a>, <a href="#parameter-targetDatabase">targetDatabase</a></td>
    <td>Clones an existing schema, with modifiers as query parameters. You must provide the full schema definition when cloning an existing schema.</td>
</tr>
<tr>
    <td><a href="#undrop_schema"><CopyableCode code="undrop_schema" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Undrops schema.</td>
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
<tr id="parameter-history">
    <td><CopyableCode code="history" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include dropped schemas that have not yet been purged. Default: `false`. (default: false)</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. (example: true, default: false)</td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of schema to clone. Currently, Snowflake supports only `transient` and `permanent` (also represented by the empty string). (default: )</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
<tr id="parameter-restrict">
    <td><CopyableCode code="restrict" /></td>
    <td><code>boolean</code></td>
    <td>Whether to drop the schema if foreign keys exist that reference any tables in the schema. - `true`: Return a warning about existing foreign key references and don't drop the schema. - `false`: Drop the schema and all objects in the database, including tables with primary or unique keys that are referenced by foreign keys in other tables. Default: `false`. (default: false)</td>
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
    <td>Database of the newly created schema. Defaults to the source schema's database. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_schemas"
    values={[
        { label: 'list_schemas', value: 'list_schemas' },
        { label: 'fetch_schema', value: 'fetch_schema' }
    ]}
>
<TabItem value="list_schemas">

Lists the accessible schemas.

```sql
SELECT
name,
database_name,
budget,
comment,
created_on,
data_retention_time_in_days,
default_ddl_collation,
dropped_on,
is_current,
is_default,
kind,
log_level,
managed_access,
max_data_extension_time_in_days,
options,
owner,
owner_role_type,
pipe_execution_paused,
retention_time,
serverless_task_max_statement_size,
serverless_task_min_statement_size,
suspend_task_after_num_failures,
trace_level,
user_task_managed_initial_warehouse_size,
user_task_timeout_ms
FROM snowflake.schema.schemas
WHERE database_name = '{{ database_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}'
AND history = '{{ history }}';
```
</TabItem>
<TabItem value="fetch_schema">

Fetches a schema.

```sql
SELECT
name,
database_name,
budget,
comment,
created_on,
data_retention_time_in_days,
default_ddl_collation,
dropped_on,
is_current,
is_default,
kind,
log_level,
managed_access,
max_data_extension_time_in_days,
options,
owner,
owner_role_type,
pipe_execution_paused,
retention_time,
serverless_task_max_statement_size,
serverless_task_min_statement_size,
suspend_task_after_num_failures,
trace_level,
user_task_managed_initial_warehouse_size,
user_task_timeout_ms
FROM snowflake.schema.schemas
WHERE database_name = '{{ database_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_schema"
    values={[
        { label: 'create_schema', value: 'create_schema' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_schema">

Creates a schema, with modifiers as query parameters. You must provide the full schema definition when creating a schema.

```sql
INSERT INTO snowflake.schema.schemas (
data__name,
data__kind,
data__comment,
data__managed_access,
data__data_retention_time_in_days,
data__default_ddl_collation,
data__log_level,
data__pipe_execution_paused,
data__max_data_extension_time_in_days,
data__suspend_task_after_num_failures,
data__trace_level,
data__user_task_managed_initial_warehouse_size,
data__serverless_task_min_statement_size,
data__serverless_task_max_statement_size,
data__user_task_timeout_ms,
database_name,
endpoint,
createMode,
kind
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ comment }}',
{{ managed_access }},
{{ data_retention_time_in_days }},
'{{ default_ddl_collation }}',
'{{ log_level }}',
{{ pipe_execution_paused }},
{{ max_data_extension_time_in_days }},
{{ suspend_task_after_num_failures }},
'{{ trace_level }}',
'{{ user_task_managed_initial_warehouse_size }}',
'{{ serverless_task_min_statement_size }}',
'{{ serverless_task_max_statement_size }}',
{{ user_task_timeout_ms }},
'{{ database_name }}',
'{{ endpoint }}',
'{{ createMode }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: schemas
  props:
    - name: database_name
      value: string
      description: Required parameter for the schemas resource.
    - name: endpoint
      value: string
      description: Required parameter for the schemas resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: kind
      value: string
      description: >
        Schema type, permanent (default) or transient.
        
      valid_values: ['PERMANENT', 'TRANSIENT']
      default: PERMANENT
    - name: comment
      value: string
      description: >
        Optional comment in which to store information related to the schema.
        
    - name: managed_access
      value: boolean
      description: >
        Whether this schema is a managed access schema that centralizes privilege management with the schema owner.
        
      default: false
    - name: data_retention_time_in_days
      value: integer
      description: >
        Number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the default Time Travel retention time for all tables created in the schema
        
    - name: default_ddl_collation
      value: string
      description: >
        Specifies a default collation specification for all tables added to the schema. You an override the default at the schema and individual table levels.
        
    - name: log_level
      value: string
      description: >
        Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.
        
    - name: pipe_execution_paused
      value: boolean
      description: >
        Whether pipe execution is paused.
        
    - name: max_data_extension_time_in_days
      value: integer
      description: >
        Maximum number of days for which Snowflake can extend the data retention period for tables in the schema to prevent streams on the tables from becoming stale.
        
    - name: suspend_task_after_num_failures
      value: integer
      description: >
        Specifies the number of consecutive failed task runs after which the current task is suspended automatically.
        
    - name: trace_level
      value: string
      description: >
        How trace events are ingested into the event table. Currently, Snowflake supports only `ALWAYS`, `ON_EVENT`, and `OFF`.
        
    - name: user_task_managed_initial_warehouse_size
      value: string
      description: >
        Size of the compute resources to provision for the first run of the serverless task, before a task history is available for Snowflake to determine an ideal size.
        
    - name: serverless_task_min_statement_size
      value: string
      description: >
        Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.
        
    - name: serverless_task_max_statement_size
      value: string
      description: >
        Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.
        
    - name: user_task_timeout_ms
      value: integer
      description: >
        Time limit, in milliseconds, for a single run of the task before it times out.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
    - name: kind
      value: string
      description: Type of schema to create. Currently, Snowflake supports only `transient` and `permanent` (also represented by the empty string). (default: )
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_schema"
    values={[
        { label: 'create_or_alter_schema', value: 'create_or_alter_schema' }
    ]}
>
<TabItem value="create_or_alter_schema">

Creates a new, or alters an existing, schema. You must provide the full schema definition even when altering an existing schema.

```sql
REPLACE snowflake.schema.schemas
SET 
data__name = '{{ name }}',
data__kind = '{{ kind }}',
data__comment = '{{ comment }}',
data__managed_access = {{ managed_access }},
data__data_retention_time_in_days = {{ data_retention_time_in_days }},
data__default_ddl_collation = '{{ default_ddl_collation }}',
data__log_level = '{{ log_level }}',
data__pipe_execution_paused = {{ pipe_execution_paused }},
data__max_data_extension_time_in_days = {{ max_data_extension_time_in_days }},
data__suspend_task_after_num_failures = {{ suspend_task_after_num_failures }},
data__trace_level = '{{ trace_level }}',
data__user_task_managed_initial_warehouse_size = '{{ user_task_managed_initial_warehouse_size }}',
data__serverless_task_min_statement_size = '{{ serverless_task_min_statement_size }}',
data__serverless_task_max_statement_size = '{{ serverless_task_max_statement_size }}',
data__user_task_timeout_ms = {{ user_task_timeout_ms }}
WHERE 
database_name = '{{ database_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required
AND kind = '{{ kind}}';
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_schema"
    values={[
        { label: 'delete_schema', value: 'delete_schema' }
    ]}
>
<TabItem value="delete_schema">

Deletes the specified schema. If you enable the `ifExists` parameter, the operation succeeds even if the schema does not exist. Otherwise, a 404 failure is returned if the schema does not exist. if the drop is unsuccessful.

```sql
DELETE FROM snowflake.schema.schemas
WHERE database_name = '{{ database_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}'
AND restrict = '{{ restrict }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="clone_schema"
    values={[
        { label: 'clone_schema', value: 'clone_schema' },
        { label: 'undrop_schema', value: 'undrop_schema' }
    ]}
>
<TabItem value="clone_schema">

Clones an existing schema, with modifiers as query parameters. You must provide the full schema definition when cloning an existing schema.

```sql
EXEC snowflake.schema.schemas.clone_schema 
@database_name='{{ database_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@kind='{{ kind }}', 
@targetDatabase='{{ targetDatabase }}' 
@@json=
'{
"name": "{{ name }}", 
"kind": "{{ kind }}", 
"comment": "{{ comment }}", 
"managed_access": {{ managed_access }}, 
"data_retention_time_in_days": {{ data_retention_time_in_days }}, 
"default_ddl_collation": "{{ default_ddl_collation }}", 
"log_level": "{{ log_level }}", 
"pipe_execution_paused": {{ pipe_execution_paused }}, 
"max_data_extension_time_in_days": {{ max_data_extension_time_in_days }}, 
"suspend_task_after_num_failures": {{ suspend_task_after_num_failures }}, 
"trace_level": "{{ trace_level }}", 
"user_task_managed_initial_warehouse_size": "{{ user_task_managed_initial_warehouse_size }}", 
"serverless_task_min_statement_size": "{{ serverless_task_min_statement_size }}", 
"serverless_task_max_statement_size": "{{ serverless_task_max_statement_size }}", 
"user_task_timeout_ms": {{ user_task_timeout_ms }}
}';
```
</TabItem>
<TabItem value="undrop_schema">

Undrops schema.

```sql
EXEC snowflake.schema.schemas.undrop_schema 
@database_name='{{ database_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
