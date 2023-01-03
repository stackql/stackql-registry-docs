---
title: os_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - os_policy_assignments
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
<tr><td><b>Name</b></td><td><code>os_policy_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.os_policy_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id}` This field is ignored when you create an OS policy assignment. |
| `description` | `string` | OS policy assignment description. Length of the description is limited to 1024 characters. |
| `instanceFilter` | `object` | Filters to select target VMs for an assignment. If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them. |
| `osPolicies` | `array` | Required. List of OS policies to be applied to the VMs. |
| `rollout` | `object` | Message to configure the rollout at the zonal level for the OS policy assignment. |
| `baseline` | `boolean` | Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision. For a given OS policy assignment, there is only one revision with a value of `true` for this field. |
| `deleted` | `boolean` | Output only. Indicates that this revision deletes the OS policy assignment. |
| `reconciling` | `boolean` | Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rollout_state` is one of: * IN_PROGRESS * CANCELLING |
| `etag` | `string` | The etag for this OS policy assignment. If this is provided on update, it must match the server's etag. |
| `rolloutState` | `string` | Output only. OS policy assignment rollout state |
| `uid` | `string` | Output only. Server generated unique id for the OS policy assignment resource. |
| `revisionId` | `string` | Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_osPolicyAssignments_get` | `SELECT` | `locationsId, osPolicyAssignmentsId, projectsId` | Retrieve an existing OS policy assignment. This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter. |
| `projects_locations_osPolicyAssignments_list` | `SELECT` | `locationsId, projectsId` | List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned. |
| `projects_locations_osPolicyAssignments_create` | `INSERT` | `locationsId, projectsId` | Create an OS policy assignment. This method also creates the first revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |
| `projects_locations_osPolicyAssignments_delete` | `DELETE` | `locationsId, osPolicyAssignmentsId, projectsId` | Delete the OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |
| `projects_locations_osPolicyAssignments_patch` | `EXEC` | `locationsId, osPolicyAssignmentsId, projectsId` | Update an existing OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |
