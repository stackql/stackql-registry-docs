---
title: notebook_execution_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_execution_jobs
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

Creates, updates, deletes, gets or lists a <code>notebook_execution_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_execution_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.notebook_execution_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this NotebookExecutionJob. Format: `projects/{project_id}/locations/{location}/notebookExecutionJobs/{job_id}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this NotebookExecutionJob was created. |
| <CopyableCode code="dataformRepositorySource" /> | `object` | The Dataform Repository containing the input notebook. |
| <CopyableCode code="directNotebookSource" /> | `object` | The content of the input notebook in ipynb format. |
| <CopyableCode code="displayName" /> | `string` | The display name of the NotebookExecutionJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="executionTimeout" /> | `string` | Max running time of the execution job in seconds (default 86400s / 24 hrs). |
| <CopyableCode code="executionUser" /> | `string` | The user email to run the execution as. Only supported by Colab runtimes. |
| <CopyableCode code="gcsNotebookSource" /> | `object` | The Cloud Storage uri for the input notebook. |
| <CopyableCode code="gcsOutputUri" /> | `string` | The Cloud Storage location to upload the result to. Format: `gs://bucket-name` |
| <CopyableCode code="jobState" /> | `string` | Output only. The state of the NotebookExecutionJob. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize NotebookExecutionJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="notebookRuntimeTemplateResourceName" /> | `string` | The NotebookRuntimeTemplate to source compute configuration from. |
| <CopyableCode code="scheduleResourceName" /> | `string` | Output only. The Schedule resource name if this job is triggered by one. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}` |
| <CopyableCode code="serviceAccount" /> | `string` | The service account to run the execution as. |
| <CopyableCode code="status" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this NotebookExecutionJob was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, notebookExecutionJobsId, projectsId" /> | Gets a NotebookExecutionJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists NotebookExecutionJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a NotebookExecutionJob. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, notebookExecutionJobsId, projectsId" /> | Deletes a NotebookExecutionJob. |

## `SELECT` examples

Lists NotebookExecutionJobs in a Location.

```sql
SELECT
name,
createTime,
dataformRepositorySource,
directNotebookSource,
displayName,
encryptionSpec,
executionTimeout,
executionUser,
gcsNotebookSource,
gcsOutputUri,
jobState,
labels,
notebookRuntimeTemplateResourceName,
scheduleResourceName,
serviceAccount,
status,
updateTime
FROM google.aiplatform.notebook_execution_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notebook_execution_jobs</code> resource.

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
INSERT INTO google.aiplatform.notebook_execution_jobs (
locationsId,
projectsId,
notebookRuntimeTemplateResourceName,
executionTimeout,
gcsOutputUri,
serviceAccount,
encryptionSpec,
displayName,
dataformRepositorySource,
executionUser,
gcsNotebookSource,
labels,
directNotebookSource
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ notebookRuntimeTemplateResourceName }}',
'{{ executionTimeout }}',
'{{ gcsOutputUri }}',
'{{ serviceAccount }}',
'{{ encryptionSpec }}',
'{{ displayName }}',
'{{ dataformRepositorySource }}',
'{{ executionUser }}',
'{{ gcsNotebookSource }}',
'{{ labels }}',
'{{ directNotebookSource }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
updateTime: string
createTime: string
notebookRuntimeTemplateResourceName: string
executionTimeout: string
gcsOutputUri: string
serviceAccount: string
encryptionSpec:
  kmsKeyName: string
displayName: string
dataformRepositorySource:
  commitSha: string
  dataformRepositoryResourceName: string
executionUser: string
scheduleResourceName: string
name: string
gcsNotebookSource:
  generation: string
  uri: string
labels: object
directNotebookSource:
  content: string
status:
  message: string
  code: integer
  details:
    - additionalProperties: any
      type: string
jobState: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notebook_execution_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.notebook_execution_jobs
WHERE locationsId = '{{ locationsId }}'
AND notebookExecutionJobsId = '{{ notebookExecutionJobsId }}'
AND projectsId = '{{ projectsId }}';
```
