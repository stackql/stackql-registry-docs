---
title: tuning_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - tuning_jobs
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

Creates, updates, deletes, gets or lists a <code>tuning_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tuning_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.tuning_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. Resource name of a TuningJob. Format: `projects/{project}/locations/{location}/tuningJobs/{tuning_job}` |
| <CopyableCode code="description" /> | `string` | Optional. The description of the TuningJob. |
| <CopyableCode code="baseModel" /> | `string` | The base model that is being tuned, e.g., "gemini-1.0-pro-002". |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the TuningJob was created. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the TuningJob entered any of the following JobStates: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`, `JOB_STATE_EXPIRED`. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="experiment" /> | `string` | Output only. The Experiment associated with this TuningJob. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize TuningJob and generated resources such as Model and Endpoint. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the TuningJob for the first time entered the `JOB_STATE_RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the job. |
| <CopyableCode code="supervisedTuningSpec" /> | `object` | Tuning Spec for Supervised Tuning. |
| <CopyableCode code="tunedModel" /> | `object` | The Model Registry Model and Online Prediction Endpoint assiociated with this TuningJob. |
| <CopyableCode code="tunedModelDisplayName" /> | `string` | Optional. The display name of the TunedModel. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="tuningDataStats" /> | `object` | The tuning data statistic values for TuningJob. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the TuningJob was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tuningJobsId" /> | Gets a TuningJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TuningJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a TuningJob. A created TuningJob right away will be attempted to be run. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, tuningJobsId" /> | Cancels a TuningJob. Starts asynchronous cancellation on the TuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use GenAiTuningService.GetTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the TuningJob is not deleted; instead it becomes a job with a TuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TuningJob.state is set to `CANCELLED`. |

## `SELECT` examples

Lists TuningJobs in a Location.

```sql
SELECT
name,
description,
baseModel,
createTime,
encryptionSpec,
endTime,
error,
experiment,
labels,
startTime,
state,
supervisedTuningSpec,
tunedModel,
tunedModelDisplayName,
tuningDataStats,
updateTime
FROM google.aiplatform.tuning_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tuning_jobs</code> resource.

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
INSERT INTO google.aiplatform.tuning_jobs (
locationsId,
projectsId,
supervisedTuningSpec,
tuningDataStats,
name,
state,
updateTime,
tunedModel,
encryptionSpec,
tunedModelDisplayName,
endTime,
experiment,
error,
description,
startTime,
createTime,
baseModel,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ supervisedTuningSpec }}',
'{{ tuningDataStats }}',
'{{ name }}',
'{{ state }}',
'{{ updateTime }}',
'{{ tunedModel }}',
'{{ encryptionSpec }}',
'{{ tunedModelDisplayName }}',
'{{ endTime }}',
'{{ experiment }}',
'{{ error }}',
'{{ description }}',
'{{ startTime }}',
'{{ createTime }}',
'{{ baseModel }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: supervisedTuningSpec
        value: '{{ supervisedTuningSpec }}'
      - name: tuningDataStats
        value: '{{ tuningDataStats }}'
      - name: name
        value: '{{ name }}'
      - name: state
        value: '{{ state }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: tunedModel
        value: '{{ tunedModel }}'
      - name: encryptionSpec
        value: '{{ encryptionSpec }}'
      - name: tunedModelDisplayName
        value: '{{ tunedModelDisplayName }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: experiment
        value: '{{ experiment }}'
      - name: error
        value: '{{ error }}'
      - name: description
        value: '{{ description }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: baseModel
        value: '{{ baseModel }}'
      - name: labels
        value: '{{ labels }}'

```
</TabItem>
</Tabs>
