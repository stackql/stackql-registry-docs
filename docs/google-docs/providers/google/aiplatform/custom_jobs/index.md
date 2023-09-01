---
title: custom_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_jobs
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>custom_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.custom_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of a CustomJob. |
| `displayName` | `string` | Required. The display name of the CustomJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `state` | `string` | Output only. The detailed state of the job. |
| `createTime` | `string` | Output only. Time when the CustomJob was created. |
| `webAccessUris` | `object` | Output only. URIs for accessing [interactive shells](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) (one URI for each training node). Only available if job_spec.enable_web_access is `true`. The keys are names of each node in the training job; for example, `workerpool0-0` for the primary node, `workerpool1-0` for the first node in the second worker pool, and `workerpool1-1` for the second node in the second worker pool. The values are the URIs for each node's interactive shell. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `labels` | `object` | The labels with user-defined metadata to organize CustomJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `updateTime` | `string` | Output only. Time when the CustomJob was most recently updated. |
| `jobSpec` | `object` | Represents the spec of a CustomJob. |
| `startTime` | `string` | Output only. Time when the CustomJob for the first time entered the `JOB_STATE_RUNNING` state. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `endTime` | `string` | Output only. Time when the CustomJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customJobsId, locationsId, projectsId` | Gets a CustomJob. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists CustomJobs in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a CustomJob. A created CustomJob right away will be attempted to be run. |
| `delete` | `DELETE` | `customJobsId, locationsId, projectsId` | Deletes a CustomJob. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists CustomJobs in a Location. |
| `cancel` | `EXEC` | `customJobsId, locationsId, projectsId` | Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`. |
