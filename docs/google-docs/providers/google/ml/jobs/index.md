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
      value: string
    - name: trainingInput
      value:
        - name: scaleTier
          value: string
        - name: masterType
          value: string
        - name: masterConfig
          value:
            - name: acceleratorConfig
              value:
                - name: count
                  value: string
                - name: type
                  value: string
            - name: imageUri
              value: string
            - name: tpuTfVersion
              value: string
            - name: diskConfig
              value:
                - name: bootDiskType
                  value: string
                - name: bootDiskSizeGb
                  value: integer
            - name: containerCommand
              value:
                - string
            - name: containerArgs
              value:
                - string
        - name: workerType
          value: string
        - name: parameterServerType
          value: string
        - name: evaluatorType
          value: string
        - name: workerCount
          value: string
        - name: parameterServerCount
          value: string
        - name: evaluatorCount
          value: string
        - name: packageUris
          value:
            - string
        - name: pythonModule
          value: string
        - name: args
          value:
            - string
        - name: hyperparameters
          value:
            - name: goal
              value: string
            - name: params
              value:
                - - name: parameterName
                    value: string
                  - name: type
                    value: string
                  - name: minValue
                    value: number
                  - name: maxValue
                    value: number
                  - name: categoricalValues
                    value:
                      - string
                  - name: discreteValues
                    value:
                      - number
                  - name: scaleType
                    value: string
            - name: maxTrials
              value: integer
            - name: maxParallelTrials
              value: integer
            - name: maxFailedTrials
              value: integer
            - name: hyperparameterMetricTag
              value: string
            - name: resumePreviousJobId
              value: string
            - name: enableTrialEarlyStopping
              value: boolean
            - name: algorithm
              value: string
        - name: region
          value: string
        - name: jobDir
          value: string
        - name: runtimeVersion
          value: string
        - name: pythonVersion
          value: string
        - name: encryptionConfig
          value:
            - name: kmsKeyName
              value: string
        - name: scheduling
          value:
            - name: maxRunningTime
              value: string
            - name: maxWaitTime
              value: string
            - name: priority
              value: integer
        - name: network
          value: string
        - name: serviceAccount
          value: string
        - name: useChiefInTfConfig
          value: boolean
        - name: enableWebAccess
          value: boolean
    - name: predictionInput
      value:
        - name: modelName
          value: string
        - name: versionName
          value: string
        - name: uri
          value: string
        - name: dataFormat
          value: string
        - name: outputDataFormat
          value: string
        - name: inputPaths
          value:
            - string
        - name: outputPath
          value: string
        - name: maxWorkerCount
          value: string
        - name: region
          value: string
        - name: runtimeVersion
          value: string
        - name: batchSize
          value: string
        - name: signatureName
          value: string
    - name: createTime
      value: string
    - name: startTime
      value: string
    - name: endTime
      value: string
    - name: state
      value: string
    - name: errorMessage
      value: string
    - name: trainingOutput
      value:
        - name: completedTrialCount
          value: string
        - name: trials
          value:
            - - name: trialId
                value: string
              - name: hyperparameters
                value: object
              - name: startTime
                value: string
              - name: endTime
                value: string
              - name: state
                value: string
              - name: finalMetric
                value:
                  - name: trainingStep
                    value: string
                  - name: objectiveValue
                    value: number
              - name: isTrialStoppedEarly
                value: boolean
              - name: allMetrics
                value:
                  - - name: trainingStep
                      value: string
                    - name: objectiveValue
                      value: number
              - name: builtInAlgorithmOutput
                value:
                  - name: framework
                    value: string
                  - name: runtimeVersion
                    value: string
                  - name: pythonVersion
                    value: string
                  - name: modelPath
                    value: string
              - name: webAccessUris
                value: object
        - name: consumedMLUnits
          value: number
        - name: isHyperparameterTuningJob
          value: boolean
        - name: isBuiltInAlgorithmJob
          value: boolean
        - name: hyperparameterMetricTag
          value: string
        - name: webAccessUris
          value: object
    - name: predictionOutput
      value:
        - name: outputPath
          value: string
        - name: predictionCount
          value: string
        - name: errorCount
          value: string
        - name: nodeHours
          value: number
    - name: labels
      value: object
    - name: etag
      value: string
    - name: jobPosition
      value: string

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
