---
title: report
hide_title: false
hide_table_of_contents: false
keywords:
  - report
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
<tr><td><b>Name</b></td><td><code>report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.report</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The `OSPolicyAssignmentReport` API resource name. Format: `projects/&#123;project_number&#125;/locations/&#123;location&#125;/instances/&#123;instance_id&#125;/osPolicyAssignments/&#123;os_policy_assignment_id&#125;/report` |
| `osPolicyAssignment` | `string` | Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to. Format: `projects/&#123;project_number&#125;/locations/&#123;location&#125;/osPolicyAssignments/&#123;os_policy_assignment_id@revision_id&#125;` |
| `osPolicyCompliances` | `array` | Compliance data for each `OSPolicy` that is applied to the VM. |
| `updateTime` | `string` | Timestamp for when the report was last generated. |
| `instance` | `string` | The Compute Engine VM instance name. |
| `lastRunId` | `string` | Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM. This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `instancesId, locationsId, osPolicyAssignmentsId, projectsId` |
