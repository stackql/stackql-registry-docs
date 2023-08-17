---
title: nas_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - nas_jobs
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
<tr><td><b>Name</b></td><td><code>nas_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.nas_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the NasJob. |
| `displayName` | `string` | Required. The display name of the NasJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `enableRestrictedImageTraining` | `boolean` | Optional. Enable a separation of Custom model training and restricted image training for tenant project. |
| `createTime` | `string` | Output only. Time when the NasJob was created. |
| `endTime` | `string` | Output only. Time when the NasJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
| `startTime` | `string` | Output only. Time when the NasJob for the first time entered the `JOB_STATE_RUNNING` state. |
| `updateTime` | `string` | Output only. Time when the NasJob was most recently updated. |
| `labels` | `object` | The labels with user-defined metadata to organize NasJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `nasJobSpec` | `object` | Represents the spec of a NasJob. |
| `state` | `string` | Output only. The detailed state of the job. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `nasJobOutput` | `object` | Represents a uCAIP NasJob output. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, nasJobsId, projectsId` | Gets a NasJob |
| `list` | `SELECT` | `locationsId, projectsId` | Lists NasJobs in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a NasJob |
| `delete` | `DELETE` | `locationsId, nasJobsId, projectsId` | Deletes a NasJob. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists NasJobs in a Location. |
| `cancel` | `EXEC` | `locationsId, nasJobsId, projectsId` | Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`. |
