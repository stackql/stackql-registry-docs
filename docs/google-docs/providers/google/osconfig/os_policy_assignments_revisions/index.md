---
title: os_policy_assignments_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - os_policy_assignments_revisions
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>os_policy_assignments_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.os_policy_assignments_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. Format: `projects/&#123;project_number&#125;/locations/&#123;location&#125;/osPolicyAssignments/&#123;os_policy_assignment_id&#125;` This field is ignored when you create an OS policy assignment. |
| `description` | `string` | OS policy assignment description. Length of the description is limited to 1024 characters. |
| `osPolicies` | `array` | Required. List of OS policies to be applied to the VMs. |
| `rollout` | `object` | Message to configure the rollout at the zonal level for the OS policy assignment. |
| `uid` | `string` | Output only. Server generated unique id for the OS policy assignment resource. |
| `baseline` | `boolean` | Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision. For a given OS policy assignment, there is only one revision with a value of `true` for this field. |
| `reconciling` | `boolean` | Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rollout_state` is one of: * IN_PROGRESS * CANCELLING |
| `instanceFilter` | `object` | Filters to select target VMs for an assignment. If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them. |
| `rolloutState` | `string` | Output only. OS policy assignment rollout state |
| `etag` | `string` | The etag for this OS policy assignment. If this is provided on update, it must match the server's etag. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `revisionId` | `string` | Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment |
| `deleted` | `boolean` | Output only. Indicates that this revision deletes the OS policy assignment. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_revisions` | `SELECT` | `locationsId, osPolicyAssignmentsId, projectsId` |
| `_list_revisions` | `EXEC` | `locationsId, osPolicyAssignmentsId, projectsId` |
