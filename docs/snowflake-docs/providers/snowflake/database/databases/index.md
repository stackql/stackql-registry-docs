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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="budget" /> | `string` | Budget that defines a monthly spending limit on the compute costs for a Snowflake account or a custom group of Snowflake objects. |
| <CopyableCode code="comment" /> | `string` | Optional comment in which to store information related to the database. |
| <CopyableCode code="created_on" /> | `string` | Date and time the database was created. |
| <CopyableCode code="data_retention_time_in_days" /> | `integer` | Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the default Time Travel retention time for all schemas created in the database. |
| <CopyableCode code="default_ddl_collation" /> | `string` | Default collation specification for all schemas and tables added to the database. You an override the default at the schema and individual table levels. |
| <CopyableCode code="dropped_on" /> | `string` | Date and time the database was dropped. |
| <CopyableCode code="is_current" /> | `boolean` | Current database for the session. |
| <CopyableCode code="is_default" /> | `boolean` | Whether the database is the default database for a user. |
| <CopyableCode code="kind" /> | `string` | Database type, permanent (default) or transient. |
| <CopyableCode code="log_level" /> | `string` | Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`. |
| <CopyableCode code="max_data_extension_time_in_days" /> | `integer` | Maximum number of days for which Snowflake can extend the data retention period for tables in the database to prevent streams on the tables from becoming stale. |
| <CopyableCode code="options" /> | `string` |  |
| <CopyableCode code="origin" /> | `string` |  |
| <CopyableCode code="owner" /> | `string` | Name of the role that owns the database. |
| <CopyableCode code="owner_role_type" /> | `string` | Type of role that owns the object, either ROLE or DATABASE_ROLE |
| <CopyableCode code="retention_time" /> | `integer` | Number of days that historical data is retained for Time Travel. |
| <CopyableCode code="serverless_task_max_statement_size" /> | `string` | Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. |
| <CopyableCode code="serverless_task_min_statement_size" /> | `string` | Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. |
| <CopyableCode code="suspend_task_after_num_failures" /> | `integer` | Maximum number of consecutive failed task runs before the current task is suspended automatically. |
| <CopyableCode code="trace_level" /> | `string` | How trace events are ingested into the event table. Currently, Snowflake supports only `ALWAYS`, `ON_EVENT`, and `OFF`. |
| <CopyableCode code="user_task_managed_initial_warehouse_size" /> | `string` | Size of the compute resources to provision for the first run of the serverless task, before a task history is available for Snowflake to determine an ideal size. |
| <CopyableCode code="user_task_timeout_ms" /> | `integer` | Time limit, in milliseconds, for a single run of the task before it times out. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_database" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetches a database. |
| <CopyableCode code="list_databases" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" />, <CopyableCode code="history" /> | Lists the accessible databases. |
| <CopyableCode code="create_database" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="kind" /> | Creates a database, with modifiers as query parameters. You must provide the full database definition when creating a database. |
| <CopyableCode code="delete_database" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="restrict" /> | Deletes the specified database. If you enable the `ifExists` parameter, the operation succeeds even if the database does not exist. Otherwise, a 404 failure is returned if the database does not exist. if the drop is unsuccessful. |
| <CopyableCode code="create_or_alter_database" /> | `REPLACE` | <CopyableCode code="name, data__name, endpoint" /> | - | Creates a new, or alters an existing, database. You must provide the full database definition even when altering an existing database. |
| <CopyableCode code="clone_database" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="kind" /> | Clones an existing database, with modifiers as query parameters. You must provide the full database definition when cloning an existing database. |
| <CopyableCode code="create_database_from_share" /> | `EXEC` | <CopyableCode code="endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="share" /> | Creates a database from a given share. |
| <CopyableCode code="create_database_from_share_deprecated" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="share" /> | Creates a database from a given share. |
| <CopyableCode code="disable_database_failover" /> | `EXEC` | <CopyableCode code="name, data__accounts, endpoint" /> | - | Disables failover for this primary database, meaning no replica of this database (i.e. secondary database) can be promoted to serve as the primary database. |
| <CopyableCode code="disable_database_replication" /> | `EXEC` | <CopyableCode code="name, data__accounts, endpoint" /> | - | Disables replication for this primary database, meaning no replica of this database (i.e. secondary database) in another account can be refreshed. Any secondary databases remain linked to the primary database, but requests to refresh a secondary database are denied. |
| <CopyableCode code="enable_database_failover" /> | `EXEC` | <CopyableCode code="name, data__accounts, endpoint" /> | - | Specifies a comma-separated list of accounts in your organization where a replica of this primary database can be promoted to serve as the primary database. |
| <CopyableCode code="enable_database_replication" /> | `EXEC` | <CopyableCode code="name, data__accounts, endpoint" /> | <CopyableCode code="ignore_edition_check" /> | Promotes a local database to serve as a primary database for replication. A primary database can be replicated in one or more accounts, allowing users in those accounts to query objects in each secondary (i.e. replica) database. |
| <CopyableCode code="primary_database_failover" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Promotes the specified secondary (replica) database to serve as the primary database. When promoted, the database becomes writeable. At the same time, the previous primary database becomes a read-only secondary database. |
| <CopyableCode code="refresh_database_replication" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Refreshes a secondary database from a snapshot of its primary database. A snapshot includes changes to the objects and data. If you call this endpoint while another refresh for the same replica database is running, it fails and returns an error. Snowflake ensures only one refresh is executed at any given time. |
| <CopyableCode code="undrop_database" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Undrops database. |

  

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="history" /> | Optionally includes dropped databases that have not yet been purged. | `boolean` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="ignore_edition_check" /> | Whether to allow replicating data to accounts on lower editions. Default: `true`. For more information, see the {a href=https://docs.snowflake.com/en/sql-reference/sql/alter-database} ALTER DATABASE{/a} reference. | `boolean` | `-` |
| <CopyableCode code="kind" /> | Type of database to create. Currently, Snowflake supports only `transient` and `permanent` (also represented by the empty string). | `string` | `-` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="restrict" /> | Whether to drop the database if foreign keys exist that reference any tables in the database. - `true`: Return a warning about existing foreign key references and don't drop the database. - `false`: Drop the database and all objects in the database, including tables with primary or unique keys that are referenced by foreign keys in other tables. | `boolean` | `false` |
| <CopyableCode code="share" /> | ID of the share from which to create the database, in the form "{provider_account}.{share_name}". | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

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
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

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
endpoint
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ comment }}',
'{{ data_retention_time_in_days }}',
'{{ default_ddl_collation }}',
'{{ log_level }}',
'{{ max_data_extension_time_in_days }}',
'{{ suspend_task_after_num_failures }}',
'{{ trace_level }}',
'{{ user_task_managed_initial_warehouse_size }}',
'{{ serverless_task_min_statement_size }}',
'{{ serverless_task_max_statement_size }}',
'{{ user_task_timeout_ms }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.database.databases (
data__name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: databases
  props:
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: comment
      value: string
    - name: data_retention_time_in_days
      value: integer
    - name: default_ddl_collation
      value: string
    - name: log_level
      value: string
    - name: max_data_extension_time_in_days
      value: integer
    - name: suspend_task_after_num_failures
      value: integer
    - name: trace_level
      value: string
    - name: user_task_managed_initial_warehouse_size
      value: string
    - name: serverless_task_min_statement_size
      value: string
    - name: serverless_task_max_statement_size
      value: string
    - name: user_task_timeout_ms
      value: integer

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>databases</code> resource.

```sql
/*+ update */
REPLACE snowflake.database.databases
SET 
name = '{{ name }}',
kind = '{{ kind }}',
comment = '{{ comment }}',
data_retention_time_in_days = '{{ data_retention_time_in_days }}',
default_ddl_collation = '{{ default_ddl_collation }}',
log_level = '{{ log_level }}',
max_data_extension_time_in_days = '{{ max_data_extension_time_in_days }}',
suspend_task_after_num_failures = '{{ suspend_task_after_num_failures }}',
trace_level = '{{ trace_level }}',
user_task_managed_initial_warehouse_size = '{{ user_task_managed_initial_warehouse_size }}',
serverless_task_min_statement_size = '{{ serverless_task_min_statement_size }}',
serverless_task_max_statement_size = '{{ serverless_task_max_statement_size }}',
user_task_timeout_ms = '{{ user_task_timeout_ms }}'
WHERE 
name = '{{ name }}'
AND data__name = '{{ data__name }}'
AND endpoint = '{{ endpoint }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.database.databases
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
