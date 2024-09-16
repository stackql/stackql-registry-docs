---
title: custom_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_jobs
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

Creates, updates, deletes, gets or lists a <code>custom_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.custom_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of a CustomJob. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the CustomJob was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the CustomJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the CustomJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="jobSpec" /> | `object` | Represents the spec of a CustomJob. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize CustomJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the CustomJob for the first time entered the `JOB_STATE_RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the CustomJob was most recently updated. |
| <CopyableCode code="webAccessUris" /> | `object` | Output only. URIs for accessing [interactive shells](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) (one URI for each training node). Only available if job_spec.enable_web_access is `true`. The keys are names of each node in the training job; for example, `workerpool0-0` for the primary node, `workerpool1-0` for the first node in the second worker pool, and `workerpool1-1` for the second node in the second worker pool. The values are the URIs for each node's interactive shell. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customJobsId, locationsId, projectsId" /> | Gets a CustomJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CustomJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a CustomJob. A created CustomJob right away will be attempted to be run. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customJobsId, locationsId, projectsId" /> | Deletes a CustomJob. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="customJobsId, locationsId, projectsId" /> | Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`. |

## `SELECT` examples

Lists CustomJobs in a Location.

```sql
SELECT
name,
createTime,
displayName,
encryptionSpec,
endTime,
error,
jobSpec,
labels,
satisfiesPzi,
satisfiesPzs,
startTime,
state,
updateTime,
webAccessUris
FROM google.aiplatform.custom_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_jobs</code> resource.

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
INSERT INTO google.aiplatform.custom_jobs (
locationsId,
projectsId,
displayName,
encryptionSpec,
labels,
jobSpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ encryptionSpec }}',
'{{ labels }}',
'{{ jobSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: '{{ displayName }}'
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: '{{ kmsKeyName }}'
    - name: labels
      value: '{{ labels }}'
    - name: jobSpec
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>custom_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.custom_jobs
WHERE customJobsId = '{{ customJobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
