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
| `updateTime` | `string` | Output only. The last-modified time. |
| `retriedCount` | `integer` | Output only. The number of tasks which have retried at least once. |
| `labels` | `object` | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |
| `cancelledCount` | `integer` | Output only. The number of tasks which reached phase Cancelled. |
| `conditions` | `array` | Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `failedCount` | `integer` | Output only. The number of tasks which reached phase Failed. |
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `runningCount` | `integer` | Output only. The number of actively running tasks. |
| `succeededCount` | `integer` | Output only. The number of tasks which reached phase Succeeded. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `job` | `string` | Output only. The name of the parent Job. |
| `logUri` | `string` | Output only. URI where logs for this execution can be found in Cloud Console. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `template` | `object` | TaskTemplate describes the data a task should have when created from a template. |
| `startTime` | `string` | Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| `observedGeneration` | `string` | Output only. The generation of this Execution. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `parallelism` | `integer` | Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be &lt;= task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `createTime` | `string` | Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations. |
| `taskCount` | `integer` | Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution. |
| `annotations` | `object` | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| `launchStage` | `string` | The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA. |
| `completionTime` | `string` | Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Gets information about an Execution. |
| `list` | `SELECT` | `jobsId, locationsId, projectsId` | Lists Executions from a Job. |
| `delete` | `DELETE` | `executionsId, jobsId, locationsId, projectsId` | Deletes an Execution. |
| `_list` | `EXEC` | `jobsId, locationsId, projectsId` | Lists Executions from a Job. |
