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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>training_pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>training_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.training_pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the TrainingPipeline. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the TrainingPipeline was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of this TrainingPipeline. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the TrainingPipeline entered any of the following states: `PIPELINE_STATE_SUCCEEDED`, `PIPELINE_STATE_FAILED`, `PIPELINE_STATE_CANCELLED`. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="inputDataConfig" /> | `object` | Specifies Vertex AI owned input data to be used for training, and possibly evaluating, the Model. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="modelId" /> | `string` | Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen. |
| <CopyableCode code="modelToUpload" /> | `object` | A trained machine learning Model. |
| <CopyableCode code="parentModel" /> | `string` | Optional. When specify this field, the `model_to_upload` will not be uploaded as a new model, instead, it will become a new version of this `parent_model`. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the TrainingPipeline for the first time entered the `PIPELINE_STATE_RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the pipeline. |
| <CopyableCode code="trainingTaskDefinition" /> | `string` | Required. A Google Cloud Storage path to the YAML file that defines the training task which is responsible for producing the model artifact, and may also include additional auxiliary work. The definition files that can be used here are found in gs://google-cloud-aiplatform/schema/trainingjob/definition/. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |
| <CopyableCode code="trainingTaskInputs" /> | `any` | Required. The training task's parameter(s), as specified in the training_task_definition's `inputs`. |
| <CopyableCode code="trainingTaskMetadata" /> | `any` | Output only. The metadata information as specified in the training_task_definition's `metadata`. This metadata is an auxiliary runtime and final information about the training task. While the pipeline is running this information is populated only at a best effort basis. Only present if the pipeline's training_task_definition contains `metadata` object. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the TrainingPipeline was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, trainingPipelinesId" /> | Gets a TrainingPipeline. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TrainingPipelines in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, trainingPipelinesId" /> | Deletes a TrainingPipeline. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, trainingPipelinesId" /> | Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`. |

## `SELECT` examples

Lists TrainingPipelines in a Location.

```sql
SELECT
name,
createTime,
displayName,
encryptionSpec,
endTime,
error,
inputDataConfig,
labels,
modelId,
modelToUpload,
parentModel,
startTime,
state,
trainingTaskDefinition,
trainingTaskInputs,
trainingTaskMetadata,
updateTime
FROM google.aiplatform.training_pipelines
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>training_pipelines</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.aiplatform.training_pipelines (
locationsId,
projectsId,
displayName,
labels,
modelId,
modelToUpload,
encryptionSpec,
inputDataConfig,
trainingTaskDefinition,
parentModel,
trainingTaskInputs
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ labels }}',
'{{ modelId }}',
'{{ modelToUpload }}',
'{{ encryptionSpec }}',
'{{ inputDataConfig }}',
'{{ trainingTaskDefinition }}',
'{{ parentModel }}',
'{{ trainingTaskInputs }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
displayName: string
state: string
labels: object
modelId: string
updateTime: string
error:
  code: integer
  message: string
  details:
    - additionalProperties: any
      type: string
createTime: string
trainingTaskMetadata: any
modelToUpload:
  pipelineJob: string
  explanationSpec:
    metadata:
      latentSpaceSource: string
      featureAttributionsSchemaUri: string
      outputs: object
      inputs: object
    parameters:
      integratedGradientsAttribution:
        blurBaselineConfig:
          maxBlurSigma: number
        smoothGradConfig:
          featureNoiseSigma:
            noiseSigma:
              - name: string
                sigma: number
          noisySampleCount: integer
          noiseSigma: number
        stepCount: integer
      topK: integer
      outputIndices:
        - type: string
      sampledShapleyAttribution:
        pathCount: integer
      xraiAttribution:
        stepCount: integer
      examples:
        nearestNeighborSearchConfig: any
        neighborCount: integer
        exampleGcsSource:
          gcsSource:
            uris:
              - type: string
          dataFormat: string
        presets:
          modality: string
          query: string
  supportedOutputStorageFormats:
    - type: string
  name: string
  versionDescription: string
  encryptionSpec:
    kmsKeyName: string
  originalModelInfo:
    model: string
  satisfiesPzs: boolean
  supportedInputStorageFormats:
    - type: string
  artifactUri: string
  metadataArtifact: string
  predictSchemata:
    instanceSchemaUri: string
    predictionSchemaUri: string
    parametersSchemaUri: string
  createTime: string
  etag: string
  containerSpec:
    imageUri: string
    healthRoute: string
    env:
      - value: string
        name: string
    ports:
      - containerPort: integer
    args:
      - type: string
    command:
      - type: string
    deploymentTimeout: string
    startupProbe:
      exec:
        command:
          - type: string
      timeoutSeconds: integer
      periodSeconds: integer
    grpcPorts:
      - containerPort: integer
    sharedMemorySizeMb: string
    predictRoute: string
  baseModelSource:
    genieSource:
      baseModelUri: string
    modelGardenSource:
      publicModelName: string
  labels: object
  versionUpdateTime: string
  satisfiesPzi: boolean
  deployedModels:
    - endpoint: string
      deployedModelId: string
  dataStats:
    validationDataItemsCount: string
    testDataItemsCount: string
    validationAnnotationsCount: string
    testAnnotationsCount: string
    trainingDataItemsCount: string
    trainingAnnotationsCount: string
  description: string
  versionAliases:
    - type: string
  metadataSchemaUri: string
  metadata: any
  supportedDeploymentResourcesTypes:
    - enumDescriptions: string
      enum: string
      type: string
  displayName: string
  versionCreateTime: string
  versionId: string
  supportedExportFormats:
    - exportableContents:
        - enumDescriptions: string
          enum: string
          type: string
      id: string
  updateTime: string
  trainingPipeline: string
  modelSourceInfo:
    sourceType: string
    copy: boolean
name: string
inputDataConfig:
  stratifiedSplit:
    testFraction: number
    key: string
    validationFraction: number
    trainingFraction: number
  fractionSplit:
    trainingFraction: number
    validationFraction: number
    testFraction: number
  datasetId: string
  savedQueryId: string
  filterSplit:
    trainingFilter: string
    validationFilter: string
    testFilter: string
  annotationSchemaUri: string
  persistMlUseAssignment: boolean
  gcsDestination:
    outputUriPrefix: string
  bigqueryDestination:
    outputUri: string
  predefinedSplit:
    key: string
  timestampSplit:
    trainingFraction: number
    key: string
    validationFraction: number
    testFraction: number
  annotationsFilter: string
startTime: string
trainingTaskDefinition: string
endTime: string
parentModel: string
trainingTaskInputs: any

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>training_pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.training_pipelines
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND trainingPipelinesId = '{{ trainingPipelinesId }}';
```
