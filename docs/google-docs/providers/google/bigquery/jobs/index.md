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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output-only] Opaque ID field of the job |
| `selfLink` | `string` | [Output-only] A URL that can be used to access this resource again. |
| `statistics` | `object` |  |
| `user_email` | `string` | [Output-only] Email address of the user who ran the job. |
| `configuration` | `object` |  |
| `etag` | `string` | [Output-only] A hash of this resource. |
| `jobReference` | `object` |  |
| `status` | `object` |  |
| `kind` | `string` | [Output-only] The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobId, projectId` | Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role. |
| `list` | `SELECT` | `projectId` | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| `insert` | `INSERT` | `projectId` | Starts a new asynchronous job. Requires the Can View project role. |
| `delete` | `DELETE` | `jobId, projectId` | Requests the deletion of the metadata of a job. This call returns when the job's metadata is deleted. |
| `cancel` | `EXEC` | `jobId, projectId` | Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs. |
| `query` | `EXEC` | `projectId` | Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout. |
