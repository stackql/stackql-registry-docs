---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - run
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique name of this Task. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `job` | `string` | Output only. The name of the parent Job. |
| `lastAttemptResult` | `object` | Result of a task attempt. |
| `startTime` | `string` | Output only. Represents time when the task started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| `observedGeneration` | `string` | Output only. The generation of this Task. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Task. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `volumes` | `array` | A list of Volumes to make available to containers. |
| `timeout` | `string` | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. |
| `encryptionKey` | `string` | Output only. A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `maxRetries` | `integer` | Number of retries allowed per Task, before marking this Task failed. |
| `vpcAccess` | `object` | VPC Access settings. For more information on creating a VPC Connector, visit https://cloud.google.com/vpc/docs/configure-serverless-vpc-access For information on how to configure Cloud Run with an existing VPC Connector, visit https://cloud.google.com/run/docs/configuring/connecting-vpc |
| `serviceAccount` | `string` | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project's default service account. |
| `index` | `integer` | Output only. Index of the Task, unique per execution, and beginning at 0. |
| `retried` | `integer` | Output only. The number of times this Task was retried. Tasks are retried when they fail up to the maxRetries limit. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `logUri` | `string` | Output only. URI where logs for this execution can be found in Cloud Console. |
| `createTime` | `string` | Output only. Represents time when the task was created by the job controller. It is not guaranteed to be set in happens-before order across separate operations. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |
| `conditions` | `array` | Output only. The Condition of this Task, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| `annotations` | `object` | KRM-style annotations for the resource. |
| `executionEnvironment` | `string` | The execution environment being used to host this Task. |
| `containers` | `array` | Holds the single container that defines the unit of execution for this task. |
| `completionTime` | `string` | Output only. Represents time when the Task was completed. It is not guaranteed to be set in happens-before order across separate operations. |
| `execution` | `string` | Output only. The name of the parent Execution. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_executions_tasks_get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId, tasksId` | Gets information about a Task. |
| `projects_locations_jobs_executions_tasks_list` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Lists Tasks from an Execution of a Job. |
