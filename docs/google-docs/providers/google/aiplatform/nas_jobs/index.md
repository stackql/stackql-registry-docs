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

Creates, updates, deletes or gets an <code>nas_job</code> resource or lists <code>nas_jobs</code> in a region

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
createTime,
encryptionSpec,
startTime,
error,
satisfiesPzi,
nasJobSpec,
satisfiesPzs,
nasJobOutput,
displayName,
endTime,
updateTime,
enableRestrictedImageTraining,
labels,
name,
state
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ createTime }}',
'{{ encryptionSpec }}',
'{{ startTime }}',
'{{ error }}',
true|false,
'{{ nasJobSpec }}',
true|false,
'{{ nasJobOutput }}',
'{{ displayName }}',
'{{ endTime }}',
'{{ updateTime }}',
true|false,
'{{ labels }}',
'{{ name }}',
'{{ state }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: createTime
        value: '{{ createTime }}'
      - name: encryptionSpec
        value: '{{ encryptionSpec }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: error
        value: '{{ error }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: nasJobSpec
        value: '{{ nasJobSpec }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: nasJobOutput
        value: '{{ nasJobOutput }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: enableRestrictedImageTraining
        value: '{{ enableRestrictedImageTraining }}'
      - name: labels
        value: '{{ labels }}'
      - name: name
        value: '{{ name }}'
      - name: state
        value: '{{ state }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified nas_job resource.

```sql
DELETE FROM google.aiplatform.nas_jobs
WHERE locationsId = '{{ locationsId }}'
AND nasJobsId = '{{ nasJobsId }}'
AND projectsId = '{{ projectsId }}';
```
