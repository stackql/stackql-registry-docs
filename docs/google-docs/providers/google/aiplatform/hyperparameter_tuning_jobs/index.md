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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>hyperparameter_tuning_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hyperparameter_tuning_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.hyperparameter_tuning_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the HyperparameterTuningJob. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the HyperparameterTuningJob was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="maxFailedTrialCount" /> | `integer` | The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails. |
| <CopyableCode code="maxTrialCount" /> | `integer` | Required. The desired total number of Trials. |
| <CopyableCode code="parallelTrialCount" /> | `integer` | Required. The desired number of Trials to run in parallel. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the job. |
| <CopyableCode code="studySpec" /> | `object` | Represents specification of a Study. |
| <CopyableCode code="trialJobSpec" /> | `object` | Represents the spec of a CustomJob. |
| <CopyableCode code="trials" /> | `array` | Output only. Trials of the HyperparameterTuningJob. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the HyperparameterTuningJob was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hyperparameterTuningJobsId, locationsId, projectsId" /> | Gets a HyperparameterTuningJob |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists HyperparameterTuningJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a HyperparameterTuningJob |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hyperparameterTuningJobsId, locationsId, projectsId" /> | Deletes a HyperparameterTuningJob. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="hyperparameterTuningJobsId, locationsId, projectsId" /> | Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`. |

## `SELECT` examples

Lists HyperparameterTuningJobs in a Location.

```sql
SELECT
name,
createTime,
displayName,
encryptionSpec,
endTime,
error,
labels,
maxFailedTrialCount,
maxTrialCount,
parallelTrialCount,
satisfiesPzi,
satisfiesPzs,
startTime,
state,
studySpec,
trialJobSpec,
trials,
updateTime
FROM google.aiplatform.hyperparameter_tuning_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hyperparameter_tuning_jobs</code> resource.

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
INSERT INTO google.aiplatform.hyperparameter_tuning_jobs (
locationsId,
projectsId,
trialJobSpec,
studySpec,
maxTrialCount,
labels,
maxFailedTrialCount,
displayName,
encryptionSpec,
parallelTrialCount
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ trialJobSpec }}',
'{{ studySpec }}',
'{{ maxTrialCount }}',
'{{ labels }}',
'{{ maxFailedTrialCount }}',
'{{ displayName }}',
'{{ encryptionSpec }}',
'{{ parallelTrialCount }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: trialJobSpec
      value:
        - name: workerPoolSpecs
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: tensorboard
          value: '{{ tensorboard }}'
        - name: experimentRun
          value: '{{ experimentRun }}'
        - name: reservedIpRanges
          value:
            - name: type
              value: '{{ type }}'
        - name: scheduling
          value:
            - name: timeout
              value: '{{ timeout }}'
            - name: disableRetries
              value: '{{ disableRetries }}'
            - name: strategy
              value: '{{ strategy }}'
            - name: restartJobOnWorkerRestart
              value: '{{ restartJobOnWorkerRestart }}'
            - name: maxWaitDuration
              value: '{{ maxWaitDuration }}'
        - name: protectedArtifactLocationId
          value: '{{ protectedArtifactLocationId }}'
        - name: serviceAccount
          value: '{{ serviceAccount }}'
        - name: baseOutputDirectory
          value:
            - name: outputUriPrefix
              value: '{{ outputUriPrefix }}'
        - name: enableWebAccess
          value: '{{ enableWebAccess }}'
        - name: experiment
          value: '{{ experiment }}'
        - name: models
          value:
            - name: type
              value: '{{ type }}'
        - name: persistentResourceId
          value: '{{ persistentResourceId }}'
        - name: network
          value: '{{ network }}'
        - name: enableDashboardAccess
          value: '{{ enableDashboardAccess }}'
    - name: studySpec
      value:
        - name: metrics
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: observationNoise
          value: '{{ observationNoise }}'
        - name: parameters
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: decayCurveStoppingSpec
          value:
            - name: useElapsedDuration
              value: '{{ useElapsedDuration }}'
        - name: convexAutomatedStoppingSpec
          value:
            - name: useElapsedDuration
              value: '{{ useElapsedDuration }}'
            - name: minStepCount
              value: '{{ minStepCount }}'
            - name: maxStepCount
              value: '{{ maxStepCount }}'
            - name: learningRateParameterName
              value: '{{ learningRateParameterName }}'
            - name: updateAllStoppedTrials
              value: '{{ updateAllStoppedTrials }}'
            - name: minMeasurementCount
              value: '{{ minMeasurementCount }}'
        - name: algorithm
          value: '{{ algorithm }}'
        - name: medianAutomatedStoppingSpec
          value:
            - name: useElapsedDuration
              value: '{{ useElapsedDuration }}'
        - name: measurementSelectionType
          value: '{{ measurementSelectionType }}'
        - name: studyStoppingConfig
          value:
            - name: minNumTrials
              value: '{{ minNumTrials }}'
            - name: shouldStopAsap
              value: '{{ shouldStopAsap }}'
            - name: maxNumTrialsNoProgress
              value: '{{ maxNumTrialsNoProgress }}'
            - name: maximumRuntimeConstraint
              value:
                - name: maxDuration
                  value: '{{ maxDuration }}'
                - name: endTime
                  value: '{{ endTime }}'
            - name: maxDurationNoProgress
              value: '{{ maxDurationNoProgress }}'
            - name: maxNumTrials
              value: '{{ maxNumTrials }}'
    - name: maxTrialCount
      value: '{{ maxTrialCount }}'
    - name: labels
      value: '{{ labels }}'
    - name: maxFailedTrialCount
      value: '{{ maxFailedTrialCount }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: '{{ kmsKeyName }}'
    - name: parallelTrialCount
      value: '{{ parallelTrialCount }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hyperparameter_tuning_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.hyperparameter_tuning_jobs
WHERE hyperparameterTuningJobsId = '{{ hyperparameterTuningJobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
