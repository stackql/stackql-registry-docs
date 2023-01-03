---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
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
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The `OSPolicyAssignmentReport` API resource name. Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/osPolicyAssignments/{os_policy_assignment_id}/report` |
| `instance` | `string` | The Compute Engine VM instance name. |
| `lastRunId` | `string` | Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM. This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs. |
| `osPolicyAssignment` | `string` | Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to. Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}` |
| `osPolicyCompliances` | `array` | Compliance data for each `OSPolicy` that is applied to the VM. |
| `updateTime` | `string` | Timestamp for when the report was last generated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_instances_osPolicyAssignments_reports_list` | `SELECT` | `instancesId, locationsId, osPolicyAssignmentsId, projectsId` |
