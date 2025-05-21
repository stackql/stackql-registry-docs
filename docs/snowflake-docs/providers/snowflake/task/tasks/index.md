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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An ID for the current task. |
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="allow_overlapping_execution" /> | `boolean` | Specifies whether to allow multiple instances of the DAG to run concurrently. |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the task. |
| <CopyableCode code="condition" /> | `string` | Specifies a Boolean SQL expression condition; multiple conditions joined with AND/OR are supported |
| <CopyableCode code="config" /> | `object` | Task Config |
| <CopyableCode code="created_on" /> | `string` | The time the task was created on. |
| <CopyableCode code="database_name" /> | `string` | The name of the parent database for the task. |
| <CopyableCode code="definition" /> | `string` | The SQL definition for the task. Any one of single SQL statement, call to stored procedure, or procedural logic using Snowflake scripting. |
| <CopyableCode code="error_integration" /> | `string` | Specifies the name of the notification integration used to communicate with Amazon SNS, MS Azure Event Grid, or Google Pub/Sub. |
| <CopyableCode code="finalize" /> | `string` | Specifies the name of the root task that the finalizer task is associated with. |
| <CopyableCode code="last_committed_on" /> | `string` | The time the task was last committed on. |
| <CopyableCode code="last_suspended_on" /> | `string` | The time the task was last suspended on. |
| <CopyableCode code="owner" /> | `string` | The role that owns the task. |
| <CopyableCode code="owner_role_type" /> | `string` | The role type of the task owner. |
| <CopyableCode code="predecessors" /> | `array` | Specifies one or more predecessor tasks for the current task |
| <CopyableCode code="schedule" /> | `object` | Specifies the schedule for periodically running the task. |
| <CopyableCode code="schema_name" /> | `string` | The name of the parent schema for the task. |
| <CopyableCode code="serverless_task_max_statement_size" /> | `string` | Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks. |
| <CopyableCode code="serverless_task_min_statement_size" /> | `string` | Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks. |
| <CopyableCode code="session_parameters" /> | `object` | Session Parameters for the task at runtime. |
| <CopyableCode code="state" /> | `string` | The state of the task. Must be one of started or suspended. |
| <CopyableCode code="suspend_task_after_num_failures" /> | `integer` | Specifies the number of consecutive failed task runs after which the current task is suspended automatically. |
| <CopyableCode code="target_completion_interval" /> | `object` | A schedule for executing a task at specified intervals of minutes. |
| <CopyableCode code="task_auto_retry_attempts" /> | `integer` | Root task settable only. Specifies the number of automatic task graph retry attempts. Valid range is 0 to 30. When not specified, no retry would happen. |
| <CopyableCode code="task_relations" /> | `string` | Displays the relationship between the root task and its corresponding finalizer tasks. |
| <CopyableCode code="user_task_managed_initial_warehouse_size" /> | `string` | Specifies the size of the compute resources to provision for the first run of the task. This parameter only applies to serverless tasks. |
| <CopyableCode code="user_task_timeout_ms" /> | `integer` | Specifies the time limit on a single run of the task before it times out (in milliseconds). |
| <CopyableCode code="warehouse" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_task" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Fetch a task using the describe command output. |
| <CopyableCode code="list_tasks" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | Lists tasks under the database and schema, with show options as query parameters. |
| <CopyableCode code="create_task" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__definition, data__name, endpoint" /> | Create a task, with standard create modifiers as query parameters. See the Task component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_task" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Delete a task with the task name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful. |
| <CopyableCode code="create_or_alter_task" /> | `REPLACE` | <CopyableCode code="database_name, name, schema_name, data__definition, data__name, endpoint" /> | Create a (or alter an existing) task. Even if the operation is just an alter, the full property set must be provided. |
| <CopyableCode code="execute_task" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Execute a task -- this is equivalent to EXECUTE IMMEDIATE. |
| <CopyableCode code="resume_task" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Resumes a suspended task object. This is equivalento an ALTER TASK ... RESUME. |
| <CopyableCode code="suspend_task" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Suspends a running task. This is equivalent to an ALTER TASK ... SUSPEND. |

## `SELECT` examples

Lists tasks under the database and schema, with show options as query parameters.


```sql
SELECT
id,
name,
allow_overlapping_execution,
comment,
condition,
config,
created_on,
database_name,
definition,
error_integration,
finalize,
last_committed_on,
last_suspended_on,
owner,
owner_role_type,
predecessors,
schedule,
schema_name,
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
WHERE database_name = '{{ database_name }}' AND schema_name = '{{ schema_name }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tasks</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.task.tasks (
endpoint,
schema_name,
data__definition,
database_name,
data__name
)
SELECT 
'{ database_name }',
'{ name }',
'{ endpoint }',
'{ schema_name }',
'{ definition }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: tasks
  props:
  - name: database_name
    value: string
  - name: schema_name
    value: string
  - name: data__definition
    value: string
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>tasks</code> resource.

```sql
/*+ update */
REPLACE snowflake.task.tasks
SET 

WHERE 
database_name = '{ database_name }' AND name = '{ name }' AND schema_name = '{ schema_name }' AND data__definition = '{ data__definition }' AND data__name = '{ data__name }' AND endpoint = '{ endpoint }';
```

## `DELETE` example

Deletes the specified <code>tasks</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.task.tasks
WHERE database_name = '{ database_name }' AND name = '{ name }' AND schema_name = '{ schema_name }' AND endpoint = '{ endpoint }';
```
