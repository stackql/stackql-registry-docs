---
title: hyperparameter_tuning_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperparameter_tuning_jobs
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
<tr><td><b>Name</b></td><td><code>hyperparameter_tuning_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.hyperparameter_tuning_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the HyperparameterTuningJob. |
| `parallelTrialCount` | `integer` | Required. The desired number of Trials to run in parallel. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `studySpec` | `object` | Represents specification of a Study. |
| `maxTrialCount` | `integer` | Required. The desired total number of Trials. |
| `createTime` | `string` | Output only. Time when the HyperparameterTuningJob was created. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `state` | `string` | Output only. The detailed state of the job. |
| `updateTime` | `string` | Output only. Time when the HyperparameterTuningJob was most recently updated. |
| `trialJobSpec` | `object` | Represents the spec of a CustomJob. |
| `labels` | `object` | The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `startTime` | `string` | Output only. Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state. |
| `maxFailedTrialCount` | `integer` | The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails. |
| `endTime` | `string` | Output only. Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
| `trials` | `array` | Output only. Trials of the HyperparameterTuningJob. |
| `displayName` | `string` | Required. The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hyperparameterTuningJobsId, locationsId, projectsId` | Gets a HyperparameterTuningJob |
| `list` | `SELECT` | `locationsId, projectsId` | Lists HyperparameterTuningJobs in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a HyperparameterTuningJob |
| `delete` | `DELETE` | `hyperparameterTuningJobsId, locationsId, projectsId` | Deletes a HyperparameterTuningJob. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists HyperparameterTuningJobs in a Location. |
| `cancel` | `EXEC` | `hyperparameterTuningJobsId, locationsId, projectsId` | Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`. |
