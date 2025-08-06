--- 
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - task
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.task.tasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_tasks"
    values={[
        { label: 'list_tasks', value: 'list_tasks' },
        { label: 'fetch_task', value: 'fetch_task' }
    ]}
>
<TabItem value="list_tasks">

A Snowflake task, used to execute SQL code.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>An ID for the current task.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the parent database for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the parent schema for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="allow_overlapping_execution" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to allow multiple instances of the DAG to run concurrently.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>Specifies a Boolean SQL expression condition; multiple conditions joined with AND/OR are supported</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>Task Config</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the task was created on.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>string</code></td>
    <td>The SQL definition for the task. Any one of single SQL statement, call to stored procedure, or procedural logic using Snowflake scripting.</td>
</tr>
<tr>
    <td><CopyableCode code="error_integration" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the notification integration used to communicate with Amazon SNS, MS Azure Event Grid, or Google Pub/Sub.</td>
</tr>
<tr>
    <td><CopyableCode code="finalize" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the root task that the finalizer task is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="last_committed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the task was last committed on.</td>
</tr>
<tr>
    <td><CopyableCode code="last_suspended_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the task was last suspended on.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The role that owns the task.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The role type of the task owner.</td>
</tr>
<tr>
    <td><CopyableCode code="predecessors" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more predecessor tasks for the current task</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically running the task.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_max_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_min_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="session_parameters" /></td>
    <td><code>object</code></td>
    <td>Session Parameters for the task at runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the task. Must be one of started or suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend_task_after_num_failures" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of consecutive failed task runs after which the current task is suspended automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="target_completion_interval" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically running the task.</td>
</tr>
<tr>
    <td><CopyableCode code="task_auto_retry_attempts" /></td>
    <td><code>integer</code></td>
    <td>Root task settable only. Specifies the number of automatic task graph retry attempts. Valid range is 0 to 30. When not specified, no retry would happen.</td>
</tr>
<tr>
    <td><CopyableCode code="task_relations" /></td>
    <td><code>string</code></td>
    <td>Displays the relationship between the root task and its corresponding finalizer tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_managed_initial_warehouse_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the size of the compute resources to provision for the first run of the task. This parameter only applies to serverless tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_timeout_ms" /></td>
    <td><code>integer</code></td>
    <td>Specifies the time limit on a single run of the task before it times out (in milliseconds).</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_task">

A Snowflake task, used to execute SQL code.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>An ID for the current task.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the parent database for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the parent schema for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="allow_overlapping_execution" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to allow multiple instances of the DAG to run concurrently.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>Specifies a Boolean SQL expression condition; multiple conditions joined with AND/OR are supported</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>Task Config</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the task was created on.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>string</code></td>
    <td>The SQL definition for the task. Any one of single SQL statement, call to stored procedure, or procedural logic using Snowflake scripting.</td>
</tr>
<tr>
    <td><CopyableCode code="error_integration" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the notification integration used to communicate with Amazon SNS, MS Azure Event Grid, or Google Pub/Sub.</td>
</tr>
<tr>
    <td><CopyableCode code="finalize" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the root task that the finalizer task is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="last_committed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the task was last committed on.</td>
</tr>
<tr>
    <td><CopyableCode code="last_suspended_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the task was last suspended on.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The role that owns the task.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The role type of the task owner.</td>
</tr>
<tr>
    <td><CopyableCode code="predecessors" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more predecessor tasks for the current task</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically running the task.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_max_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="serverless_task_min_statement_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="session_parameters" /></td>
    <td><code>object</code></td>
    <td>Session Parameters for the task at runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the task. Must be one of started or suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend_task_after_num_failures" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of consecutive failed task runs after which the current task is suspended automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="target_completion_interval" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically running the task.</td>
</tr>
<tr>
    <td><CopyableCode code="task_auto_retry_attempts" /></td>
    <td><code>integer</code></td>
    <td>Root task settable only. Specifies the number of automatic task graph retry attempts. Valid range is 0 to 30. When not specified, no retry would happen.</td>
</tr>
<tr>
    <td><CopyableCode code="task_relations" /></td>
    <td><code>string</code></td>
    <td>Displays the relationship between the root task and its corresponding finalizer tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_managed_initial_warehouse_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the size of the compute resources to provision for the first run of the task. This parameter only applies to serverless tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="user_task_timeout_ms" /></td>
    <td><code>integer</code></td>
    <td>Specifies the time limit on a single run of the task before it times out (in milliseconds).</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
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
    <td><a href="#list_tasks"><CopyableCode code="list_tasks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-rootOnly">rootOnly</a>, <a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a></td>
    <td>Lists tasks under the database and schema, with show options as query parameters.</td>
</tr>
<tr>
    <td><a href="#fetch_task"><CopyableCode code="fetch_task" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch a task using the describe command output.</td>
</tr>
<tr>
    <td><a href="#create_task"><CopyableCode code="create_task" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create a task, with standard create modifiers as query parameters. See the Task component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_task"><CopyableCode code="create_or_alter_task" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Create a (or alter an existing) task. Even if the operation is just an alter, the full property set must be provided.</td>
</tr>
<tr>
    <td><a href="#delete_task"><CopyableCode code="delete_task" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete a task with the task name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#execute_task"><CopyableCode code="execute_task" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-asyncExec">asyncExec</a>, <a href="#parameter-retryLast">retryLast</a></td>
    <td>Execute a task -- this is equivalent to EXECUTE IMMEDIATE.</td>
</tr>
<tr>
    <td><a href="#resume_task"><CopyableCode code="resume_task" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Resumes a suspended task object. This is equivalento an ALTER TASK ... RESUME.</td>
</tr>
<tr>
    <td><a href="#suspend_task"><CopyableCode code="suspend_task" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Suspends a running task. This is equivalent to an ALTER TASK ... SUSPEND.</td>
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
<tr id="parameter-asyncExec">
    <td><CopyableCode code="asyncExec" /></td>
    <td><code>boolean</code></td>
    <td>Asynchronous execution enable/disable. Default is disable. (default: false)</td>
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
<tr id="parameter-retryLast">
    <td><CopyableCode code="retryLast" /></td>
    <td><code>boolean</code></td>
    <td>Retry the last failed run of the DAG. (default: false)</td>
</tr>
<tr id="parameter-rootOnly">
    <td><CopyableCode code="rootOnly" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter to filter the command output to return only root resources (resources with no predecessors). (example: false, default: false)</td>
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
    defaultValue="list_tasks"
    values={[
        { label: 'list_tasks', value: 'list_tasks' },
        { label: 'fetch_task', value: 'fetch_task' }
    ]}
>
<TabItem value="list_tasks">

Lists tasks under the database and schema, with show options as query parameters.

```sql
SELECT
id,
name,
database_name,
schema_name,
allow_overlapping_execution,
comment,
condition,
config,
created_on,
definition,
error_integration,
finalize,
last_committed_on,
last_suspended_on,
owner,
owner_role_type,
predecessors,
schedule,
serverless_task_max_statement_size,
serverless_task_min_statement_size,
session_parameters,
state,
suspend_task_after_num_failures,
target_completion_interval,
task_auto_retry_attempts,
task_relations,
user_task_managed_initial_warehouse_size,
user_task_timeout_ms,
warehouse
FROM snowflake.task.tasks
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND rootOnly = '{{ rootOnly }}'
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}';
```
</TabItem>
<TabItem value="fetch_task">

Fetch a task using the describe command output.

```sql
SELECT
id,
name,
database_name,
schema_name,
allow_overlapping_execution,
comment,
condition,
config,
created_on,
definition,
error_integration,
finalize,
last_committed_on,
last_suspended_on,
owner,
owner_role_type,
predecessors,
schedule,
serverless_task_max_statement_size,
serverless_task_min_statement_size,
session_parameters,
state,
suspend_task_after_num_failures,
target_completion_interval,
task_auto_retry_attempts,
task_relations,
user_task_managed_initial_warehouse_size,
user_task_timeout_ms,
warehouse
FROM snowflake.task.tasks
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_task"
    values={[
        { label: 'create_task', value: 'create_task' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_task">

Create a task, with standard create modifiers as query parameters. See the Task component definition for what is required to be provided in the request body.

```sql
INSERT INTO snowflake.task.tasks (
data__name,
data__warehouse,
data__schedule,
data__comment,
data__finalize,
data__task_auto_retry_attempts,
data__config,
data__session_parameters,
data__definition,
data__predecessors,
data__user_task_managed_initial_warehouse_size,
data__target_completion_interval,
data__serverless_task_min_statement_size,
data__serverless_task_max_statement_size,
data__user_task_timeout_ms,
data__suspend_task_after_num_failures,
data__condition,
data__allow_overlapping_execution,
data__error_integration,
database_name,
schema_name,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ warehouse }}',
'{{ schedule }}',
'{{ comment }}',
'{{ finalize }}',
{{ task_auto_retry_attempts }},
'{{ config }}',
'{{ session_parameters }}',
'{{ definition }}',
'{{ predecessors }}',
'{{ user_task_managed_initial_warehouse_size }}',
'{{ target_completion_interval }}',
'{{ serverless_task_min_statement_size }}',
'{{ serverless_task_max_statement_size }}',
{{ user_task_timeout_ms }},
{{ suspend_task_after_num_failures }},
'{{ condition }}',
{{ allow_overlapping_execution }},
'{{ error_integration }}',
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
- name: tasks
  props:
    - name: database_name
      value: string
      description: Required parameter for the tasks resource.
    - name: schema_name
      value: string
      description: Required parameter for the tasks resource.
    - name: endpoint
      value: string
      description: Required parameter for the tasks resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: warehouse
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: schedule
      value: object
      description: >
        Specifies the schedule for periodically running the task.
        
    - name: comment
      value: string
      description: >
        Specifies a comment for the task.
        
    - name: finalize
      value: string
      description: >
        Specifies the name of the root task that the finalizer task is associated with.
        
    - name: task_auto_retry_attempts
      value: integer
      description: >
        Root task settable only. Specifies the number of automatic task graph retry attempts. Valid range is 0 to 30. When not specified, no retry would happen.
        
    - name: config
      value: object
      description: >
        Task Config
        
    - name: session_parameters
      value: object
      description: >
        Session Parameters for the task at runtime.
        
    - name: definition
      value: string
      description: >
        The SQL definition for the task. Any one of single SQL statement, call to stored procedure, or procedural logic using Snowflake scripting.
        
    - name: predecessors
      value: array
      description: >
        Specifies one or more predecessor tasks for the current task
        
    - name: user_task_managed_initial_warehouse_size
      value: string
      description: >
        Specifies the size of the compute resources to provision for the first run of the task. This parameter only applies to serverless tasks.
        
    - name: target_completion_interval
      value: object
      description: >
        Specifies the schedule for periodically running the task.
        
    - name: serverless_task_min_statement_size
      value: string
      description: >
        Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.
        
    - name: serverless_task_max_statement_size
      value: string
      description: >
        Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.
        
    - name: user_task_timeout_ms
      value: integer
      description: >
        Specifies the time limit on a single run of the task before it times out (in milliseconds).
        
    - name: suspend_task_after_num_failures
      value: integer
      description: >
        Specifies the number of consecutive failed task runs after which the current task is suspended automatically.
        
    - name: condition
      value: string
      description: >
        Specifies a Boolean SQL expression condition; multiple conditions joined with AND/OR are supported
        
    - name: allow_overlapping_execution
      value: boolean
      description: >
        Specifies whether to allow multiple instances of the DAG to run concurrently.
        
    - name: error_integration
      value: string
      description: >
        Specifies the name of the notification integration used to communicate with Amazon SNS, MS Azure Event Grid, or Google Pub/Sub.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_task"
    values={[
        { label: 'create_or_alter_task', value: 'create_or_alter_task' }
    ]}
>
<TabItem value="create_or_alter_task">

Create a (or alter an existing) task. Even if the operation is just an alter, the full property set must be provided.

```sql
REPLACE snowflake.task.tasks
SET 
data__name = '{{ name }}',
data__warehouse = '{{ warehouse }}',
data__schedule = '{{ schedule }}',
data__comment = '{{ comment }}',
data__finalize = '{{ finalize }}',
data__task_auto_retry_attempts = {{ task_auto_retry_attempts }},
data__config = '{{ config }}',
data__session_parameters = '{{ session_parameters }}',
data__definition = '{{ definition }}',
data__predecessors = '{{ predecessors }}',
data__user_task_managed_initial_warehouse_size = '{{ user_task_managed_initial_warehouse_size }}',
data__target_completion_interval = '{{ target_completion_interval }}',
data__serverless_task_min_statement_size = '{{ serverless_task_min_statement_size }}',
data__serverless_task_max_statement_size = '{{ serverless_task_max_statement_size }}',
data__user_task_timeout_ms = {{ user_task_timeout_ms }},
data__suspend_task_after_num_failures = {{ suspend_task_after_num_failures }},
data__condition = '{{ condition }}',
data__allow_overlapping_execution = {{ allow_overlapping_execution }},
data__error_integration = '{{ error_integration }}'
WHERE 
database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required
AND data__definition = '{{ definition }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_task"
    values={[
        { label: 'delete_task', value: 'delete_task' }
    ]}
>
<TabItem value="delete_task">

Delete a task with the task name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

```sql
DELETE FROM snowflake.task.tasks
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
    defaultValue="execute_task"
    values={[
        { label: 'execute_task', value: 'execute_task' },
        { label: 'resume_task', value: 'resume_task' },
        { label: 'suspend_task', value: 'suspend_task' }
    ]}
>
<TabItem value="execute_task">

Execute a task -- this is equivalent to EXECUTE IMMEDIATE.

```sql
EXEC snowflake.task.tasks.execute_task 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@asyncExec={{ asyncExec }}, 
@retryLast={{ retryLast }};
```
</TabItem>
<TabItem value="resume_task">

Resumes a suspended task object. This is equivalento an ALTER TASK ... RESUME.

```sql
EXEC snowflake.task.tasks.resume_task 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="suspend_task">

Suspends a running task. This is equivalent to an ALTER TASK ... SUSPEND.

```sql
EXEC snowflake.task.tasks.suspend_task 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
