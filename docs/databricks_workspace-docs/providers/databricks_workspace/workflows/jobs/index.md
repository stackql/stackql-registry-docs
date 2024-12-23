---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - jobs
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

Operations on a <code>jobs</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="created_time" /> | `integer` |
| <CopyableCode code="creator_user_name" /> | `string` |
| <CopyableCode code="has_more" /> | `boolean` |
| <CopyableCode code="job_id" /> | `integer` |
| <CopyableCode code="settings" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="job_id, deployment_name" /> | Retrieves the details for a single job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Retrieves a list of jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a new job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes a job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Add, update, or remove specific settings of an existing job. Use the |
| <CopyableCode code="reset" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Overwrite all settings for the given job. Use the |
| <CopyableCode code="runnow" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Run a job and return the |
| <CopyableCode code="submit" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Runs submitted using this endpoint don’t display in the UI. Use the |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'jobs (list)', value: 'list' },
        { label: 'jobs (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
created_time,
creator_user_name,
has_more,
job_id,
settings
FROM databricks_workspace.workflows.jobs
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
created_time,
creator_user_name,
has_more,
job_id,
settings
FROM databricks_workspace.workflows.jobs
WHERE job_id = '{{ job_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'jobs', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.workflows.jobs (
deployment_name,
data__name,
data__description,
data__email_notifications,
data__webhook_notifications,
data__notification_settings,
data__timeout_seconds,
data__health,
data__schedule,
data__trigger,
data__continuous,
data__max_concurrent_runs,
data__tasks,
data__job_clusters,
data__git_source,
data__tags,
data__format,
data__queue,
data__parameters,
data__run_as,
data__edit_mode,
data__deployment,
data__environments,
data__access_control_list
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ description }}',
'{{ email_notifications }}',
'{{ webhook_notifications }}',
'{{ notification_settings }}',
'{{ timeout_seconds }}',
'{{ health }}',
'{{ schedule }}',
'{{ trigger }}',
'{{ continuous }}',
'{{ max_concurrent_runs }}',
'{{ tasks }}',
'{{ job_clusters }}',
'{{ git_source }}',
'{{ tags }}',
'{{ format }}',
'{{ queue }}',
'{{ parameters }}',
'{{ run_as }}',
'{{ edit_mode }}',
'{{ deployment }}',
'{{ environments }}',
'{{ access_control_list }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: A multitask job
  - name: description
    value: This job contain multiple tasks that are required to produce the weekly
      shark sightings report.
  - name: email_notifications
    value:
      on_start:
      - user.name@databricks.com
      on_success:
      - user.name@databricks.com
      on_failure:
      - user.name@databricks.com
      on_duration_warning_threshold_exceeded:
      - user.name@databricks.com
      on_streaming_backlog_exceeded:
      - user.name@databricks.com
      no_alert_for_skipped_runs: false
  - name: webhook_notifications
    value:
      on_start:
      - - id: 0481e838-0a59-4eff-9541-a4ca6f149574
      on_success:
      - - id: 0481e838-0a59-4eff-9541-a4ca6f149574
      on_failure:
      - - id: 0481e838-0a59-4eff-9541-a4ca6f149574
      on_duration_warning_threshold_exceeded:
      - - id: 0481e838-0a59-4eff-9541-a4ca6f149574
      on_streaming_backlog_exceeded:
      - - id: 0481e838-0a59-4eff-9541-a4ca6f149574
  - name: notification_settings
    value:
      no_alert_for_skipped_runs: false
      no_alert_for_canceled_runs: false
  - name: timeout_seconds
    value: 86400
  - name: health
    value:
      rules:
      - metric: RUN_DURATION_SECONDS
        op: GREATER_THAN
        value: 10
  - name: schedule
    value:
      quartz_cron_expression: 20 30 * * * ?
      timezone_id: Europe/London
      pause_status: UNPAUSED
  - name: trigger
    value:
      pause_status: UNPAUSED
      file_arrival:
        url: string
        min_time_between_triggers_seconds: 0
        wait_after_last_change_seconds: 0
      periodic:
        interval: 0
        unit: HOURS
  - name: continuous
    value:
      pause_status: UNPAUSED
  - name: max_concurrent_runs
    value: 10
  - name: tasks
    value:
    - max_retries: 3
      task_key: Sessionize
      description: Extracts session data from events
      min_retry_interval_millis: 2000
      depends_on: []
      timeout_seconds: 86400
      spark_jar_task:
        main_class_name: com.databricks.Sessionize
        parameters:
        - --data
        - dbfs:/path/to/data.json
      libraries:
      - jar: dbfs:/mnt/databricks/Sessionize.jar
      retry_on_timeout: false
      existing_cluster_id: 0923-164208-meows279
    - max_retries: 3
      task_key: Orders_Ingest
      description: Ingests order data
      job_cluster_key: auto_scaling_cluster
      min_retry_interval_millis: 2000
      depends_on: []
      timeout_seconds: 86400
      spark_jar_task:
        main_class_name: com.databricks.OrdersIngest
        parameters:
        - --data
        - dbfs:/path/to/order-data.json
      libraries:
      - jar: dbfs:/mnt/databricks/OrderIngest.jar
      retry_on_timeout: false
    - max_retries: 3
      task_key: Match
      description: Matches orders with user sessions
      notebook_task:
        base_parameters:
          age: '35'
          name: John Doe
        notebook_path: /Users/user.name@databricks.com/Match
      min_retry_interval_millis: 2000
      depends_on:
      - task_key: Orders_Ingest
      - task_key: Sessionize
      new_cluster:
        autoscale:
          max_workers: 16
          min_workers: 2
        node_type_id: null
        spark_conf:
          spark.speculation: true
        spark_version: 7.3.x-scala2.12
      timeout_seconds: 86400
      retry_on_timeout: false
      run_if: ALL_SUCCESS
  - name: job_clusters
    value:
    - job_cluster_key: auto_scaling_cluster
      new_cluster:
        autoscale:
          max_workers: 16
          min_workers: 2
        node_type_id: null
        spark_conf:
          spark.speculation: true
        spark_version: 7.3.x-scala2.12
  - name: git_source
    value:
      git_branch: main
      git_provider: gitHub
      git_url: https://github.com/databricks/databricks-cli
  - name: tags
    value:
      cost-center: engineering
      team: jobs
  - name: format
    value: SINGLE_TASK
  - name: queue
    value:
      enabled: true
  - name: parameters
    value:
    - default: users
      name: table
  - name: run_as
    value:
      user_name: user@databricks.com
      service_principal_name: 692bc6d0-ffa3-11ed-be56-0242ac120002
  - name: edit_mode
    value: UI_LOCKED
  - name: deployment
    value:
      kind: BUNDLE
      metadata_file_path: string
  - name: environments
    value:
    - environment_key: string
      spec:
        client: '1'
        dependencies:
        - string
  - name: access_control_list
    value:
    - user_name: string
      group_name: string
      service_principal_name: string
      permission_level: CAN_MANAGE

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.workflows.jobs
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>jobs</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.workflows.jobs
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workflows.jobs
WHERE deployment_name = '{{ deployment_name }}';
```
