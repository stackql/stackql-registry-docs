--- 
title: current_graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - current_graphs
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

Creates, updates, deletes, gets or lists a <code>current_graphs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>current_graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.task.current_graphs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_current_graphs_deprecated"
    values={[
        { label: 'get_current_graphs_deprecated', value: 'get_current_graphs_deprecated' },
        { label: 'get_current_graphs', value: 'get_current_graphs' }
    ]}
>
<TabItem value="get_current_graphs_deprecated">

A task run executing a standalone task or a DAG of tasks starting from the root task.

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
    <td><CopyableCode code="root_task_id" /></td>
    <td><code>string</code></td>
    <td>The unique task ID for the root task.</td>
</tr>
<tr>
    <td><CopyableCode code="run_id" /></td>
    <td><code>integer</code></td>
    <td>The unique ID for the current task run.</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the current database for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="first_error_task_name" /></td>
    <td><code>string</code></td>
    <td>The name of the first task throwing an error in the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="root_task_name" /></td>
    <td><code>string</code></td>
    <td>The name of the root task in the current task run.</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the current schema for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="completed_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task run was last completed.</td>
</tr>
<tr>
    <td><CopyableCode code="first_error_code" /></td>
    <td><code>integer</code></td>
    <td>The first error code thrown in the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="first_error_message" /></td>
    <td><code>string</code></td>
    <td>The first error message thrown in the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="graph_version" /></td>
    <td><code>integer</code></td>
    <td>The current version of the DAG on the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="next_scheduled_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The next upcoming time for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="query_start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the task run query.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduled_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled time for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the task run.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_current_graphs">

A task run executing a standalone task or a DAG of tasks starting from the root task.

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
    <td><CopyableCode code="root_task_id" /></td>
    <td><code>string</code></td>
    <td>The unique task ID for the root task.</td>
</tr>
<tr>
    <td><CopyableCode code="run_id" /></td>
    <td><code>integer</code></td>
    <td>The unique ID for the current task run.</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the current database for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="first_error_task_name" /></td>
    <td><code>string</code></td>
    <td>The name of the first task throwing an error in the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="root_task_name" /></td>
    <td><code>string</code></td>
    <td>The name of the root task in the current task run.</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the current schema for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="completed_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task run was last completed.</td>
</tr>
<tr>
    <td><CopyableCode code="first_error_code" /></td>
    <td><code>integer</code></td>
    <td>The first error code thrown in the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="first_error_message" /></td>
    <td><code>string</code></td>
    <td>The first error message thrown in the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="graph_version" /></td>
    <td><code>integer</code></td>
    <td>The current version of the DAG on the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="next_scheduled_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The next upcoming time for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="query_start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the task run query.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduled_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled time for the task run.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the task run.</td>
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
    <td><a href="#get_current_graphs_deprecated"><CopyableCode code="get_current_graphs_deprecated" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-resultLimit">resultLimit</a></td>
    <td>This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days.</td>
</tr>
<tr>
    <td><a href="#get_current_graphs"><CopyableCode code="get_current_graphs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-resultLimit">resultLimit</a></td>
    <td>This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days.</td>
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
<tr id="parameter-resultLimit">
    <td><CopyableCode code="resultLimit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_current_graphs_deprecated"
    values={[
        { label: 'get_current_graphs_deprecated', value: 'get_current_graphs_deprecated' },
        { label: 'get_current_graphs', value: 'get_current_graphs' }
    ]}
>
<TabItem value="get_current_graphs_deprecated">

This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days.

```sql
SELECT
root_task_id,
run_id,
database_name,
first_error_task_name,
root_task_name,
schema_name,
completed_time,
first_error_code,
first_error_message,
graph_version,
next_scheduled_time,
query_start_time,
scheduled_time,
state
FROM snowflake.task.current_graphs
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND resultLimit = '{{ resultLimit }}';
```
</TabItem>
<TabItem value="get_current_graphs">

This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days.

```sql
SELECT
root_task_id,
run_id,
database_name,
first_error_task_name,
root_task_name,
schema_name,
completed_time,
first_error_code,
first_error_message,
graph_version,
next_scheduled_time,
query_start_time,
scheduled_time,
state
FROM snowflake.task.current_graphs
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND resultLimit = '{{ resultLimit }}';
```
</TabItem>
</Tabs>
