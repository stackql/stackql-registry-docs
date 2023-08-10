---
title: clone_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - clone_jobs
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>clone_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.clone_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the clone. |
| `stateTime` | `string` | Output only. The time the state was last updated. |
| `steps` | `array` | Output only. The clone steps list representing its progress. |
| `computeEngineDisksTargetDetails` | `object` | ComputeEngineDisksTargetDetails is a collection of created Persistent Disks details. |
| `computeEngineTargetDetails` | `object` | ComputeEngineTargetDetails is a collection of details for creating a VM in a target Compute Engine project. |
| `endTime` | `string` | Output only. The time the clone job was ended. |
| `state` | `string` | Output only. State of the clone job. |
| `createTime` | `string` | Output only. The time the clone job was created (as an API call, not when it was actually created in the target). |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloneJobsId, locationsId, migratingVmsId, projectsId, sourcesId` | Gets details of a single CloneJob. |
| `list` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists CloneJobs of a given migrating VM. |
| `create` | `INSERT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Initiates a Clone of a specific migrating VM. |
| `_list` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists CloneJobs of a given migrating VM. |
| `cancel` | `EXEC` | `cloneJobsId, locationsId, migratingVmsId, projectsId, sourcesId` | Initiates the cancellation of a running clone job. |
