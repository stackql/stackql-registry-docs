---
title: pipeline_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_jobs
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

Creates, updates, deletes, gets or lists a <code>pipeline_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.pipeline_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the PipelineJob. |
| <CopyableCode code="createTime" /> | `string` | Output only. Pipeline creation time. |
| <CopyableCode code="displayName" /> | `string` | The display name of the Pipeline. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endTime" /> | `string` | Output only. Pipeline end time. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="jobDetail" /> | `object` | The runtime detail of PipelineJob. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize PipelineJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. Note there is some reserved label key for Vertex AI Pipelines. - `vertex-ai-pipelines-run-billing-id`, user set value will get overrided. |
| <CopyableCode code="network" /> | `string` | The full name of the Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the Pipeline Job's workload should be peered. For example, `projects/12345/global/networks/myVPC`. [Format](/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name. Private services access must already be configured for the network. Pipeline job will apply the network configuration to the Google Cloud resources being launched, if applied, such as Vertex AI Training or Dataflow job. If left unspecified, the workload is not peered with any network. |
| <CopyableCode code="pipelineSpec" /> | `object` | The spec of the pipeline. |
| <CopyableCode code="preflightValidations" /> | `boolean` | Optional. Whether to do component level validations before job creation. |
| <CopyableCode code="reservedIpRanges" /> | `array` | A list of names for the reserved ip ranges under the VPC network that can be used for this Pipeline Job's workload. If set, we will deploy the Pipeline Job's workload within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network. Example: ['vertex-ai-ip-range']. |
| <CopyableCode code="runtimeConfig" /> | `object` | The runtime config of a PipelineJob. |
| <CopyableCode code="scheduleName" /> | `string` | Output only. The schedule resource name. Only returned if the Pipeline is created by Schedule API. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account that the pipeline workload runs as. If not specified, the Compute Engine default service account in the project will be used. See https://cloud.google.com/compute/docs/access/service-accounts#default_service_account Users starting the pipeline must have the `iam.serviceAccounts.actAs` permission on this service account. |
| <CopyableCode code="startTime" /> | `string` | Output only. Pipeline start time. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the job. |
| <CopyableCode code="templateMetadata" /> | `object` | Pipeline template metadata if PipelineJob.template_uri is from supported template registry. Currently, the only supported registry is Artifact Registry. |
| <CopyableCode code="templateUri" /> | `string` | A template uri from where the PipelineJob.pipeline_spec, if empty, will be downloaded. Currently, only uri from Vertex Template Registry & Gallery is supported. Reference to https://cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this PipelineJob was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, pipelineJobsId, projectsId" /> | Gets a PipelineJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists PipelineJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a PipelineJob. A PipelineJob will run immediately when created. |
| <CopyableCode code="batch_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId" /> | Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, pipelineJobsId, projectsId" /> | Deletes a PipelineJob. |
| <CopyableCode code="batch_cancel" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="locationsId, pipelineJobsId, projectsId" /> | Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`. |

## `SELECT` examples

Lists PipelineJobs in a Location.

```sql
SELECT
name,
createTime,
displayName,
encryptionSpec,
endTime,
error,
jobDetail,
labels,
network,
pipelineSpec,
preflightValidations,
reservedIpRanges,
runtimeConfig,
scheduleName,
serviceAccount,
startTime,
state,
templateMetadata,
templateUri,
updateTime
FROM google.aiplatform.pipeline_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline_jobs</code> resource.

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
INSERT INTO google.aiplatform.pipeline_jobs (
locationsId,
projectsId,
pipelineSpec,
displayName,
network,
preflightValidations,
labels,
templateUri,
serviceAccount,
reservedIpRanges,
encryptionSpec,
runtimeConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ pipelineSpec }}',
'{{ displayName }}',
'{{ network }}',
true|false,
'{{ labels }}',
'{{ templateUri }}',
'{{ serviceAccount }}',
'{{ reservedIpRanges }}',
'{{ encryptionSpec }}',
'{{ runtimeConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
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
error:
  code: integer
  message: string
  details:
    - additionalProperties: any
      type: string
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
encryptionSpec:
  kmsKeyName: string
runtimeConfig:
  failurePolicy: string
  inputArtifacts: object
  parameters: object
  parameterValues: object
  gcsOutputDirectory: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>pipeline_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.pipeline_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
