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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>worker_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.worker_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the `WorkerPool`, with format `projects/&#123;project&#125;/locations/&#123;location&#125;/workerPools/&#123;worker_pool&#125;`. The value of `&#123;worker_pool&#125;` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `&#123;location&#125;` is determined by the endpoint accessed. |
| <CopyableCode code="annotations" /> | `object` | User specified annotations. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the request to create the `WorkerPool` was received. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time at which the request to delete the `WorkerPool` was received. |
| <CopyableCode code="displayName" /> | `string` | A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters. |
| <CopyableCode code="etag" /> | `string` | Output only. Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
| <CopyableCode code="privatePoolV1Config" /> | `object` | Configuration for a V1 `PrivatePool`. |
| <CopyableCode code="state" /> | `string` | Output only. `WorkerPool` state. |
| <CopyableCode code="uid" /> | `string` | Output only. A unique identifier for the `WorkerPool`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time at which the request to update the `WorkerPool` was received. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_worker_pools_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workerPoolsId" /> | Returns details of a `WorkerPool`. |
| <CopyableCode code="projects_locations_worker_pools_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `WorkerPool`s. |
| <CopyableCode code="projects_locations_worker_pools_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a `WorkerPool`. |
| <CopyableCode code="projects_locations_worker_pools_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, workerPoolsId" /> | Deletes a `WorkerPool`. |
| <CopyableCode code="_projects_locations_worker_pools_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists `WorkerPool`s. |
| <CopyableCode code="projects_locations_worker_pools_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workerPoolsId" /> | Updates a `WorkerPool`. |
