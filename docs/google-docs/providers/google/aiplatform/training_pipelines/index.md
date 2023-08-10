---
title: training_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - training_pipelines
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
<tr><td><b>Name</b></td><td><code>training_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.training_pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the TrainingPipeline. |
| `state` | `string` | Output only. The detailed state of the pipeline. |
| `displayName` | `string` | Required. The user-defined name of this TrainingPipeline. |
| `trainingTaskMetadata` | `any` | Output only. The metadata information as specified in the training_task_definition's `metadata`. This metadata is an auxiliary runtime and final information about the training task. While the pipeline is running this information is populated only at a best effort basis. Only present if the pipeline's training_task_definition contains `metadata` object. |
| `startTime` | `string` | Output only. Time when the TrainingPipeline for the first time entered the `PIPELINE_STATE_RUNNING` state. |
| `modelToUpload` | `object` | A trained machine learning Model. |
| `modelId` | `string` | Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen. |
| `createTime` | `string` | Output only. Time when the TrainingPipeline was created. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `trainingTaskInputs` | `any` | Required. The training task's parameter(s), as specified in the training_task_definition's `inputs`. |
| `updateTime` | `string` | Output only. Time when the TrainingPipeline was most recently updated. |
| `parentModel` | `string` | Optional. When specify this field, the `model_to_upload` will not be uploaded as a new model, instead, it will become a new version of this `parent_model`. |
| `trainingTaskDefinition` | `string` | Required. A Google Cloud Storage path to the YAML file that defines the training task which is responsible for producing the model artifact, and may also include additional auxiliary work. The definition files that can be used here are found in gs://google-cloud-aiplatform/schema/trainingjob/definition/. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |
| `labels` | `object` | The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `inputDataConfig` | `object` | Specifies Vertex AI owned input data to be used for training, and possibly evaluating, the Model. |
| `endTime` | `string` | Output only. Time when the TrainingPipeline entered any of the following states: `PIPELINE_STATE_SUCCEEDED`, `PIPELINE_STATE_FAILED`, `PIPELINE_STATE_CANCELLED`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, trainingPipelinesId` | Gets a TrainingPipeline. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists TrainingPipelines in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run. |
| `delete` | `DELETE` | `locationsId, projectsId, trainingPipelinesId` | Deletes a TrainingPipeline. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists TrainingPipelines in a Location. |
| `cancel` | `EXEC` | `locationsId, projectsId, trainingPipelinesId` | Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`. |
