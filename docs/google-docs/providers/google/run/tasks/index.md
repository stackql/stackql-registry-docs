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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `updateTime` | `string` | Output only. The last-modified time. |
| `observedGeneration` | `string` | Output only. The generation of this Task. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `createTime` | `string` | Output only. Represents time when the task was created by the job controller. It is not guaranteed to be set in happens-before order across separate operations. |
| `annotations` | `object` | KRM-style annotations for the resource. |
| `index` | `integer` | Output only. Index of the Task, unique per execution, and beginning at 0. |
| `volumes` | `array` | A list of Volumes to make available to containers. |
| `maxRetries` | `integer` | Number of retries allowed per Task, before marking this Task failed. |
| `job` | `string` | Output only. The name of the parent Job. |
| `execution` | `string` | Output only. The name of the parent Execution. |
| `lastAttemptResult` | `object` | Result of a task attempt. |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved. |
| `launchStage` | `string` | Set the launch stage to a preview stage on write to allow use of preview features in that stage. On read, describes whether the resource uses preview features. Launch Stages are defined at [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). |
| `vpcAccess` | `object` | VPC Access settings. For more information on creating a VPC Connector, visit https://cloud.google.com/vpc/docs/configure-serverless-vpc-access For information on how to configure Cloud Run with an existing VPC Connector, visit https://cloud.google.com/run/docs/configuring/connecting-vpc |
| `containers` | `array` | Holds the single container that defines the unit of execution for this task. |
| `timeout` | `string` | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. |
| `completionTime` | `string` | Output only. Represents time when the Task was completed. It is not guaranteed to be set in happens-before order across separate operations. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `serviceAccount` | `string` | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project's default service account. |
| `retried` | `integer` | Output only. The number of times this Task was retried. Tasks are retried when they fail up to the maxRetries limit. |
| `executionEnvironment` | `string` | The execution environment being used to host this Task. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `startTime` | `string` | Output only. Represents time when the task started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Task. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `conditions` | `array` | Output only. The Condition of this Task, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `encryptionKey` | `string` | Output only. A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_executions_tasks_get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId, tasksId` | Gets information about a Task. |
| `projects_locations_jobs_executions_tasks_list` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | List Tasks from an Execution of a Job. |
