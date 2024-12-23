---
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - job_runs
  - workflows
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>job_runs</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.job_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="attempt_number" /> | `integer` |
| <CopyableCode code="cleanup_duration" /> | `integer` |
| <CopyableCode code="cluster_instance" /> | `object` |
| <CopyableCode code="cluster_spec" /> | `object` |
| <CopyableCode code="creator_user_name" /> | `string` |
| <CopyableCode code="end_time" /> | `integer` |
| <CopyableCode code="execution_duration" /> | `integer` |
| <CopyableCode code="git_source" /> | `object` |
| <CopyableCode code="has_more" /> | `boolean` |
| <CopyableCode code="job_clusters" /> | `array` |
| <CopyableCode code="job_id" /> | `integer` |
| <CopyableCode code="job_parameters" /> | `array` |
| <CopyableCode code="job_run_id" /> | `integer` |
| <CopyableCode code="number_in_job" /> | `integer` |
| <CopyableCode code="original_attempt_run_id" /> | `integer` |
| <CopyableCode code="overriding_parameters" /> | `object` |
| <CopyableCode code="queue_duration" /> | `integer` |
| <CopyableCode code="repair_history" /> | `array` |
| <CopyableCode code="run_duration" /> | `integer` |
| <CopyableCode code="run_id" /> | `integer` |
| <CopyableCode code="run_name" /> | `string` |
| <CopyableCode code="run_page_url" /> | `string` |
| <CopyableCode code="run_type" /> | `string` |
| <CopyableCode code="schedule" /> | `object` |
| <CopyableCode code="setup_duration" /> | `integer` |
| <CopyableCode code="start_time" /> | `integer` |
| <CopyableCode code="state" /> | `object` |
| <CopyableCode code="status" /> | `object` |
| <CopyableCode code="tasks" /> | `array` |
| <CopyableCode code="trigger" /> | `string` |
| <CopyableCode code="trigger_info" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getrun" /> | `SELECT` | <CopyableCode code="run_id, deployment_name" /> | Retrieves the metadata of a run. |
| <CopyableCode code="listruns" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List runs in descending order by start time. |
| <CopyableCode code="deleterun" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes a non-active run. Returns an error if the run is active. |
| <CopyableCode code="cancelallruns" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs from being started. |
| <CopyableCode code="cancelrun" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when this request completes. |
| <CopyableCode code="exportrun" /> | `EXEC` | <CopyableCode code="run_id, deployment_name" /> | Export and retrieve the job run task. |
| <CopyableCode code="repairrun" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job and task settings, and can be viewed in the history for the original job run. |

## `SELECT` examples

<Tabs
    defaultValue="listruns"
    values={[
        { label: 'job_runs (listruns)', value: 'listruns' },
        { label: 'job_runs (getrun)', value: 'getrun' }
    ]
}>
<TabItem value="listruns">

```sql
SELECT
description,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
creator_user_name,
end_time,
execution_duration,
git_source,
has_more,
job_clusters,
job_id,
job_parameters,
job_run_id,
number_in_job,
original_attempt_run_id,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_id,
run_name,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
FROM databricks_workspace.workflows.job_runs
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getrun">

```sql
SELECT
description,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
creator_user_name,
end_time,
execution_duration,
git_source,
has_more,
job_clusters,
job_id,
job_parameters,
job_run_id,
number_in_job,
original_attempt_run_id,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_id,
run_name,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
FROM databricks_workspace.workflows.job_runs
WHERE run_id = '{{ run_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>job_runs</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workflows.job_runs
WHERE deployment_name = '{{ deployment_name }}';
```
