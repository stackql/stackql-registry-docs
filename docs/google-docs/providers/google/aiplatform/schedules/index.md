---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
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

Creates, updates, deletes, gets or lists a <code>schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the Schedule. |
| <CopyableCode code="allowQueueing" /> | `boolean` | Optional. Whether new scheduled runs can be queued when max_concurrent_runs limit is reached. If set to true, new runs will be queued instead of skipped. Default to false. |
| <CopyableCode code="catchUp" /> | `boolean` | Output only. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. Default to false. |
| <CopyableCode code="createNotebookExecutionJobRequest" /> | `object` | Request message for [NotebookService.CreateNotebookExecutionJob] |
| <CopyableCode code="createPipelineJobRequest" /> | `object` | Request message for PipelineService.CreatePipelineJob. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Schedule was created. |
| <CopyableCode code="cron" /> | `string` | Cron schedule (https://en.wikipedia.org/wiki/Cron) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *". |
| <CopyableCode code="displayName" /> | `string` | Required. User provided name of the Schedule. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="endTime" /> | `string` | Optional. Timestamp after which no new runs can be scheduled. If specified, The schedule will be completed when either end_time is reached or when scheduled_run_count >= max_run_count. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified. |
| <CopyableCode code="lastPauseTime" /> | `string` | Output only. Timestamp when this Schedule was last paused. Unset if never paused. |
| <CopyableCode code="lastResumeTime" /> | `string` | Output only. Timestamp when this Schedule was last resumed. Unset if never resumed from pause. |
| <CopyableCode code="lastScheduledRunResponse" /> | `object` | Status of a scheduled run. |
| <CopyableCode code="maxConcurrentRunCount" /> | `string` | Required. Maximum number of runs that can be started concurrently for this Schedule. This is the limit for starting the scheduled requests and not the execution of the operations/jobs created by the requests (if applicable). |
| <CopyableCode code="maxRunCount" /> | `string` | Optional. Maximum run count of the schedule. If specified, The schedule will be completed when either started_run_count >= max_run_count or when end_time is reached. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified. |
| <CopyableCode code="nextRunTime" /> | `string` | Output only. Timestamp when this Schedule should schedule the next run. Having a next_run_time in the past means the runs are being started behind schedule. |
| <CopyableCode code="startTime" /> | `string` | Optional. Timestamp after which the first run can be scheduled. Default to Schedule create time if not specified. |
| <CopyableCode code="startedRunCount" /> | `string` | Output only. The number of runs started by this schedule. |
| <CopyableCode code="state" /> | `string` | Output only. The state of this Schedule. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Schedule was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, schedulesId" /> | Gets a Schedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Schedules in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, schedulesId" /> | Deletes a Schedule. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, schedulesId" /> | Updates an active or paused Schedule. When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, schedulesId" /> | Pauses a Schedule. Will mark Schedule.state to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, schedulesId" /> | Resumes a paused Schedule to start scheduling new runs. Will mark Schedule.state to 'ACTIVE'. Only paused Schedule can be resumed. When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If Schedule.catchUp is set up true, all missed runs will be scheduled for backfill first. |

## `SELECT` examples

Lists Schedules in a Location.

```sql
SELECT
name,
allowQueueing,
catchUp,
createNotebookExecutionJobRequest,
createPipelineJobRequest,
createTime,
cron,
displayName,
endTime,
lastPauseTime,
lastResumeTime,
lastScheduledRunResponse,
maxConcurrentRunCount,
maxRunCount,
nextRunTime,
startTime,
startedRunCount,
state,
updateTime
FROM google.aiplatform.schedules
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schedules</code> resource.

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
INSERT INTO google.aiplatform.schedules (
locationsId,
projectsId,
displayName,
allowQueueing,
cron,
endTime,
createNotebookExecutionJobRequest,
maxConcurrentRunCount,
maxRunCount,
startTime,
name,
createPipelineJobRequest
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
true|false,
'{{ cron }}',
'{{ endTime }}',
'{{ createNotebookExecutionJobRequest }}',
'{{ maxConcurrentRunCount }}',
'{{ maxRunCount }}',
'{{ startTime }}',
'{{ name }}',
'{{ createPipelineJobRequest }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
lastPauseTime: string
displayName: string
nextRunTime: string
lastScheduledRunResponse:
  runResponse: string
  scheduledRunTime: string
allowQueueing: boolean
createTime: string
startedRunCount: string
lastResumeTime: string
cron: string
endTime: string
createNotebookExecutionJobRequest:
  notebookExecutionJobId: string
  parent: string
  notebookExecutionJob:
    scheduleResourceName: string
    executionTimeout: string
    notebookRuntimeTemplateResourceName: string
    createTime: string
    labels: object
    directNotebookSource:
      content: string
    name: string
    displayName: string
    updateTime: string
    serviceAccount: string
    status:
      code: integer
      message: string
      details:
        - additionalProperties: any
          type: string
    jobState: string
    gcsNotebookSource:
      uri: string
      generation: string
    executionUser: string
    gcsOutputUri: string
    encryptionSpec:
      kmsKeyName: string
    dataformRepositorySource:
      commitSha: string
      dataformRepositoryResourceName: string
catchUp: boolean
maxConcurrentRunCount: string
state: string
maxRunCount: string
startTime: string
name: string
createPipelineJobRequest:
  pipelineJobId: string
  parent: string
  pipelineJob:
    pipelineSpec: object
    displayName: string
    templateMetadata:
      version: string
    network: string
    preflightValidations: boolean
    startTime: string
    labels: object
    createTime: string
    updateTime: string
    templateUri: string
    scheduleName: string
    name: string
    endTime: string
    state: string
    jobDetail:
      pipelineRunContext:
        parentContexts:
          - type: string
        schemaVersion: string
        etag: string
        schemaTitle: string
        description: string
        updateTime: string
        name: string
        labels: object
        displayName: string
        metadata: object
        createTime: string
      taskDetails:
        - executorDetail:
            containerDetail:
              failedPreCachingCheckJobs:
                - type: string
              mainJob: string
              preCachingCheckJob: string
              failedMainJobs:
                - type: string
            customJobDetail:
              failedJobs:
                - type: string
              job: string
          inputs: object
          execution:
            schemaVersion: string
            metadata: object
            createTime: string
            labels: object
            name: string
            updateTime: string
            displayName: string
            description: string
            state: string
            schemaTitle: string
            etag: string
          pipelineTaskStatus:
            - updateTime: string
              state: string
          taskName: string
          createTime: string
          outputs: object
          endTime: string
          parentTaskId: string
          state: string
          startTime: string
          taskId: string
    serviceAccount: string
    reservedIpRanges:
      - type: string
    runtimeConfig:
      failurePolicy: string
      inputArtifacts: object
      parameters: object
      parameterValues: object
      gcsOutputDirectory: string
updateTime: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schedules</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.schedules
SET 
displayName = '{{ displayName }}',
allowQueueing = true|false,
cron = '{{ cron }}',
endTime = '{{ endTime }}',
createNotebookExecutionJobRequest = '{{ createNotebookExecutionJobRequest }}',
maxConcurrentRunCount = '{{ maxConcurrentRunCount }}',
maxRunCount = '{{ maxRunCount }}',
startTime = '{{ startTime }}',
name = '{{ name }}',
createPipelineJobRequest = '{{ createPipelineJobRequest }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND schedulesId = '{{ schedulesId }}';
```

## `DELETE` example

Deletes the specified <code>schedules</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.schedules
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND schedulesId = '{{ schedulesId }}';
```
