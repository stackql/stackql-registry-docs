---
title: patch_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_deployments
  - osconfig
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
<tr><td><b>Name</b></td><td><code>patch_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.patch_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/{project_id}/patchDeployments/{patch_deployment_id}`. This field is ignored when you create a new patch deployment. |
| `description` | `string` | Optional. Description of the patch deployment. Length of the description is limited to 1024 characters. |
| `updateTime` | `string` | Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `state` | `string` | Output only. Current state of the patch deployment. |
| `duration` | `string` | Optional. Duration of the patch. After the duration ends, the patch times out. |
| `rollout` | `object` | Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs. |
| `lastExecuteTime` | `string` | Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `patchConfig` | `object` | Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance. |
| `recurringSchedule` | `object` | Sets the time for recurring patch deployments. |
| `createTime` | `string` | Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `instanceFilter` | `object` | A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones. |
| `oneTimeSchedule` | `object` | Sets the time for a one time patch deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_patchDeployments_get` | `SELECT` | `patchDeploymentsId, projectsId` | Get an OS Config patch deployment. |
| `projects_patchDeployments_list` | `SELECT` | `projectsId` | Get a page of OS Config patch deployments. |
| `projects_patchDeployments_create` | `INSERT` | `projectsId` | Create an OS Config patch deployment. |
| `projects_patchDeployments_delete` | `DELETE` | `patchDeploymentsId, projectsId` | Delete an OS Config patch deployment. |
| `projects_patchDeployments_patch` | `EXEC` | `patchDeploymentsId, projectsId` | Update an OS Config patch deployment. |
| `projects_patchDeployments_pause` | `EXEC` | `patchDeploymentsId, projectsId` | Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs. |
| `projects_patchDeployments_resume` | `EXEC` | `patchDeploymentsId, projectsId` | Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs. |
