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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Output only. The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{worker_pool}`. The value of `{worker_pool}` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `{location}` is determined by the endpoint accessed. |
| `annotations` | `object` | User specified annotations. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `deleteTime` | `string` | Output only. Time at which the request to delete the `WorkerPool` was received. |
| `state` | `string` | Output only. `WorkerPool` state. |
| `privatePoolV1Config` | `object` | Configuration for a V1 `PrivatePool`. |
| `uid` | `string` | Output only. A unique identifier for the `WorkerPool`. |
| `createTime` | `string` | Output only. Time at which the request to create the `WorkerPool` was received. |
| `etag` | `string` | Output only. Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
| `updateTime` | `string` | Output only. Time at which the request to update the `WorkerPool` was received. |
| `displayName` | `string` | A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workerPools_get` | `SELECT` | `locationsId, projectsId, workerPoolsId` | Returns details of a `WorkerPool`. |
| `projects_locations_workerPools_list` | `SELECT` | `locationsId, projectsId` | Lists `WorkerPool`s. |
| `projects_locations_workerPools_create` | `INSERT` | `locationsId, projectsId` | Creates a `WorkerPool`. |
| `projects_locations_workerPools_delete` | `DELETE` | `locationsId, projectsId, workerPoolsId` | Deletes a `WorkerPool`. |
| `projects_locations_workerPools_patch` | `EXEC` | `locationsId, projectsId, workerPoolsId` | Updates a `WorkerPool`. |
