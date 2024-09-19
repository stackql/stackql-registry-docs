---
title: nas_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - nas_jobs
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

Creates, updates, deletes, gets or lists a <code>nas_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nas_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.nas_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the NasJob. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the NasJob was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the NasJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="enableRestrictedImageTraining" /> | `boolean` | Optional. Enable a separation of Custom model training and restricted image training for tenant project. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the NasJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize NasJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="nasJobOutput" /> | `object` | Represents a uCAIP NasJob output. |
| <CopyableCode code="nasJobSpec" /> | `object` | Represents the spec of a NasJob. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the NasJob for the first time entered the `JOB_STATE_RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the NasJob was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, nasJobsId, projectsId" /> | Gets a NasJob |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists NasJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a NasJob |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, nasJobsId, projectsId" /> | Deletes a NasJob. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="locationsId, nasJobsId, projectsId" /> | Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`. |

## `SELECT` examples

Lists NasJobs in a Location.

```sql
SELECT
name,
createTime,
displayName,
enableRestrictedImageTraining,
encryptionSpec,
endTime,
error,
labels,
nasJobOutput,
nasJobSpec,
satisfiesPzi,
satisfiesPzs,
startTime,
state,
updateTime
FROM google.aiplatform.nas_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nas_jobs</code> resource.

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
INSERT INTO google.aiplatform.nas_jobs (
locationsId,
projectsId,
enableRestrictedImageTraining,
labels,
nasJobSpec,
displayName,
encryptionSpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
{{ enableRestrictedImageTraining }},
'{{ labels }}',
'{{ nasJobSpec }}',
'{{ displayName }}',
'{{ encryptionSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: enableRestrictedImageTraining
      value: boolean
    - name: labels
      value: object
    - name: nasJobSpec
      value:
        - name: multiTrialAlgorithmSpec
          value:
            - name: multiTrialAlgorithm
              value: string
            - name: trainTrialSpec
              value:
                - name: trainTrialJobSpec
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
                - name: maxParallelTrialCount
                  value: integer
                - name: frequency
                  value: integer
            - name: searchTrialSpec
              value:
                - name: maxFailedTrialCount
                  value: integer
                - name: maxTrialCount
                  value: integer
                - name: maxParallelTrialCount
                  value: integer
            - name: metric
              value:
                - name: goal
                  value: string
                - name: metricId
                  value: string
        - name: resumeNasJobId
          value: string
        - name: searchSpaceSpec
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
    - name: displayName
      value: string
    - name: startTime
      value: string
    - name: state
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: updateTime
      value: string
    - name: endTime
      value: string
    - name: nasJobOutput
      value:
        - name: multiTrialJobOutput
          value:
            - name: trainTrials
              value:
                - - name: finalMeasurement
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
                  - name: id
                    value: string
                  - name: endTime
                    value: string
                  - name: startTime
                    value: string
                  - name: state
                    value: string
            - name: searchTrials
              value:
                - - name: id
                    value: string
                  - name: endTime
                    value: string
                  - name: startTime
                    value: string
                  - name: state
                    value: string
    - name: createTime
      value: string
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: string
    - name: satisfiesPzi
      value: boolean
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>nas_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.nas_jobs
WHERE locationsId = '{{ locationsId }}'
AND nasJobsId = '{{ nasJobsId }}'
AND projectsId = '{{ projectsId }}';
```
