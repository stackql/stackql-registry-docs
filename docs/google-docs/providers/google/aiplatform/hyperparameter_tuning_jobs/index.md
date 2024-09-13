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

Creates, updates, deletes or gets an <code>hyperparameter_tuning_job</code> resource or lists <code>hyperparameter_tuning_jobs</code> in a region

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
name,
trialJobSpec,
error,
studySpec,
updateTime,
createTime,
trials,
maxTrialCount,
labels,
satisfiesPzs,
state,
maxFailedTrialCount,
endTime,
satisfiesPzi,
displayName,
encryptionSpec,
startTime,
parallelTrialCount
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ trialJobSpec }}',
'{{ error }}',
'{{ studySpec }}',
'{{ updateTime }}',
'{{ createTime }}',
'{{ trials }}',
'{{ maxTrialCount }}',
'{{ labels }}',
true|false,
'{{ state }}',
'{{ maxFailedTrialCount }}',
'{{ endTime }}',
true|false,
'{{ displayName }}',
'{{ encryptionSpec }}',
'{{ startTime }}',
'{{ parallelTrialCount }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: trialJobSpec
        value: '{{ trialJobSpec }}'
      - name: error
        value: '{{ error }}'
      - name: studySpec
        value: '{{ studySpec }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: trials
        value: '{{ trials }}'
      - name: maxTrialCount
        value: '{{ maxTrialCount }}'
      - name: labels
        value: '{{ labels }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: state
        value: '{{ state }}'
      - name: maxFailedTrialCount
        value: '{{ maxFailedTrialCount }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: encryptionSpec
        value: '{{ encryptionSpec }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: parallelTrialCount
        value: '{{ parallelTrialCount }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified hyperparameter_tuning_job resource.

```sql
DELETE FROM google.aiplatform.hyperparameter_tuning_jobs
WHERE hyperparameterTuningJobsId = '{{ hyperparameterTuningJobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
