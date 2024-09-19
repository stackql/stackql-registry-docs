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
displayName,
studySpec,
maxFailedTrialCount,
trialJobSpec,
maxTrialCount,
encryptionSpec,
parallelTrialCount,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ studySpec }}',
'{{ maxFailedTrialCount }}',
'{{ trialJobSpec }}',
'{{ maxTrialCount }}',
'{{ encryptionSpec }}',
'{{ parallelTrialCount }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: createTime
      value: string
    - name: studySpec
      value:
        - name: parameters
          value:
            - - name: discreteValueSpec
                value:
                  - name: values
                    value:
                      - number
                  - name: defaultValue
                    value: number
              - name: categoricalValueSpec
                value:
                  - name: defaultValue
                    value: string
                  - name: values
                    value:
                      - string
              - name: conditionalParameterSpecs
                value:
                  - - name: parentCategoricalValues
                      value:
                        - name: values
                          value:
                            - string
                    - name: parentDiscreteValues
                      value:
                        - name: values
                          value:
                            - number
                    - name: parameterSpec
                      value:
                        - name: conditionalParameterSpecs
                          value:
                            - - name: parentIntValues
                                value:
                                  - name: values
                                    value:
                                      - string
                        - name: scaleType
                          value: string
                        - name: integerValueSpec
                          value:
                            - name: maxValue
                              value: string
                            - name: defaultValue
                              value: string
                            - name: minValue
                              value: string
                        - name: parameterId
                          value: string
                        - name: doubleValueSpec
                          value:
                            - name: defaultValue
                              value: number
                            - name: maxValue
                              value: number
                            - name: minValue
                              value: number
              - name: scaleType
                value: string
              - name: parameterId
                value: string
        - name: decayCurveStoppingSpec
          value:
            - name: useElapsedDuration
              value: boolean
        - name: observationNoise
          value: string
        - name: measurementSelectionType
          value: string
        - name: medianAutomatedStoppingSpec
          value:
            - name: useElapsedDuration
              value: boolean
        - name: convexAutomatedStoppingSpec
          value:
            - name: maxStepCount
              value: string
            - name: updateAllStoppedTrials
              value: boolean
            - name: minStepCount
              value: string
            - name: learningRateParameterName
              value: string
            - name: useElapsedDuration
              value: boolean
            - name: minMeasurementCount
              value: string
        - name: metrics
          value:
            - - name: goal
                value: string
              - name: metricId
                value: string
              - name: safetyConfig
                value:
                  - name: desiredMinSafeTrialsFraction
                    value: number
                  - name: safetyThreshold
                    value: number
        - name: studyStoppingConfig
          value:
            - name: maxNumTrials
              value: integer
            - name: maxNumTrialsNoProgress
              value: integer
            - name: shouldStopAsap
              value: boolean
            - name: maximumRuntimeConstraint
              value:
                - name: maxDuration
                  value: string
                - name: endTime
                  value: string
            - name: minNumTrials
              value: integer
            - name: maxDurationNoProgress
              value: string
        - name: algorithm
          value: string
    - name: maxFailedTrialCount
      value: integer
    - name: state
      value: string
    - name: trialJobSpec
      value:
        - name: scheduling
          value:
            - name: restartJobOnWorkerRestart
              value: boolean
            - name: timeout
              value: string
            - name: strategy
              value: string
            - name: disableRetries
              value: boolean
            - name: maxWaitDuration
              value: string
        - name: persistentResourceId
          value: string
        - name: baseOutputDirectory
          value:
            - name: outputUriPrefix
              value: string
        - name: experimentRun
          value: string
        - name: protectedArtifactLocationId
          value: string
        - name: serviceAccount
          value: string
        - name: workerPoolSpecs
          value:
            - - name: pythonPackageSpec
                value:
                  - name: args
                    value:
                      - string
                  - name: env
                    value:
                      - - name: value
                          value: string
                        - name: name
                          value: string
                  - name: pythonModule
                    value: string
                  - name: executorImageUri
                    value: string
                  - name: packageUris
                    value:
                      - string
              - name: diskSpec
                value:
                  - name: bootDiskType
                    value: string
                  - name: bootDiskSizeGb
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
              - name: containerSpec
                value:
                  - name: command
                    value:
                      - string
                  - name: args
                    value:
                      - string
                  - name: imageUri
                    value: string
                  - name: env
                    value:
                      - - name: value
                          value: string
                        - name: name
                          value: string
              - name: nfsMounts
                value:
                  - - name: mountPoint
                      value: string
                    - name: path
                      value: string
                    - name: server
                      value: string
              - name: replicaCount
                value: string
        - name: enableDashboardAccess
          value: boolean
        - name: network
          value: string
        - name: enableWebAccess
          value: boolean
        - name: experiment
          value: string
        - name: reservedIpRanges
          value:
            - string
        - name: tensorboard
          value: string
        - name: models
          value:
            - string
    - name: maxTrialCount
      value: integer
    - name: endTime
      value: string
    - name: name
      value: string
    - name: satisfiesPzi
      value: boolean
    - name: encryptionSpec
      value:
        - name: kmsKeyName
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
    - name: parallelTrialCount
      value: integer
    - name: startTime
      value: string
    - name: trials
      value:
        - - name: id
            value: string
          - name: clientId
            value: string
          - name: name
            value: string
          - name: customJob
            value: string
          - name: finalMeasurement
            value:
              - name: stepCount
                value: string
              - name: elapsedDuration
                value: string
              - name: metrics
                value:
                  - - name: value
                      value: number
                    - name: metricId
                      value: string
          - name: startTime
            value: string
          - name: measurements
            value:
              - - name: stepCount
                  value: string
                - name: elapsedDuration
                  value: string
                - name: metrics
                  value:
                    - - name: value
                        value: number
                      - name: metricId
                        value: string
          - name: state
            value: string
          - name: endTime
            value: string
          - name: webAccessUris
            value: object
          - name: parameters
            value:
              - - name: value
                  value: any
                - name: parameterId
                  value: string
          - name: infeasibleReason
            value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: satisfiesPzs
      value: boolean

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
