--- 
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - database
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.database.databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_databases"
    values={[
        { label: 'list_databases', value: 'list_databases' },
        { label: 'fetch_database', value: 'fetch_database' }
    ]}
>
<TabItem value="list_databases">

Snowflake database object.

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
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Budget that defines a monthly spending limit on the compute costs for a Snowflake account or a custom group of Snowflake objects.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional comment in which to store information related to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the database was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the default Time Travel retention time for all schemas created in the database.</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Default collation specification for all schemas and tables added to the database. You an override the default at the schema and individual table levels.</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the database was dropped.</td>
</tr>
<tr>
    <td><CopyableCode code="is_current" /></td>
    <td><code>boolean</code></td>
    <td>Current database for the session.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Whether the database is the default database for a user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Database type, permanent (default) or transient. (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="log_level" /></td>
    <td><code>string</code></td>
    <td>Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days for which Snowflake can extend the data retention period for tables in the database to prevent streams on the tables from becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Name of the role that owns the database.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>Type of role that owns the object, either ROLE or DATABASE_ROLE</td>
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
    <td>Maximum number of consecutive failed task runs before the current task is suspended automatically.</td>
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
<TabItem value="fetch_database">

Snowflake database object.

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
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Budget that defines a monthly spending limit on the compute costs for a Snowflake account or a custom group of Snowflake objects.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional comment in which to store information related to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the database was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the default Time Travel retention time for all schemas created in the database.</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Default collation specification for all schemas and tables added to the database. You an override the default at the schema and individual table levels.</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the database was dropped.</td>
</tr>
<tr>
    <td><CopyableCode code="is_current" /></td>
    <td><code>boolean</code></td>
    <td>Current database for the session.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Whether the database is the default database for a user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Database type, permanent (default) or transient. (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="log_level" /></td>
    <td><code>string</code></td>
    <td>Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days for which Snowflake can extend the data retention period for tables in the database to prevent streams on the tables from becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Name of the role that owns the database.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>Type of role that owns the object, either ROLE or DATABASE_ROLE</td>
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
    <td>Maximum number of consecutive failed task runs before the current task is suspended automatically.</td>
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
    <td><a href="#list_databases"><CopyableCode code="list_databases" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a>, <a href="#parameter-history">history</a></td>
    <td>Lists the accessible databases.</td>
</tr>
<tr>
    <td><a href="#fetch_database"><CopyableCode code="fetch_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetches a database.</td>
</tr>
<tr>
    <td><a href="#create_database"><CopyableCode code="create_database" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-kind">kind</a></td>
    <td>Creates a database, with modifiers as query parameters. You must provide the full database definition when creating a database.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_database"><CopyableCode code="create_or_alter_database" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Creates a new, or alters an existing, database. You must provide the full database definition even when altering an existing database.</td>
</tr>
<tr>
    <td><a href="#delete_database"><CopyableCode code="delete_database" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a>, <a href="#parameter-restrict">restrict</a></td>
    <td>Deletes the specified database. If you enable the `ifExists` parameter, the operation succeeds even if the database does not exist. Otherwise, a 404 failure is returned if the database does not exist. if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#create_database_from_share"><CopyableCode code="create_database_from_share" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-share">share</a></td>
    <td>Creates a database from a given share.</td>
</tr>
<tr>
    <td><a href="#create_database_from_share_deprecated"><CopyableCode code="create_database_from_share_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-share">share</a></td>
    <td>Creates a database from a given share.</td>
</tr>
<tr>
    <td><a href="#clone_database"><CopyableCode code="clone_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-kind">kind</a></td>
    <td>Clones an existing database, with modifiers as query parameters. You must provide the full database definition when cloning an existing database.</td>
</tr>
<tr>
    <td><a href="#undrop_database"><CopyableCode code="undrop_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Undrops database.</td>
</tr>
<tr>
    <td><a href="#enable_database_replication"><CopyableCode code="enable_database_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ignore_edition_check">ignore_edition_check</a></td>
    <td>Promotes a local database to serve as a primary database for replication. A primary database can be replicated in one or more accounts, allowing users in those accounts to query objects in each secondary (i.e. replica) database.</td>
</tr>
<tr>
    <td><a href="#disable_database_replication"><CopyableCode code="disable_database_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Disables replication for this primary database, meaning no replica of this database (i.e. secondary database) in another account can be refreshed. Any secondary databases remain linked to the primary database, but requests to refresh a secondary database are denied.</td>
</tr>
<tr>
    <td><a href="#refresh_database_replication"><CopyableCode code="refresh_database_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Refreshes a secondary database from a snapshot of its primary database. A snapshot includes changes to the objects and data.
If you call this endpoint while another refresh for the same replica database is running, it fails and returns an error. Snowflake ensures only one refresh is executed at any given time.</td>
</tr>
<tr>
    <td><a href="#enable_database_failover"><CopyableCode code="enable_database_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Specifies a comma-separated list of accounts in your organization where a replica of this primary database can be promoted to serve as the primary database.</td>
</tr>
<tr>
    <td><a href="#disable_database_failover"><CopyableCode code="disable_database_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Disables failover for this primary database, meaning no replica of this database (i.e. secondary database) can be promoted to serve as the primary database.</td>
</tr>
<tr>
    <td><a href="#primary_database_failover"><CopyableCode code="primary_database_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Promotes the specified secondary (replica) database to serve as the primary database. When promoted, the database becomes writeable. At the same time, the previous primary database becomes a read-only secondary database.</td>
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
    <td>Optionally includes dropped databases that have not yet been purged.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. (example: true, default: false)</td>
</tr>
<tr id="parameter-ignore_edition_check">
    <td><CopyableCode code="ignore_edition_check" /></td>
    <td><code>boolean</code></td>
    <td>Whether to allow replicating data to accounts on lower editions. Default: `true`. For more information, see the <a href="https://docs.snowflake.com/en/sql-reference/sql/alter-database"> ALTER DATABASE</a> reference.</td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of database to create. Currently, Snowflake supports only `transient` and `permanent` (also represented by the empty string).</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
<tr id="parameter-restrict">
    <td><CopyableCode code="restrict" /></td>
    <td><code>boolean</code></td>
    <td>Whether to drop the database if foreign keys exist that reference any tables in the database. - `true`: Return a warning about existing foreign key references and don't drop the database. - `false`: Drop the database and all objects in the database, including tables with primary or unique keys that are referenced by foreign keys in other tables. (default: false)</td>
</tr>
<tr id="parameter-share">
    <td><CopyableCode code="share" /></td>
    <td><code>string</code></td>
    <td>ID of the share from which to create the database, in the form "<provider_account>.<share_name>".</td>
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
    defaultValue="list_databases"
    values={[
        { label: 'list_databases', value: 'list_databases' },
        { label: 'fetch_database', value: 'fetch_database' }
    ]}
>
<TabItem value="list_databases">

Lists the accessible databases.

```sql
SELECT
name,
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
max_data_extension_time_in_days,
options,
origin,
owner,
owner_role_type,
retention_time,
serverless_task_max_statement_size,
serverless_task_min_statement_size,
suspend_task_after_num_failures,
trace_level,
user_task_managed_initial_warehouse_size,
user_task_timeout_ms
FROM snowflake.database.databases
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}'
AND history = '{{ history }}';
```
</TabItem>
<TabItem value="fetch_database">

Fetches a database.

```sql
SELECT
name,
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
max_data_extension_time_in_days,
options,
origin,
owner,
owner_role_type,
retention_time,
serverless_task_max_statement_size,
serverless_task_min_statement_size,
suspend_task_after_num_failures,
trace_level,
user_task_managed_initial_warehouse_size,
user_task_timeout_ms
FROM snowflake.database.databases
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_database"
    values={[
        { label: 'create_database', value: 'create_database' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_database">

Creates a database, with modifiers as query parameters. You must provide the full database definition when creating a database.

```sql
INSERT INTO snowflake.database.databases (
data__name,
data__kind,
data__comment,
data__data_retention_time_in_days,
data__default_ddl_collation,
data__log_level,
data__max_data_extension_time_in_days,
data__suspend_task_after_num_failures,
data__trace_level,
data__user_task_managed_initial_warehouse_size,
data__serverless_task_min_statement_size,
data__serverless_task_max_statement_size,
data__user_task_timeout_ms,
endpoint,
createMode,
kind
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ comment }}',
{{ data_retention_time_in_days }},
'{{ default_ddl_collation }}',
'{{ log_level }}',
{{ max_data_extension_time_in_days }},
{{ suspend_task_after_num_failures }},
'{{ trace_level }}',
'{{ user_task_managed_initial_warehouse_size }}',
'{{ serverless_task_min_statement_size }}',
'{{ serverless_task_max_statement_size }}',
{{ user_task_timeout_ms }},
'{{ endpoint }}',
'{{ createMode }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: databases
  props:
    - name: endpoint
      value: string
      description: Required parameter for the databases resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: kind
      value: string
      description: >
        Database type, permanent (default) or transient.
        
      valid_values: ['PERMANENT', 'TRANSIENT']
      default: PERMANENT
    - name: comment
      value: string
      description: >
        Optional comment in which to store information related to the database.
        
    - name: data_retention_time_in_days
      value: integer
      description: >
        Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the default Time Travel retention time for all schemas created in the database.
        
    - name: default_ddl_collation
      value: string
      description: >
        Default collation specification for all schemas and tables added to the database. You an override the default at the schema and individual table levels.
        
    - name: log_level
      value: string
      description: >
        Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.
        
    - name: max_data_extension_time_in_days
      value: integer
      description: >
        Maximum number of days for which Snowflake can extend the data retention period for tables in the database to prevent streams on the tables from becoming stale.
        
    - name: suspend_task_after_num_failures
      value: integer
      description: >
        Maximum number of consecutive failed task runs before the current task is suspended automatically.
        
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
      description: Type of database to create. Currently, Snowflake supports only `transient` and `permanent` (also represented by the empty string).
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_database"
    values={[
        { label: 'create_or_alter_database', value: 'create_or_alter_database' }
    ]}
>
<TabItem value="create_or_alter_database">

Creates a new, or alters an existing, database. You must provide the full database definition even when altering an existing database.

```sql
REPLACE snowflake.database.databases
SET 
data__name = '{{ name }}',
data__kind = '{{ kind }}',
data__comment = '{{ comment }}',
data__data_retention_time_in_days = {{ data_retention_time_in_days }},
data__default_ddl_collation = '{{ default_ddl_collation }}',
data__log_level = '{{ log_level }}',
data__max_data_extension_time_in_days = {{ max_data_extension_time_in_days }},
data__suspend_task_after_num_failures = {{ suspend_task_after_num_failures }},
data__trace_level = '{{ trace_level }}',
data__user_task_managed_initial_warehouse_size = '{{ user_task_managed_initial_warehouse_size }}',
data__serverless_task_min_statement_size = '{{ serverless_task_min_statement_size }}',
data__serverless_task_max_statement_size = '{{ serverless_task_max_statement_size }}',
data__user_task_timeout_ms = {{ user_task_timeout_ms }}
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_database"
    values={[
        { label: 'delete_database', value: 'delete_database' }
    ]}
>
<TabItem value="delete_database">

Deletes the specified database. If you enable the `ifExists` parameter, the operation succeeds even if the database does not exist. Otherwise, a 404 failure is returned if the database does not exist. if the drop is unsuccessful.

```sql
DELETE FROM snowflake.database.databases
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}'
AND restrict = '{{ restrict }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_database_from_share"
    values={[
        { label: 'create_database_from_share', value: 'create_database_from_share' },
        { label: 'create_database_from_share_deprecated', value: 'create_database_from_share_deprecated' },
        { label: 'clone_database', value: 'clone_database' },
        { label: 'undrop_database', value: 'undrop_database' },
        { label: 'enable_database_replication', value: 'enable_database_replication' },
        { label: 'disable_database_replication', value: 'disable_database_replication' },
        { label: 'refresh_database_replication', value: 'refresh_database_replication' },
        { label: 'enable_database_failover', value: 'enable_database_failover' },
        { label: 'disable_database_failover', value: 'disable_database_failover' },
        { label: 'primary_database_failover', value: 'primary_database_failover' }
    ]}
>
<TabItem value="create_database_from_share">

Creates a database from a given share.

```sql
EXEC snowflake.database.databases.create_database_from_share 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@share='{{ share }}' 
@@json=
'{
"name": "{{ name }}"
}';
```
</TabItem>
<TabItem value="create_database_from_share_deprecated">

Creates a database from a given share.

```sql
EXEC snowflake.database.databases.create_database_from_share_deprecated 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@share='{{ share }}';
```
</TabItem>
<TabItem value="clone_database">

Clones an existing database, with modifiers as query parameters. You must provide the full database definition when cloning an existing database.

```sql
EXEC snowflake.database.databases.clone_database 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@kind='{{ kind }}' 
@@json=
'{
"name": "{{ name }}", 
"kind": "{{ kind }}", 
"comment": "{{ comment }}", 
"data_retention_time_in_days": {{ data_retention_time_in_days }}, 
"default_ddl_collation": "{{ default_ddl_collation }}", 
"log_level": "{{ log_level }}", 
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
<TabItem value="undrop_database">

Undrops database.

```sql
EXEC snowflake.database.databases.undrop_database 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="enable_database_replication">

Promotes a local database to serve as a primary database for replication. A primary database can be replicated in one or more accounts, allowing users in those accounts to query objects in each secondary (i.e. replica) database.

```sql
EXEC snowflake.database.databases.enable_database_replication 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ignore_edition_check={{ ignore_edition_check }} 
@@json=
'{
"accounts": "{{ accounts }}"
}';
```
</TabItem>
<TabItem value="disable_database_replication">

Disables replication for this primary database, meaning no replica of this database (i.e. secondary database) in another account can be refreshed. Any secondary databases remain linked to the primary database, but requests to refresh a secondary database are denied.

```sql
EXEC snowflake.database.databases.disable_database_replication 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"accounts": "{{ accounts }}"
}';
```
</TabItem>
<TabItem value="refresh_database_replication">

Refreshes a secondary database from a snapshot of its primary database. A snapshot includes changes to the objects and data.
If you call this endpoint while another refresh for the same replica database is running, it fails and returns an error. Snowflake ensures only one refresh is executed at any given time.

```sql
EXEC snowflake.database.databases.refresh_database_replication 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="enable_database_failover">

Specifies a comma-separated list of accounts in your organization where a replica of this primary database can be promoted to serve as the primary database.

```sql
EXEC snowflake.database.databases.enable_database_failover 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"accounts": "{{ accounts }}"
}';
```
</TabItem>
<TabItem value="disable_database_failover">

Disables failover for this primary database, meaning no replica of this database (i.e. secondary database) can be promoted to serve as the primary database.

```sql
EXEC snowflake.database.databases.disable_database_failover 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"accounts": "{{ accounts }}"
}';
```
</TabItem>
<TabItem value="primary_database_failover">

Promotes the specified secondary (replica) database to serve as the primary database. When promoted, the database becomes writeable. At the same time, the previous primary database becomes a read-only secondary database.

```sql
EXEC snowflake.database.databases.primary_database_failover 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
