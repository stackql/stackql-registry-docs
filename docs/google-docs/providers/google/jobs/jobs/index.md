---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - jobs
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.jobs.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobs` | `array` | The Jobs for a given company. The maximum number of items returned is based on the limit field provided in the request. |
| `metadata` | `object` | Additional information returned to client, such as debugging information. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, projectsId, tenantsId` | Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days. |
| `list` | `SELECT` | `projectsId, tenantsId` | Lists jobs by filter. |
| `create` | `INSERT` | `projectsId, tenantsId` | Creates a new job. Typically, the job becomes searchable within 10 seconds, but it may take up to 5 minutes. |
| `delete` | `DELETE` | `jobsId, projectsId, tenantsId` | Deletes the specified job. Typically, the job becomes unsearchable within 10 seconds, but it may take up to 5 minutes. |
| `batch_create` | `EXEC` | `projectsId, tenantsId` | Begins executing a batch create jobs operation. |
| `batch_delete` | `EXEC` | `projectsId, tenantsId` | Begins executing a batch delete jobs operation. |
| `batch_update` | `EXEC` | `projectsId, tenantsId` | Begins executing a batch update jobs operation. |
| `patch` | `EXEC` | `jobsId, projectsId, tenantsId` | Updates specified job. Typically, updated contents become visible in search results within 10 seconds, but it may take up to 5 minutes. |
| `search` | `EXEC` | `projectsId, tenantsId` | Searches for jobs using the provided SearchJobsRequest. This call constrains the visibility of jobs present in the database, and only returns jobs that the caller has permission to search against. |
| `search_for_alert` | `EXEC` | `projectsId, tenantsId` | Searches for jobs using the provided SearchJobsRequest. This API call is intended for the use case of targeting passive job seekers (for example, job seekers who have signed up to receive email alerts about potential job opportunities), it has different algorithmic adjustments that are designed to specifically target passive job seekers. This call constrains the visibility of jobs present in the database, and only returns jobs the caller has permission to search against. |
