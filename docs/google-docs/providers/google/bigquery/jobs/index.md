---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - bigquery
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output-only] Opaque ID field of the job |
| <CopyableCode code="configuration" /> | `object` |  |
| <CopyableCode code="etag" /> | `string` | [Output-only] A hash of this resource. |
| <CopyableCode code="jobReference" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | [Output-only] The type of the resource. |
| <CopyableCode code="selfLink" /> | `string` | [Output-only] A URL that can be used to access this resource again. |
| <CopyableCode code="statistics" /> | `object` |  |
| <CopyableCode code="status" /> | `object` |  |
| <CopyableCode code="user_email" /> | `string` | [Output-only] Email address of the user who ran the job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> | Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectId" /> | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="projectId" /> | Starts a new asynchronous job. Requires the Can View project role. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+jobId, projectId" /> | Requests the deletion of the metadata of a job. This call returns when the job's metadata is deleted. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectId" /> | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobId, projectId" /> | Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="projectId" /> | Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout. |
