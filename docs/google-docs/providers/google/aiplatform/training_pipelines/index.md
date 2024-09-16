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
trainingTaskDefinition,
inputDataConfig,
parentModel,
modelToUpload,
labels,
modelId,
encryptionSpec,
trainingTaskInputs,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ trainingTaskDefinition }}',
'{{ inputDataConfig }}',
'{{ parentModel }}',
'{{ modelToUpload }}',
'{{ labels }}',
'{{ modelId }}',
'{{ encryptionSpec }}',
'{{ trainingTaskInputs }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: trainingTaskDefinition
      value: '{{ trainingTaskDefinition }}'
    - name: inputDataConfig
      value:
        - name: stratifiedSplit
          value:
            - name: key
              value: '{{ key }}'
            - name: trainingFraction
              value: '{{ trainingFraction }}'
            - name: testFraction
              value: '{{ testFraction }}'
            - name: validationFraction
              value: '{{ validationFraction }}'
        - name: timestampSplit
          value:
            - name: validationFraction
              value: '{{ validationFraction }}'
            - name: key
              value: '{{ key }}'
            - name: trainingFraction
              value: '{{ trainingFraction }}'
            - name: testFraction
              value: '{{ testFraction }}'
        - name: predefinedSplit
          value:
            - name: key
              value: '{{ key }}'
        - name: gcsDestination
          value:
            - name: outputUriPrefix
              value: '{{ outputUriPrefix }}'
        - name: datasetId
          value: '{{ datasetId }}'
        - name: filterSplit
          value:
            - name: validationFilter
              value: '{{ validationFilter }}'
            - name: testFilter
              value: '{{ testFilter }}'
            - name: trainingFilter
              value: '{{ trainingFilter }}'
        - name: annotationsFilter
          value: '{{ annotationsFilter }}'
        - name: fractionSplit
          value:
            - name: trainingFraction
              value: '{{ trainingFraction }}'
            - name: validationFraction
              value: '{{ validationFraction }}'
            - name: testFraction
              value: '{{ testFraction }}'
        - name: bigqueryDestination
          value:
            - name: outputUri
              value: '{{ outputUri }}'
        - name: savedQueryId
          value: '{{ savedQueryId }}'
        - name: persistMlUseAssignment
          value: '{{ persistMlUseAssignment }}'
        - name: annotationSchemaUri
          value: '{{ annotationSchemaUri }}'
    - name: parentModel
      value: '{{ parentModel }}'
    - name: modelToUpload
      value:
        - name: dataStats
          value:
            - name: testAnnotationsCount
              value: '{{ testAnnotationsCount }}'
            - name: trainingAnnotationsCount
              value: '{{ trainingAnnotationsCount }}'
            - name: trainingDataItemsCount
              value: '{{ trainingDataItemsCount }}'
            - name: testDataItemsCount
              value: '{{ testDataItemsCount }}'
            - name: validationDataItemsCount
              value: '{{ validationDataItemsCount }}'
            - name: validationAnnotationsCount
              value: '{{ validationAnnotationsCount }}'
        - name: containerSpec
          value:
            - name: startupProbe
              value:
                - name: timeoutSeconds
                  value: '{{ timeoutSeconds }}'
                - name: periodSeconds
                  value: '{{ periodSeconds }}'
                - name: exec
                  value:
                    - name: command
                      value:
                        - name: type
                          value: '{{ type }}'
            - name: imageUri
              value: '{{ imageUri }}'
            - name: grpcPorts
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: command
              value:
                - name: type
                  value: '{{ type }}'
            - name: sharedMemorySizeMb
              value: '{{ sharedMemorySizeMb }}'
            - name: deploymentTimeout
              value: '{{ deploymentTimeout }}'
            - name: healthRoute
              value: '{{ healthRoute }}'
            - name: predictRoute
              value: '{{ predictRoute }}'
            - name: args
              value:
                - name: type
                  value: '{{ type }}'
            - name: env
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: ports
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: versionAliases
          value:
            - name: type
              value: '{{ type }}'
        - name: baseModelSource
          value:
            - name: modelGardenSource
              value:
                - name: publicModelName
                  value: '{{ publicModelName }}'
            - name: genieSource
              value:
                - name: baseModelUri
                  value: '{{ baseModelUri }}'
        - name: etag
          value: '{{ etag }}'
        - name: predictSchemata
          value:
            - name: predictionSchemaUri
              value: '{{ predictionSchemaUri }}'
            - name: instanceSchemaUri
              value: '{{ instanceSchemaUri }}'
            - name: parametersSchemaUri
              value: '{{ parametersSchemaUri }}'
        - name: metadata
          value: '{{ metadata }}'
        - name: metadataSchemaUri
          value: '{{ metadataSchemaUri }}'
        - name: artifactUri
          value: '{{ artifactUri }}'
        - name: explanationSpec
          value:
            - name: metadata
              value:
                - name: outputs
                  value: '{{ outputs }}'
                - name: featureAttributionsSchemaUri
                  value: '{{ featureAttributionsSchemaUri }}'
                - name: inputs
                  value: '{{ inputs }}'
                - name: latentSpaceSource
                  value: '{{ latentSpaceSource }}'
            - name: parameters
              value:
                - name: topK
                  value: '{{ topK }}'
                - name: examples
                  value:
                    - name: nearestNeighborSearchConfig
                      value: '{{ nearestNeighborSearchConfig }}'
                    - name: neighborCount
                      value: '{{ neighborCount }}'
                    - name: exampleGcsSource
                      value:
                        - name: dataFormat
                          value: '{{ dataFormat }}'
                        - name: gcsSource
                          value:
                            - name: uris
                              value:
                                - name: type
                                  value: '{{ type }}'
                    - name: presets
                      value:
                        - name: modality
                          value: '{{ modality }}'
                        - name: query
                          value: '{{ query }}'
                - name: sampledShapleyAttribution
                  value:
                    - name: pathCount
                      value: '{{ pathCount }}'
                - name: xraiAttribution
                  value:
                    - name: smoothGradConfig
                      value:
                        - name: featureNoiseSigma
                          value:
                            - name: noiseSigma
                              value:
                                - name: $ref
                                  value: '{{ $ref }}'
                        - name: noisySampleCount
                          value: '{{ noisySampleCount }}'
                        - name: noiseSigma
                          value: '{{ noiseSigma }}'
                    - name: stepCount
                      value: '{{ stepCount }}'
                    - name: blurBaselineConfig
                      value:
                        - name: maxBlurSigma
                          value: '{{ maxBlurSigma }}'
                - name: outputIndices
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: integratedGradientsAttribution
                  value:
                    - name: stepCount
                      value: '{{ stepCount }}'
        - name: description
          value: '{{ description }}'
        - name: labels
          value: '{{ labels }}'
        - name: versionDescription
          value: '{{ versionDescription }}'
        - name: pipelineJob
          value: '{{ pipelineJob }}'
        - name: displayName
          value: '{{ displayName }}'
        - name: encryptionSpec
          value:
            - name: kmsKeyName
              value: '{{ kmsKeyName }}'
        - name: name
          value: '{{ name }}'
    - name: labels
      value: '{{ labels }}'
    - name: modelId
      value: '{{ modelId }}'
    - name: trainingTaskInputs
      value: '{{ trainingTaskInputs }}'
    - name: displayName
      value: '{{ displayName }}'

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
