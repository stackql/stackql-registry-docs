---
title: worker_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - worker_pools
  - cloudbuild
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
<tr><td><b>Name</b></td><td><code>worker_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.worker_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Continuation token used to page through large result sets. Provide this value in a subsequent ListWorkerPoolsRequest to return the next page of results. |
| `workerPools` | `array` | `WorkerPools` for the specified project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_worker_pools_list` | `SELECT` | `locationsId, projectsId` | Lists `WorkerPool`s. |
| `projects_locations_worker_pools_create` | `INSERT` | `locationsId, projectsId` | Creates a `WorkerPool`. |
| `projects_locations_worker_pools_delete` | `DELETE` | `locationsId, projectsId, workerPoolsId` | Deletes a `WorkerPool`. |
| `projects_locations_worker_pools_get` | `EXEC` | `locationsId, projectsId, workerPoolsId` | Returns details of a `WorkerPool`. |
| `projects_locations_worker_pools_patch` | `EXEC` | `locationsId, projectsId, workerPoolsId` | Updates a `WorkerPool`. |
