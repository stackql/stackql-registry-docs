---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - datapipelines
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datapipelines.pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The pipeline name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID`. * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), and periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). * `LOCATION_ID` is the canonical ID for the pipeline's location. The list of available locations can be obtained by calling `google.cloud.location.Locations.ListLocations`. Note that the Data Pipelines service is not available in all regions. It depends on Cloud Scheduler, an App Engine application, so it's only available in [App Engine regions](https://cloud.google.com/about/locations#region). * `PIPELINE_ID` is the ID of the pipeline. Must be unique for the selected project and location. |
| <CopyableCode code="createTime" /> | `string` | Output only. Immutable. The timestamp when the pipeline was initially created. Set by the Data Pipelines service. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the pipeline. It can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), and underscores (_). |
| <CopyableCode code="jobCount" /> | `integer` | Output only. Number of jobs. |
| <CopyableCode code="lastUpdateTime" /> | `string` | Output only. Immutable. The timestamp when the pipeline was last modified. Set by the Data Pipelines service. |
| <CopyableCode code="pipelineSources" /> | `object` | Immutable. The sources of the pipeline (for example, Dataplex). The keys and values are set by the corresponding sources during pipeline creation. |
| <CopyableCode code="scheduleInfo" /> | `object` | Details of the schedule the pipeline runs on. |
| <CopyableCode code="schedulerServiceAccountEmail" /> | `string` | Optional. A service account email to be used with the Cloud Scheduler job. If not specified, the default compute engine service account will be used. |
| <CopyableCode code="state" /> | `string` | Required. The state of the pipeline. When the pipeline is created, the state is set to 'PIPELINE_STATE_ACTIVE' by default. State changes can be requested by setting the state to stopping, paused, or resuming. State cannot be changed through UpdatePipeline requests. |
| <CopyableCode code="type" /> | `string` | Required. The type of the pipeline. This field affects the scheduling of the pipeline and the type of metrics to show for the pipeline. |
| <CopyableCode code="workload" /> | `object` | Workload details for creating the pipeline jobs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, pipelinesId, projectsId" /> | Looks up a single pipeline. Returns a "NOT_FOUND" error if no such pipeline exists. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists pipelines. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a pipeline. For a batch pipeline, you can pass scheduler information. Data Pipelines uses the scheduler information to create an internal scheduler that runs jobs periodically. If the internal scheduler is not configured, you can use RunPipeline to run jobs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, pipelinesId, projectsId" /> | Deletes a pipeline. If a scheduler job is attached to the pipeline, it will be deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, pipelinesId, projectsId" /> | Updates a pipeline. If successful, the updated Pipeline is returned. Returns `NOT_FOUND` if the pipeline doesn't exist. If UpdatePipeline does not return successfully, you can retry the UpdatePipeline request until you receive a successful response. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="locationsId, pipelinesId, projectsId" /> | Creates a job for the specified pipeline directly. You can use this method when the internal scheduler is not configured and you want to trigger the job directly or through an external system. Returns a "NOT_FOUND" error if the pipeline doesn't exist. Returns a "FORBIDDEN" error if the user doesn't have permission to access the pipeline or run jobs for the pipeline. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="locationsId, pipelinesId, projectsId" /> | Freezes pipeline execution permanently. If there's a corresponding scheduler entry, it's deleted, and the pipeline state is changed to "ARCHIVED". However, pipeline metadata is retained. |

## `SELECT` examples

Lists pipelines. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it.

```sql
SELECT
name,
createTime,
displayName,
jobCount,
lastUpdateTime,
pipelineSources,
scheduleInfo,
schedulerServiceAccountEmail,
state,
type,
workload
FROM google.datapipelines.pipelines
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipelines</code> resource.

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
INSERT INTO google.datapipelines.pipelines (
locationsId,
projectsId,
displayName,
name,
type,
pipelineSources,
scheduleInfo,
workload,
state,
schedulerServiceAccountEmail
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ name }}',
'{{ type }}',
'{{ pipelineSources }}',
'{{ scheduleInfo }}',
'{{ workload }}',
'{{ state }}',
'{{ schedulerServiceAccountEmail }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: name
      value: string
    - name: jobCount
      value: integer
    - name: type
      value: string
    - name: pipelineSources
      value: object
    - name: scheduleInfo
      value:
        - name: timeZone
          value: string
        - name: schedule
          value: string
        - name: nextJobTime
          value: string
    - name: workload
      value:
        - name: dataflowLaunchTemplateRequest
          value:
            - name: gcsPath
              value: string
            - name: validateOnly
              value: boolean
            - name: projectId
              value: string
            - name: location
              value: string
            - name: launchParameters
              value:
                - name: update
                  value: boolean
                - name: environment
                  value:
                    - name: workerZone
                      value: string
                    - name: maxWorkers
                      value: integer
                    - name: enableStreamingEngine
                      value: boolean
                    - name: machineType
                      value: string
                    - name: additionalExperiments
                      value:
                        - string
                    - name: zone
                      value: string
                    - name: bypassTempDirValidation
                      value: boolean
                    - name: kmsKeyName
                      value: string
                    - name: additionalUserLabels
                      value: object
                    - name: ipConfiguration
                      value: string
                    - name: tempLocation
                      value: string
                    - name: numWorkers
                      value: integer
                    - name: serviceAccountEmail
                      value: string
                    - name: network
                      value: string
                    - name: subnetwork
                      value: string
                    - name: workerRegion
                      value: string
                - name: parameters
                  value: object
                - name: jobName
                  value: string
                - name: transformNameMapping
                  value: object
        - name: dataflowFlexTemplateRequest
          value:
            - name: validateOnly
              value: boolean
            - name: launchParameter
              value:
                - name: update
                  value: boolean
                - name: transformNameMappings
                  value: object
                - name: parameters
                  value: object
                - name: environment
                  value:
                    - name: enableStreamingEngine
                      value: boolean
                    - name: subnetwork
                      value: string
                    - name: serviceAccountEmail
                      value: string
                    - name: numWorkers
                      value: integer
                    - name: tempLocation
                      value: string
                    - name: zone
                      value: string
                    - name: additionalUserLabels
                      value: object
                    - name: network
                      value: string
                    - name: maxWorkers
                      value: integer
                    - name: kmsKeyName
                      value: string
                    - name: flexrsGoal
                      value: string
                    - name: machineType
                      value: string
                    - name: workerZone
                      value: string
                    - name: workerRegion
                      value: string
                    - name: additionalExperiments
                      value:
                        - string
                    - name: ipConfiguration
                      value: string
                - name: containerSpecGcsPath
                  value: string
                - name: launchOptions
                  value: object
                - name: jobName
                  value: string
            - name: projectId
              value: string
            - name: location
              value: string
    - name: state
      value: string
    - name: lastUpdateTime
      value: string
    - name: createTime
      value: string
    - name: schedulerServiceAccountEmail
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipelines</code> resource.

```sql
/*+ update */
UPDATE google.datapipelines.pipelines
SET 
displayName = '{{ displayName }}',
name = '{{ name }}',
type = '{{ type }}',
pipelineSources = '{{ pipelineSources }}',
scheduleInfo = '{{ scheduleInfo }}',
workload = '{{ workload }}',
state = '{{ state }}',
schedulerServiceAccountEmail = '{{ schedulerServiceAccountEmail }}'
WHERE 
locationsId = '{{ locationsId }}'
AND pipelinesId = '{{ pipelinesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM google.datapipelines.pipelines
WHERE locationsId = '{{ locationsId }}'
AND pipelinesId = '{{ pipelinesId }}'
AND projectsId = '{{ projectsId }}';
```
