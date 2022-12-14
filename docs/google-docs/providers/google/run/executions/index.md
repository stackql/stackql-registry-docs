---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
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
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique name of this Execution. |
| `createTime` | `string` | Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `completionTime` | `string` | Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations. |
| `retriedCount` | `integer` | Output only. The number of tasks which have retried at least once. |
| `parallelism` | `integer` | Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be &lt;= task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ |
| `template` | `object` | TaskTemplate describes the data a task should have when created from a template. |
| `conditions` | `array` | Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| `failedCount` | `integer` | Output only. The number of tasks which reached phase Failed. |
| `runningCount` | `integer` | Output only. The number of actively running tasks. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `annotations` | `object` | KRM-style annotations for the resource. |
| `logUri` | `string` | Output only. URI where logs for this execution can be found in Cloud Console. |
| `observedGeneration` | `string` | Output only. The generation of this Execution. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `cancelledCount` | `integer` | Output only. The number of tasks which reached phase Cancelled. |
| `succeededCount` | `integer` | Output only. The number of tasks which reached phase Succeeded. |
| `job` | `string` | Output only. The name of the parent Job. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `taskCount` | `integer` | Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ |
| `uid` | `string` | Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `startTime` | `string` | Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| `launchStage` | `string` | Set the launch stage to a preview stage on write to allow use of preview features in that stage. On read, describes whether the resource uses preview features. Launch Stages are defined at [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_executions_get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Gets information about an Execution. |
| `projects_locations_jobs_executions_list` | `SELECT` | `jobsId, locationsId, projectsId` | Lists Executions from a Job. |
| `projects_locations_jobs_executions_delete` | `DELETE` | `executionsId, jobsId, locationsId, projectsId` | Deletes an Execution. |
