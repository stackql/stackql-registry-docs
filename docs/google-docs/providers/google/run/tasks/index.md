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
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `job` | `string` | Output only. The name of the parent Job. |
| `maxRetries` | `integer` | Number of retries allowed per Task, before marking this Task failed. |
| `retried` | `integer` | Output only. The number of times this Task was retried. Tasks are retried when they fail up to the maxRetries limit. |
| `startTime` | `string` | Output only. Represents time when the task started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| `conditions` | `array` | Output only. The Condition of this Task, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `vpcAccess` | `object` | VPC Access settings. For more information on creating a VPC Connector, visit https://cloud.google.com/vpc/docs/configure-serverless-vpc-access For information on how to configure Cloud Run with an existing VPC Connector, visit https://cloud.google.com/run/docs/configuring/connecting-vpc |
| `updateTime` | `string` | Output only. The last-modified time. |
| `lastAttemptResult` | `object` | Result of a task attempt. |
| `containers` | `array` | Holds the single container that defines the unit of execution for this task. |
| `index` | `integer` | Output only. Index of the Task, unique per execution, and beginning at 0. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `volumes` | `array` | A list of Volumes to make available to containers. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `logUri` | `string` | Output only. URI where logs for this execution can be found in Cloud Console. |
| `createTime` | `string` | Output only. Represents time when the task was created by the system. It is not guaranteed to be set in happens-before order across separate operations. |
| `labels` | `object` | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |
| `completionTime` | `string` | Output only. Represents time when the Task was completed. It is not guaranteed to be set in happens-before order across separate operations. |
| `executionEnvironment` | `string` | The execution environment being used to host this Task. |
| `observedGeneration` | `string` | Output only. The generation of this Task. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| `annotations` | `object` | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Task. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `encryptionKey` | `string` | Output only. A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
| `serviceAccount` | `string` | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project's default service account. |
| `timeout` | `string` | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. |
| `execution` | `string` | Output only. The name of the parent Execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId, tasksId` | Gets information about a Task. |
| `list` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Lists Tasks from an Execution of a Job. |
| `_list` | `EXEC` | `executionsId, jobsId, locationsId, projectsId` | Lists Tasks from an Execution of a Job. |
