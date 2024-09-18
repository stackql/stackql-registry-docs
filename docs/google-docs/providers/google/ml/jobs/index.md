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
jobId: string
trainingInput:
  scaleTier: string
  masterType: string
  masterConfig:
    acceleratorConfig:
      count: string
      type: string
    imageUri: string
    tpuTfVersion: string
    diskConfig:
      bootDiskType: string
      bootDiskSizeGb: integer
    containerCommand:
      - type: string
    containerArgs:
      - type: string
  workerType: string
  parameterServerType: string
  evaluatorType: string
  workerCount: string
  parameterServerCount: string
  evaluatorCount: string
  packageUris:
    - type: string
  pythonModule: string
  args:
    - type: string
  hyperparameters:
    goal: string
    params:
      - parameterName: string
        type: string
        minValue: number
        maxValue: number
        categoricalValues:
          - type: string
        discreteValues:
          - type: string
            format: string
        scaleType: string
    maxTrials: integer
    maxParallelTrials: integer
    maxFailedTrials: integer
    hyperparameterMetricTag: string
    resumePreviousJobId: string
    enableTrialEarlyStopping: boolean
    algorithm: string
  region: string
  jobDir: string
  runtimeVersion: string
  pythonVersion: string
  encryptionConfig:
    kmsKeyName: string
  scheduling:
    maxRunningTime: string
    maxWaitTime: string
    priority: integer
  network: string
  serviceAccount: string
  useChiefInTfConfig: boolean
  enableWebAccess: boolean
predictionInput:
  modelName: string
  versionName: string
  uri: string
  dataFormat: string
  outputDataFormat: string
  inputPaths:
    - type: string
  outputPath: string
  maxWorkerCount: string
  region: string
  runtimeVersion: string
  batchSize: string
  signatureName: string
createTime: string
startTime: string
endTime: string
state: string
errorMessage: string
trainingOutput:
  completedTrialCount: string
  trials:
    - trialId: string
      hyperparameters: object
      startTime: string
      endTime: string
      state: string
      finalMetric:
        trainingStep: string
        objectiveValue: number
      isTrialStoppedEarly: boolean
      allMetrics:
        - trainingStep: string
          objectiveValue: number
      builtInAlgorithmOutput:
        framework: string
        runtimeVersion: string
        pythonVersion: string
        modelPath: string
      webAccessUris: object
  consumedMLUnits: number
  isHyperparameterTuningJob: boolean
  isBuiltInAlgorithmJob: boolean
  hyperparameterMetricTag: string
  webAccessUris: object
predictionOutput:
  outputPath: string
  predictionCount: string
  errorCount: string
  nodeHours: number
labels: object
etag: string
jobPosition: string

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
