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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>os_policy_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.os_policy_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. Format: `projects/&#123;project_number&#125;/locations/&#123;location&#125;/osPolicyAssignments/&#123;os_policy_assignment_id&#125;` This field is ignored when you create an OS policy assignment. |
| <CopyableCode code="description" /> | `string` | OS policy assignment description. Length of the description is limited to 1024 characters. |
| <CopyableCode code="baseline" /> | `boolean` | Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision. For a given OS policy assignment, there is only one revision with a value of `true` for this field. |
| <CopyableCode code="deleted" /> | `boolean` | Output only. Indicates that this revision deletes the OS policy assignment. |
| <CopyableCode code="etag" /> | `string` | The etag for this OS policy assignment. If this is provided on update, it must match the server's etag. |
| <CopyableCode code="instanceFilter" /> | `object` | Filters to select target VMs for an assignment. If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them. |
| <CopyableCode code="osPolicies" /> | `array` | Required. List of OS policies to be applied to the VMs. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rollout_state` is one of: * IN_PROGRESS * CANCELLING |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp that the revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment |
| <CopyableCode code="rollout" /> | `object` | Message to configure the rollout at the zonal level for the OS policy assignment. |
| <CopyableCode code="rolloutState" /> | `string` | Output only. OS policy assignment rollout state |
| <CopyableCode code="uid" /> | `string` | Output only. Server generated unique id for the OS policy assignment resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, osPolicyAssignmentsId, projectsId" /> | Retrieve an existing OS policy assignment. This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create an OS policy assignment. This method also creates the first revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, osPolicyAssignmentsId, projectsId" /> | Delete the OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, osPolicyAssignmentsId, projectsId" /> | Update an existing OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned. |
