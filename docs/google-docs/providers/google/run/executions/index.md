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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `createTime` | `string` | Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `parallelism` | `integer` | Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be &lt;= task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ |
| `observedGeneration` | `string` | Output only. The generation of this Execution. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `runningCount` | `integer` | Output only. The number of actively running tasks. |
| `launchStage` | `string` | Set the launch stage to a preview stage on write to allow use of preview features in that stage. On read, describes whether the resource uses preview features. Launch Stages are defined at [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved. |
| `startTime` | `string` | Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `taskCount` | `integer` | Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ |
| `failedCount` | `integer` | Output only. The number of tasks which reached phase Failed. |
| `succeededCount` | `integer` | Output only. The number of tasks which reached phase Succeeded. |
| `completionTime` | `string` | Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations. |
| `annotations` | `object` | KRM-style annotations for the resource. |
| `template` | `object` | TaskTemplate describes the data a task should have when created from a template. |
| `conditions` | `array` | Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| `job` | `string` | Output only. The name of the parent Job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_executions_get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Gets information about a Execution. |
| `projects_locations_jobs_executions_list` | `SELECT` | `jobsId, locationsId, projectsId` | List Executions from a Job. |
| `projects_locations_jobs_executions_delete` | `DELETE` | `executionsId, jobsId, locationsId, projectsId` | Delete an Execution. |
