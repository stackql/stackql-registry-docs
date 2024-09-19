---
title: batch_prediction_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_prediction_jobs
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

Creates, updates, deletes, gets or lists a <code>batch_prediction_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_prediction_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.batch_prediction_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the BatchPredictionJob. |
| <CopyableCode code="completionStats" /> | `object` | Success and error statistics of processing multiple entities (for example, DataItems or structured data rows) in batch. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the BatchPredictionJob was created. |
| <CopyableCode code="dedicatedResources" /> | `object` | A description of resources that are used for performing batch operations, are dedicated to a Model, and need manual configuration. |
| <CopyableCode code="disableContainerLogging" /> | `boolean` | For custom-trained Models and AutoML Tabular Models, the container of the DeployedModel instances will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing). User can disable container logging by setting this flag to true. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of this BatchPredictionJob. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the BatchPredictionJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="explanationSpec" /> | `object` | Specification of Model explanation. |
| <CopyableCode code="generateExplanation" /> | `boolean` | Generate explanation with the batch prediction results. When set to `true`, the batch prediction output changes based on the `predictions_format` field of the BatchPredictionJob.output_config object: * `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the Explanation object. * `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the Explanation object. * `csv`: Generating explanations for CSV format is not supported. If this field is set to true, either the Model.explanation_spec or explanation_spec must be populated. |
| <CopyableCode code="inputConfig" /> | `object` | Configures the input to BatchPredictionJob. See Model.supported_input_storage_formats for Model's supported input formats, and how instances should be expressed via any of them. |
| <CopyableCode code="instanceConfig" /> | `object` | Configuration defining how to transform batch prediction input instances to the instances that the Model accepts. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize BatchPredictionJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="manualBatchTuningParameters" /> | `object` | Manual batch tuning parameters. |
| <CopyableCode code="model" /> | `string` | The name of the Model resource that produces the predictions via this job, must share the same ancestor Location. Starting this job has no impact on any existing deployments of the Model and their resources. Exactly one of model and unmanaged_container_model must be set. The model resource name may contain version id or version alias to specify the version. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` if no version is specified, the default version will be deployed. The model resource could also be a publisher model. Example: `publishers/{publisher}/models/{model}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}` |
| <CopyableCode code="modelParameters" /> | `any` | The parameters that govern the predictions. The schema of the parameters may be specified via the Model's PredictSchemata's parameters_schema_uri. |
| <CopyableCode code="modelVersionId" /> | `string` | Output only. The version ID of the Model that produces the predictions via this job. |
| <CopyableCode code="outputConfig" /> | `object` | Configures the output of BatchPredictionJob. See Model.supported_output_storage_formats for supported output formats, and how predictions are expressed via any of them. |
| <CopyableCode code="outputInfo" /> | `object` | Further describes this job's output. Supplements output_config. |
| <CopyableCode code="partialFailures" /> | `array` | Output only. Partial failures encountered. For example, single files that can't be read. This field never exceeds 20 entries. Status details fields contain standard Google Cloud error details. |
| <CopyableCode code="resourcesConsumed" /> | `object` | Statistics information about resource consumption. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account that the DeployedModel's container runs as. If not specified, a system generated one will be used, which has minimal permissions and the custom container, if used, may not have enough permission to access other Google Cloud resources. Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the BatchPredictionJob for the first time entered the `JOB_STATE_RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the job. |
| <CopyableCode code="unmanagedContainerModel" /> | `object` | Contains model information necessary to perform batch prediction without requiring a full model import. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the BatchPredictionJob was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="batchPredictionJobsId, locationsId, projectsId" /> | Gets a BatchPredictionJob |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists BatchPredictionJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="batchPredictionJobsId, locationsId, projectsId" /> | Deletes a BatchPredictionJob. Can only be called on jobs that already finished. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="batchPredictionJobsId, locationsId, projectsId" /> | Cancels a BatchPredictionJob. Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted. |

## `SELECT` examples

Lists BatchPredictionJobs in a Location.

```sql
SELECT
name,
completionStats,
createTime,
dedicatedResources,
disableContainerLogging,
displayName,
encryptionSpec,
endTime,
error,
explanationSpec,
generateExplanation,
inputConfig,
instanceConfig,
labels,
manualBatchTuningParameters,
model,
modelParameters,
modelVersionId,
outputConfig,
outputInfo,
partialFailures,
resourcesConsumed,
satisfiesPzi,
satisfiesPzs,
serviceAccount,
startTime,
state,
unmanagedContainerModel,
updateTime
FROM google.aiplatform.batch_prediction_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>batch_prediction_jobs</code> resource.

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
INSERT INTO google.aiplatform.batch_prediction_jobs (
locationsId,
projectsId,
labels,
generateExplanation,
dedicatedResources,
explanationSpec,
inputConfig,
instanceConfig,
outputConfig,
encryptionSpec,
disableContainerLogging,
displayName,
modelParameters,
serviceAccount,
manualBatchTuningParameters,
unmanagedContainerModel,
model
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
{{ generateExplanation }},
'{{ dedicatedResources }}',
'{{ explanationSpec }}',
'{{ inputConfig }}',
'{{ instanceConfig }}',
'{{ outputConfig }}',
'{{ encryptionSpec }}',
{{ disableContainerLogging }},
'{{ displayName }}',
'{{ modelParameters }}',
'{{ serviceAccount }}',
'{{ manualBatchTuningParameters }}',
'{{ unmanagedContainerModel }}',
'{{ model }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: labels
      value: object
    - name: generateExplanation
      value: boolean
    - name: updateTime
      value: string
    - name: state
      value: string
    - name: startTime
      value: string
    - name: dedicatedResources
      value:
        - name: startingReplicaCount
          value: integer
        - name: maxReplicaCount
          value: integer
        - name: machineSpec
          value:
            - name: acceleratorCount
              value: integer
            - name: tpuTopology
              value: string
            - name: machineType
              value: string
            - name: acceleratorType
              value: string
            - name: reservationAffinity
              value:
                - name: reservationAffinityType
                  value: string
                - name: values
                  value:
                    - string
                - name: key
                  value: string
    - name: satisfiesPzi
      value: boolean
    - name: resourcesConsumed
      value:
        - name: replicaHours
          value: number
    - name: createTime
      value: string
    - name: completionStats
      value:
        - name: successfulForecastPointCount
          value: string
        - name: failedCount
          value: string
        - name: successfulCount
          value: string
        - name: incompleteCount
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
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: inputConfig
      value:
        - name: instancesFormat
          value: string
        - name: bigquerySource
          value:
            - name: inputUri
              value: string
    - name: instanceConfig
      value:
        - name: excludedFields
          value:
            - string
        - name: instanceType
          value: string
        - name: includedFields
          value:
            - string
        - name: keyField
          value: string
    - name: outputConfig
      value:
        - name: bigqueryDestination
          value:
            - name: outputUri
              value: string
        - name: predictionsFormat
          value: string
        - name: gcsDestination
          value:
            - name: outputUriPrefix
              value: string
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: string
    - name: endTime
      value: string
    - name: disableContainerLogging
      value: boolean
    - name: displayName
      value: string
    - name: modelParameters
      value: any
    - name: serviceAccount
      value: string
    - name: partialFailures
      value:
        - - name: code
            value: integer
          - name: message
            value: string
          - name: details
            value:
              - object
    - name: manualBatchTuningParameters
      value:
        - name: batchSize
          value: integer
    - name: outputInfo
      value:
        - name: bigqueryOutputTable
          value: string
        - name: bigqueryOutputDataset
          value: string
        - name: gcsOutputDirectory
          value: string
    - name: name
      value: string
    - name: unmanagedContainerModel
      value:
        - name: artifactUri
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
        - name: predictSchemata
          value:
            - name: instanceSchemaUri
              value: string
            - name: predictionSchemaUri
              value: string
            - name: parametersSchemaUri
              value: string
    - name: model
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: modelVersionId
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>batch_prediction_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.batch_prediction_jobs
WHERE batchPredictionJobsId = '{{ batchPredictionJobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
