---
title: cutover_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - cutover_jobs
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>cutover_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.cutover_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the cutover job. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `progressPercent` | `integer` | Output only. The current progress in percentage of the cutover job. |
| `stateMessage` | `string` | Output only. A message providing possible extra details about the current state. |
| `createTime` | `string` | Output only. The time the cutover job was created (as an API call, not when it was actually created in the target). |
| `state` | `string` | Output only. State of the cutover job. |
| `endTime` | `string` | Output only. The time the cutover job had finished. |
| `stateTime` | `string` | Output only. The time the state was last updated. |
| `computeEngineTargetDetails` | `object` | ComputeEngineTargetDetails is a collection of details for creating a VM in a target Compute Engine project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sources_migratingVms_cutoverJobs_get` | `SELECT` | `cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId` | Gets details of a single CutoverJob. |
| `projects_locations_sources_migratingVms_cutoverJobs_list` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists CutoverJobs of a given migrating VM. |
| `projects_locations_sources_migratingVms_cutoverJobs_create` | `INSERT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Initiates a Cutover of a specific migrating VM. The returned LRO is completed when the cutover job resource is created and the job is initiated. |
| `projects_locations_sources_migratingVms_cutoverJobs_cancel` | `EXEC` | `cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId` | Initiates the cancellation of a running cutover job. |
