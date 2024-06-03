---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - ml
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createTime" /> | `string` | Output only. When the job was created. |
| <CopyableCode code="endTime" /> | `string` | Output only. When the job processing was completed. |
| <CopyableCode code="errorMessage" /> | `string` | Output only. The details of a failure or a cancellation. |
| <CopyableCode code="etag" /> | `string` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job. |
| <CopyableCode code="jobId" /> | `string` | Required. The user-specified id of the job. |
| <CopyableCode code="jobPosition" /> | `string` | Output only. It's only effect when the job is in QUEUED state. If it's positive, it indicates the job's position in the job scheduler. It's 0 when the job is already scheduled. |
| <CopyableCode code="labels" /> | `object` | Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. |
| <CopyableCode code="predictionInput" /> | `object` | Represents input parameters for a prediction job. |
| <CopyableCode code="predictionOutput" /> | `object` | Represents results of a prediction job. |
| <CopyableCode code="startTime" /> | `string` | Output only. When the job processing was started. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a job. |
| <CopyableCode code="trainingInput" /> | `object` | Represents input parameters for a training job. When using the gcloud command to submit your training job, you can specify the input parameters as command-line arguments and/or in a YAML configuration file referenced from the --config command-line argument. For details, see the guide to [submitting a training job](/ai-platform/training/docs/training-jobs). |
| <CopyableCode code="trainingOutput" /> | `object` | Represents results of a training job. Output only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_get" /> | `SELECT` | <CopyableCode code="jobsId, projectsId" /> | Describes a job. |
| <CopyableCode code="projects_jobs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the jobs in the project. If there are no jobs that match the request parameters, the list request returns an empty response body: &#123;&#125;. |
| <CopyableCode code="projects_jobs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a training or a batch prediction job. |
| <CopyableCode code="projects_jobs_patch" /> | `UPDATE` | <CopyableCode code="jobsId, projectsId" /> | Updates a specific job resource. Currently the only supported fields to update are `labels`. |
| <CopyableCode code="_projects_jobs_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists the jobs in the project. If there are no jobs that match the request parameters, the list request returns an empty response body: &#123;&#125;. |
| <CopyableCode code="projects_jobs_cancel" /> | `EXEC` | <CopyableCode code="jobsId, projectsId" /> | Cancels a running job. |
