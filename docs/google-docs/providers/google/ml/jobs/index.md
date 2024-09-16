---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - ml
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createTime" /> | `string` | Output only. When the job was created. |
| <CopyableCode code="endTime" /> | `string` | Output only. When the job processing was completed. |
| <CopyableCode code="errorMessage" /> | `string` | Output only. The details of a failure or a cancellation. |
| <CopyableCode code="etag" /> | `string` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job. |
| <CopyableCode code="jobId" /> | `string` | Required. The user-specified id of the job. |
| <CopyableCode code="jobPosition" /> | `string` | Output only. It's only effect when the job is in QUEUED state. If it's positive, it indicates the job's position in the job scheduler. It's 0 when the job is already scheduled. |
| <CopyableCode code="labels" /> | `object` | Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. |
| <CopyableCode code="predictionInput" /> | `object` | Represents input parameters for a prediction job. |
| <CopyableCode code="predictionOutput" /> | `object` | Represents results of a prediction job. |
| <CopyableCode code="startTime" /> | `string` | Output only. When the job processing was started. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a job. |
| <CopyableCode code="trainingInput" /> | `object` | Represents input parameters for a training job. When using the gcloud command to submit your training job, you can specify the input parameters as command-line arguments and/or in a YAML configuration file referenced from the --config command-line argument. For details, see the guide to [submitting a training job](/ai-platform/training/docs/training-jobs). |
| <CopyableCode code="trainingOutput" /> | `object` | Represents results of a training job. Output only. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_get" /> | `SELECT` | <CopyableCode code="jobsId, projectsId" /> | Describes a job. |
| <CopyableCode code="projects_jobs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the jobs in the project. If there are no jobs that match the request parameters, the list request returns an empty response body: {}. |
| <CopyableCode code="projects_jobs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a training or a batch prediction job. |
| <CopyableCode code="projects_jobs_patch" /> | `UPDATE` | <CopyableCode code="jobsId, projectsId" /> | Updates a specific job resource. Currently the only supported fields to update are `labels`. |
| <CopyableCode code="projects_jobs_cancel" /> | `EXEC` | <CopyableCode code="jobsId, projectsId" /> | Cancels a running job. |

## `SELECT` examples

Lists the jobs in the project. If there are no jobs that match the request parameters, the list request returns an empty response body: {}.

```sql
SELECT
createTime,
endTime,
errorMessage,
etag,
jobId,
jobPosition,
labels,
predictionInput,
predictionOutput,
startTime,
state,
trainingInput,
trainingOutput
FROM google.ml.jobs
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO google.ml.jobs (
projectsId,
jobId,
trainingInput,
predictionInput,
startTime,
endTime,
state,
errorMessage,
trainingOutput,
predictionOutput,
labels,
etag
)
SELECT 
'{{ projectsId }}',
'{{ jobId }}',
'{{ trainingInput }}',
'{{ predictionInput }}',
'{{ startTime }}',
'{{ endTime }}',
'{{ state }}',
'{{ errorMessage }}',
'{{ trainingOutput }}',
'{{ predictionOutput }}',
'{{ labels }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: jobId
      value: '{{ jobId }}'
    - name: trainingInput
      value:
        - name: scaleTier
          value: '{{ scaleTier }}'
        - name: masterType
          value: '{{ masterType }}'
        - name: masterConfig
          value:
            - name: acceleratorConfig
              value:
                - name: count
                  value: '{{ count }}'
                - name: type
                  value: '{{ type }}'
            - name: imageUri
              value: '{{ imageUri }}'
            - name: tpuTfVersion
              value: '{{ tpuTfVersion }}'
            - name: diskConfig
              value:
                - name: bootDiskType
                  value: '{{ bootDiskType }}'
                - name: bootDiskSizeGb
                  value: '{{ bootDiskSizeGb }}'
            - name: containerCommand
              value:
                - name: type
                  value: '{{ type }}'
            - name: containerArgs
              value:
                - name: type
                  value: '{{ type }}'
        - name: workerType
          value: '{{ workerType }}'
        - name: parameterServerType
          value: '{{ parameterServerType }}'
        - name: evaluatorType
          value: '{{ evaluatorType }}'
        - name: workerCount
          value: '{{ workerCount }}'
        - name: parameterServerCount
          value: '{{ parameterServerCount }}'
        - name: evaluatorCount
          value: '{{ evaluatorCount }}'
        - name: packageUris
          value:
            - name: type
              value: '{{ type }}'
        - name: pythonModule
          value: '{{ pythonModule }}'
        - name: args
          value:
            - name: type
              value: '{{ type }}'
        - name: hyperparameters
          value:
            - name: goal
              value: '{{ goal }}'
            - name: params
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: maxTrials
              value: '{{ maxTrials }}'
            - name: maxParallelTrials
              value: '{{ maxParallelTrials }}'
            - name: maxFailedTrials
              value: '{{ maxFailedTrials }}'
            - name: hyperparameterMetricTag
              value: '{{ hyperparameterMetricTag }}'
            - name: resumePreviousJobId
              value: '{{ resumePreviousJobId }}'
            - name: enableTrialEarlyStopping
              value: '{{ enableTrialEarlyStopping }}'
            - name: algorithm
              value: '{{ algorithm }}'
        - name: region
          value: '{{ region }}'
        - name: jobDir
          value: '{{ jobDir }}'
        - name: runtimeVersion
          value: '{{ runtimeVersion }}'
        - name: pythonVersion
          value: '{{ pythonVersion }}'
        - name: encryptionConfig
          value:
            - name: kmsKeyName
              value: '{{ kmsKeyName }}'
        - name: scheduling
          value:
            - name: maxRunningTime
              value: '{{ maxRunningTime }}'
            - name: maxWaitTime
              value: '{{ maxWaitTime }}'
            - name: priority
              value: '{{ priority }}'
        - name: network
          value: '{{ network }}'
        - name: serviceAccount
          value: '{{ serviceAccount }}'
        - name: useChiefInTfConfig
          value: '{{ useChiefInTfConfig }}'
        - name: enableWebAccess
          value: '{{ enableWebAccess }}'
    - name: predictionInput
      value:
        - name: modelName
          value: '{{ modelName }}'
        - name: versionName
          value: '{{ versionName }}'
        - name: uri
          value: '{{ uri }}'
        - name: dataFormat
          value: '{{ dataFormat }}'
        - name: outputDataFormat
          value: '{{ outputDataFormat }}'
        - name: inputPaths
          value:
            - name: type
              value: '{{ type }}'
        - name: outputPath
          value: '{{ outputPath }}'
        - name: maxWorkerCount
          value: '{{ maxWorkerCount }}'
        - name: region
          value: '{{ region }}'
        - name: runtimeVersion
          value: '{{ runtimeVersion }}'
        - name: batchSize
          value: '{{ batchSize }}'
        - name: signatureName
          value: '{{ signatureName }}'
    - name: startTime
      value: '{{ startTime }}'
    - name: endTime
      value: '{{ endTime }}'
    - name: state
      value: '{{ state }}'
    - name: errorMessage
      value: '{{ errorMessage }}'
    - name: trainingOutput
      value:
        - name: completedTrialCount
          value: '{{ completedTrialCount }}'
        - name: trials
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: consumedMLUnits
          value: '{{ consumedMLUnits }}'
        - name: isHyperparameterTuningJob
          value: '{{ isHyperparameterTuningJob }}'
        - name: isBuiltInAlgorithmJob
          value: '{{ isBuiltInAlgorithmJob }}'
        - name: builtInAlgorithmOutput
          value:
            - name: framework
              value: '{{ framework }}'
            - name: runtimeVersion
              value: '{{ runtimeVersion }}'
            - name: pythonVersion
              value: '{{ pythonVersion }}'
            - name: modelPath
              value: '{{ modelPath }}'
        - name: hyperparameterMetricTag
          value: '{{ hyperparameterMetricTag }}'
    - name: predictionOutput
      value:
        - name: outputPath
          value: '{{ outputPath }}'
        - name: predictionCount
          value: '{{ predictionCount }}'
        - name: errorCount
          value: '{{ errorCount }}'
        - name: nodeHours
          value: '{{ nodeHours }}'
    - name: labels
      value: '{{ labels }}'
    - name: etag
      value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE google.ml.jobs
SET 
jobId = '{{ jobId }}',
trainingInput = '{{ trainingInput }}',
predictionInput = '{{ predictionInput }}',
startTime = '{{ startTime }}',
endTime = '{{ endTime }}',
state = '{{ state }}',
errorMessage = '{{ errorMessage }}',
trainingOutput = '{{ trainingOutput }}',
predictionOutput = '{{ predictionOutput }}',
labels = '{{ labels }}',
etag = '{{ etag }}'
WHERE 
jobsId = '{{ jobsId }}'
AND projectsId = '{{ projectsId }}';
```
