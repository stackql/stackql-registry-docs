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
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: state
      value: string
    - name: labels
      value: object
    - name: modelId
      value: string
    - name: updateTime
      value: string
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: createTime
      value: string
    - name: trainingTaskMetadata
      value: any
    - name: modelToUpload
      value:
        - name: pipelineJob
          value: string
        - name: explanationSpec
          value:
            - name: metadata
              value:
                - name: latentSpaceSource
                  value: string
                - name: featureAttributionsSchemaUri
                  value: string
                - name: outputs
                  value: object
                - name: inputs
                  value: object
            - name: parameters
              value:
                - name: integratedGradientsAttribution
                  value:
                    - name: blurBaselineConfig
                      value:
                        - name: maxBlurSigma
                          value: number
                    - name: smoothGradConfig
                      value:
                        - name: featureNoiseSigma
                          value:
                            - name: noiseSigma
                              value:
                                - - name: name
                                    value: string
                                  - name: sigma
                                    value: number
                        - name: noisySampleCount
                          value: integer
                        - name: noiseSigma
                          value: number
                    - name: stepCount
                      value: integer
                - name: topK
                  value: integer
                - name: outputIndices
                  value:
                    - any
                - name: sampledShapleyAttribution
                  value:
                    - name: pathCount
                      value: integer
                - name: xraiAttribution
                  value:
                    - name: stepCount
                      value: integer
                - name: examples
                  value:
                    - name: nearestNeighborSearchConfig
                      value: any
                    - name: neighborCount
                      value: integer
                    - name: exampleGcsSource
                      value:
                        - name: gcsSource
                          value:
                            - name: uris
                              value:
                                - string
                        - name: dataFormat
                          value: string
                    - name: presets
                      value:
                        - name: modality
                          value: string
                        - name: query
                          value: string
        - name: supportedOutputStorageFormats
          value:
            - string
        - name: name
          value: string
        - name: versionDescription
          value: string
        - name: encryptionSpec
          value:
            - name: kmsKeyName
              value: string
        - name: originalModelInfo
          value:
            - name: model
              value: string
        - name: satisfiesPzs
          value: boolean
        - name: supportedInputStorageFormats
          value:
            - string
        - name: artifactUri
          value: string
        - name: metadataArtifact
          value: string
        - name: predictSchemata
          value:
            - name: instanceSchemaUri
              value: string
            - name: predictionSchemaUri
              value: string
            - name: parametersSchemaUri
              value: string
        - name: createTime
          value: string
        - name: etag
          value: string
        - name: containerSpec
          value:
            - name: imageUri
              value: string
            - name: healthRoute
              value: string
            - name: env
              value:
                - - name: value
                    value: string
                  - name: name
                    value: string
            - name: ports
              value:
                - - name: containerPort
                    value: integer
            - name: args
              value:
                - string
            - name: command
              value:
                - string
            - name: deploymentTimeout
              value: string
            - name: startupProbe
              value:
                - name: exec
                  value:
                    - name: command
                      value:
                        - string
                - name: timeoutSeconds
                  value: integer
                - name: periodSeconds
                  value: integer
            - name: grpcPorts
              value:
                - - name: containerPort
                    value: integer
            - name: sharedMemorySizeMb
              value: string
            - name: predictRoute
              value: string
        - name: baseModelSource
          value:
            - name: genieSource
              value:
                - name: baseModelUri
                  value: string
            - name: modelGardenSource
              value:
                - name: publicModelName
                  value: string
        - name: labels
          value: object
        - name: versionUpdateTime
          value: string
        - name: satisfiesPzi
          value: boolean
        - name: deployedModels
          value:
            - - name: endpoint
                value: string
              - name: deployedModelId
                value: string
        - name: dataStats
          value:
            - name: validationDataItemsCount
              value: string
            - name: testDataItemsCount
              value: string
            - name: validationAnnotationsCount
              value: string
            - name: testAnnotationsCount
              value: string
            - name: trainingDataItemsCount
              value: string
            - name: trainingAnnotationsCount
              value: string
        - name: description
          value: string
        - name: versionAliases
          value:
            - string
        - name: metadataSchemaUri
          value: string
        - name: metadata
          value: any
        - name: supportedDeploymentResourcesTypes
          value:
            - string
        - name: displayName
          value: string
        - name: versionCreateTime
          value: string
        - name: versionId
          value: string
        - name: supportedExportFormats
          value:
            - - name: exportableContents
                value:
                  - string
              - name: id
                value: string
        - name: updateTime
          value: string
        - name: trainingPipeline
          value: string
        - name: modelSourceInfo
          value:
            - name: sourceType
              value: string
            - name: copy
              value: boolean
    - name: name
      value: string
    - name: inputDataConfig
      value:
        - name: stratifiedSplit
          value:
            - name: testFraction
              value: number
            - name: key
              value: string
            - name: validationFraction
              value: number
            - name: trainingFraction
              value: number
        - name: fractionSplit
          value:
            - name: trainingFraction
              value: number
            - name: validationFraction
              value: number
            - name: testFraction
              value: number
        - name: datasetId
          value: string
        - name: savedQueryId
          value: string
        - name: filterSplit
          value:
            - name: trainingFilter
              value: string
            - name: validationFilter
              value: string
            - name: testFilter
              value: string
        - name: annotationSchemaUri
          value: string
        - name: persistMlUseAssignment
          value: boolean
        - name: gcsDestination
          value:
            - name: outputUriPrefix
              value: string
        - name: bigqueryDestination
          value:
            - name: outputUri
              value: string
        - name: predefinedSplit
          value:
            - name: key
              value: string
        - name: timestampSplit
          value:
            - name: trainingFraction
              value: number
            - name: key
              value: string
            - name: validationFraction
              value: number
            - name: testFraction
              value: number
        - name: annotationsFilter
          value: string
    - name: startTime
      value: string
    - name: trainingTaskDefinition
      value: string
    - name: endTime
      value: string
    - name: parentModel
      value: string
    - name: trainingTaskInputs
      value: any

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
