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
| <CopyableCode code="id" /> | `string` | Output only. Opaque ID field of the job. |
| <CopyableCode code="configuration" /> | `object` |  |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of this resource. |
| <CopyableCode code="jobCreationReason" /> | `object` | Reason about why a Job was created from a [`jobs.query`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query) method when used with `JOB_CREATION_OPTIONAL` Job creation mode. For [`jobs.insert`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert) method calls it will always be `REQUESTED`. This feature is not yet available. Jobs will always be created. |
| <CopyableCode code="jobReference" /> | `object` | A job reference is a fully qualified identifier for referring to a job. |
| <CopyableCode code="kind" /> | `string` | Output only. The type of the resource. |
| <CopyableCode code="principal_subject" /> | `string` | Output only. [Full-projection-only] String representation of identity of requesting party. Populated for both first- and third-party identities. Only present for APIs that support third-party identities. |
| <CopyableCode code="selfLink" /> | `string` | Output only. A URL that can be used to access the resource again. |
| <CopyableCode code="statistics" /> | `object` | Statistics for a single job execution. |
| <CopyableCode code="status" /> | `object` |  |
| <CopyableCode code="user_email" /> | `string` | Output only. Email address of the user who ran the job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="+jobId, projectId" /> | Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectId" /> | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="projectId" /> | Starts a new asynchronous job. This API has two different kinds of endpoint URIs, as this method supports a variety of use cases. * The *Metadata* URI is used for most interactions, as it accepts the job configuration directly. * The *Upload* URI is ONLY for the case when you're sending both a load job configuration and a data stream together. In this case, the Upload URI accepts the job configuration and the data as two distinct multipart MIME parts. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+jobId, projectId" /> | Requests the deletion of the metadata of a job. This call returns when the job's metadata is deleted. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectId" /> | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="+jobId, projectId" /> | Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="projectId" /> | Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout. |
