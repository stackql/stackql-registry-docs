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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="budget" /> | `string` | Budget that defines a monthly spending limit on the compute costs for a Snowflake account or a custom group of Snowflake objects. |
| <CopyableCode code="comment" /> | `string` | Optional comment in which to store information related to the schema. |
| <CopyableCode code="created_on" /> | `string` | Date and time the schema was created. |
| <CopyableCode code="data_retention_time_in_days" /> | `integer` | Number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the default Time Travel retention time for all tables created in the schema |
| <CopyableCode code="database_name" /> | `string` | Database that the schema belongs to |
| <CopyableCode code="default_ddl_collation" /> | `string` | Specifies a default collation specification for all tables added to the schema. You an override the default at the schema and individual table levels. |
| <CopyableCode code="dropped_on" /> | `string` | Date and time the schema was dropped. |
| <CopyableCode code="is_current" /> | `boolean` | Current schema for the session. |
| <CopyableCode code="is_default" /> | `boolean` | Default schema for a user. |
| <CopyableCode code="kind" /> | `string` | Schema type, permanent (default) or transient. |
| <CopyableCode code="log_level" /> | `string` | Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`. |
| <CopyableCode code="managed_access" /> | `boolean` | Whether this schema is a managed access schema that centralizes privilege management with the schema owner. |
| <CopyableCode code="max_data_extension_time_in_days" /> | `integer` | Maximum number of days for which Snowflake can extend the data retention period for tables in the schema to prevent streams on the tables from becoming stale. |
| <CopyableCode code="options" /> | `string` |  |
| <CopyableCode code="owner" /> | `string` | Name of the role that owns the schema. |
| <CopyableCode code="owner_role_type" /> | `string` | Type of role that owns the object, either `ROLE` or `DATABASE_ROLE`. |
| <CopyableCode code="pipe_execution_paused" /> | `boolean` | Whether pipe execution is paused. |
| <CopyableCode code="retention_time" /> | `integer` | Number of days that historical data is retained for Time Travel. |
| <CopyableCode code="serverless_task_max_statement_size" /> | `string` | Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. |
| <CopyableCode code="serverless_task_min_statement_size" /> | `string` | Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. |
| <CopyableCode code="suspend_task_after_num_failures" /> | `integer` | Specifies the number of consecutive failed task runs after which the current task is suspended automatically. |
| <CopyableCode code="trace_level" /> | `string` | How trace events are ingested into the event table. Currently, Snowflake supports only `ALWAYS`, `ON_EVENT`, and `OFF`. |
| <CopyableCode code="user_task_managed_initial_warehouse_size" /> | `string` | Size of the compute resources to provision for the first run of the serverless task, before a task history is available for Snowflake to determine an ideal size. |
| <CopyableCode code="user_task_timeout_ms" /> | `integer` | Time limit, in milliseconds, for a single run of the task before it times out. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_schema" /> | `SELECT` | <CopyableCode code="database_name, name, endpoint" /> | - | Fetches a schema. |
| <CopyableCode code="list_schemas" /> | `SELECT` | <CopyableCode code="database_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" />, <CopyableCode code="history" /> | Lists the accessible schemas. |
| <CopyableCode code="create_schema" /> | `INSERT` | <CopyableCode code="database_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="kind" /> | Creates a schema, with modifiers as query parameters. You must provide the full schema definition when creating a schema. |
| <CopyableCode code="delete_schema" /> | `DELETE` | <CopyableCode code="database_name, name, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="restrict" /> | Deletes the specified schema. If you enable the `ifExists` parameter, the operation succeeds even if the schema does not exist. Otherwise, a 404 failure is returned if the schema does not exist. if the drop is unsuccessful. |
| <CopyableCode code="create_or_alter_schema" /> | `REPLACE` | <CopyableCode code="database_name, name, data__name, endpoint" /> | <CopyableCode code="kind" /> | Creates a new, or alters an existing, schema. You must provide the full schema definition even when altering an existing schema. |
| <CopyableCode code="clone_schema" /> | `EXEC` | <CopyableCode code="database_name, name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="kind" />, <CopyableCode code="targetDatabase" /> | Clones an existing schema, with modifiers as query parameters. You must provide the full schema definition when cloning an existing schema. |
| <CopyableCode code="undrop_schema" /> | `EXEC` | <CopyableCode code="database_name, name, endpoint" /> | - | Undrops schema. |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="history" /> | Whether to include dropped schemas that have not yet been purged. Default: `false`. | `boolean` | `false` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="kind" /> | Type of schema to create. Currently, Snowflake supports only `transient` and `permanent` (also represented by the empty string). | `string` | `` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="restrict" /> | Whether to drop the schema if foreign keys exist that reference any tables in the schema. - `true`: Return a warning about existing foreign key references and don't drop the schema. - `false`: Drop the schema and all objects in the database, including tables with primary or unique keys that are referenced by foreign keys in other tables. Default: `false`. | `boolean` | `false` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |
| <CopyableCode code="targetDatabase" /> | Database of the newly created schema. Defaults to the source schema's database. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_schemas"
    values={[
        { label: 'list_schemas', value: 'list_schemas' },
        { label: 'fetch_schema', value: 'fetch_schema' }
    ]
}>
<TabItem value="list_schemas">

Lists the accessible schemas.

```sql
SELECT
name,
budget,
comment,
created_on,
data_retention_time_in_days,
database_name,
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
WHERE database_name = '{{ database_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_schema">

Fetches a schema.

```sql
SELECT
name,
budget,
comment,
created_on,
data_retention_time_in_days,
database_name,
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
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schemas</code> resource.

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
endpoint
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
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.schema.schemas (
data__name,
database_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ database_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: schemas
  props:
    - name: database_name
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
      description: >-
        A Snowflake object identifier. If the identifier contains spaces or
        special characters, the entire string must be enclosed in double quotes.
        Identifiers enclosed in double quotes are also case-sensitive.
    - name: kind
      value: string
      description: Schema type, permanent (default) or transient.
    - name: comment
      value: string
      description: Optional comment in which to store information related to the schema.
    - name: managed_access
      value: boolean
      description: >-
        Whether this schema is a managed access schema that centralizes
        privilege management with the schema owner.
    - name: data_retention_time_in_days
      value: integer
      description: >-
        Number of days for which Time Travel actions (CLONE and UNDROP) can be
        performed on the schema, as well as specifying the default Time Travel
        retention time for all tables created in the schema
    - name: default_ddl_collation
      value: string
      description: >-
        Specifies a default collation specification for all tables added to the
        schema. You an override the default at the schema and individual table
        levels.
    - name: log_level
      value: string
      description: >-
        Severity level of messages that should be ingested and made available in
        the active event table. Currently, Snowflake supports only `TRACE`,
        `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.
    - name: pipe_execution_paused
      value: boolean
      description: Whether pipe execution is paused.
    - name: max_data_extension_time_in_days
      value: integer
      description: >-
        Maximum number of days for which Snowflake can extend the data retention
        period for tables in the schema to prevent streams on the tables from
        becoming stale.
    - name: suspend_task_after_num_failures
      value: integer
      description: >-
        Specifies the number of consecutive failed task runs after which the
        current task is suspended automatically.
    - name: trace_level
      value: string
      description: >-
        How trace events are ingested into the event table. Currently, Snowflake
        supports only `ALWAYS`, `ON_EVENT`, and `OFF`.
    - name: user_task_managed_initial_warehouse_size
      value: string
      description: >-
        Size of the compute resources to provision for the first run of the
        serverless task, before a task history is available for Snowflake to
        determine an ideal size.
    - name: serverless_task_min_statement_size
      value: string
      description: >-
        Specifies the minimum allowed warehouse size for the serverless task.
        Minimum XSMALL, Maximum XXLARGE.
    - name: serverless_task_max_statement_size
      value: string
      description: >-
        Specifies the maximum allowed warehouse size for the serverless task.
        Minimum XSMALL, Maximum XXLARGE.
    - name: user_task_timeout_ms
      value: integer
      description: >-
        Time limit, in milliseconds, for a single run of the task before it
        times out.
```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>schemas</code> resource.

```sql
/*+ update */
REPLACE snowflake.schema.schemas
SET 
name = '{{ name }}',
kind = '{{ kind }}',
comment = '{{ comment }}',
managed_access = {{ managed_access }},
data_retention_time_in_days = {{ data_retention_time_in_days }},
default_ddl_collation = '{{ default_ddl_collation }}',
log_level = '{{ log_level }}',
pipe_execution_paused = {{ pipe_execution_paused }},
max_data_extension_time_in_days = {{ max_data_extension_time_in_days }},
suspend_task_after_num_failures = {{ suspend_task_after_num_failures }},
trace_level = '{{ trace_level }}',
user_task_managed_initial_warehouse_size = '{{ user_task_managed_initial_warehouse_size }}',
serverless_task_min_statement_size = '{{ serverless_task_min_statement_size }}',
serverless_task_max_statement_size = '{{ serverless_task_max_statement_size }}',
user_task_timeout_ms = {{ user_task_timeout_ms }}
WHERE 
database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND data__name = '{{ data__name }}'
AND endpoint = '{{ endpoint }}';
```

## `DELETE` example

Deletes the specified <code>schemas</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.schema.schemas
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
