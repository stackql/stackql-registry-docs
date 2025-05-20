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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="completed_time" /> | `string` | The time this task run was last completed. |
| <CopyableCode code="database_name" /> | `string` | The name of the current database for the task run. |
| <CopyableCode code="first_error_code" /> | `integer` | The first error code thrown in the task run. |
| <CopyableCode code="first_error_message" /> | `string` | The first error message thrown in the task run. |
| <CopyableCode code="first_error_task_name" /> | `string` | The name of the first task throwing an error in the task run. |
| <CopyableCode code="graph_version" /> | `integer` | The current version of the DAG on the task run. |
| <CopyableCode code="next_scheduled_time" /> | `string` | The next upcoming time for the task run. |
| <CopyableCode code="query_start_time" /> | `string` | The start time for the task run query. |
| <CopyableCode code="root_task_id" /> | `string` | The unique task ID for the root task. |
| <CopyableCode code="root_task_name" /> | `string` | The name of the root task in the current task run. |
| <CopyableCode code="run_id" /> | `integer` | The unique ID for the current task run. |
| <CopyableCode code="scheduled_time" /> | `string` | The scheduled time for the task run. |
| <CopyableCode code="schema_name" /> | `string` | The name of the current schema for the task run. |
| <CopyableCode code="state" /> | `string` | The current state of the task run. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_current_graphs" /> | `SELECT` | <CopyableCode code="database, name, schema, endpoint" /> | This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days. |
| <CopyableCode code="get_current_graphs_deprecated" /> | `SELECT` | <CopyableCode code="database, name, schema, endpoint" /> | This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days. |

## `SELECT` examples

This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days.


```sql
SELECT
completed_time,
database_name,
first_error_code,
first_error_message,
first_error_task_name,
graph_version,
next_scheduled_time,
query_start_time,
root_task_id,
root_task_name,
run_id,
scheduled_time,
schema_name,
state
FROM snowflake.task.current_graphs
WHERE database = '{{ database }}' AND name = '{{ name }}' AND schema = '{{ schema }}' AND endpoint = '{{ endpoint }}';
```