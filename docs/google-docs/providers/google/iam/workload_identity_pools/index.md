---
title: workload_identity_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_identity_pools
  - iam
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
<tr><td><b>Name</b></td><td><code>workload_identity_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.workload_identity_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the pool. |
| `description` | `string` | A description of the pool. Cannot exceed 256 characters. |
| `displayName` | `string` | A display name for the pool. Cannot exceed 32 characters. |
| `state` | `string` | Output only. The state of the pool. |
| `disabled` | `boolean` | Whether the pool is disabled. You cannot use a disabled pool to exchange tokens, or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workloadIdentityPools_get` | `SELECT` | `locationsId, projectsId, workloadIdentityPoolsId` | Gets an individual WorkloadIdentityPool. |
| `projects_locations_workloadIdentityPools_list` | `SELECT` | `locationsId, projectsId` | Lists all non-deleted WorkloadIdentityPools in a project. If `show_deleted` is set to `true`, then deleted pools are also listed. |
| `projects_locations_workloadIdentityPools_create` | `INSERT` | `locationsId, projectsId` | Creates a new WorkloadIdentityPool. You cannot reuse the name of a deleted pool until 30 days after deletion. |
| `projects_locations_workloadIdentityPools_delete` | `DELETE` | `locationsId, projectsId, workloadIdentityPoolsId` | Deletes a WorkloadIdentityPool. You cannot use a deleted pool to exchange external credentials for Google Cloud credentials. However, deletion does not revoke credentials that have already been issued. Credentials issued for a deleted pool do not grant access to resources. If the pool is undeleted, and the credentials are not expired, they grant access again. You can undelete a pool for 30 days. After 30 days, deletion is permanent. You cannot update deleted pools. However, you can view and list them. |
| `projects_locations_workloadIdentityPools_patch` | `EXEC` | `locationsId, projectsId, workloadIdentityPoolsId` | Updates an existing WorkloadIdentityPool. |
| `projects_locations_workloadIdentityPools_undelete` | `EXEC` | `locationsId, projectsId, workloadIdentityPoolsId` | Undeletes a WorkloadIdentityPool, as long as it was deleted fewer than 30 days ago. |
