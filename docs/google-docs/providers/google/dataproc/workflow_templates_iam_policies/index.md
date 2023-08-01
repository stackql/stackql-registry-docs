---
title: workflow_templates_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_templates_iam_policies
  - dataproc
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
<tr><td><b>Name</b></td><td><code>workflow_templates_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.workflow_templates_iam_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workflow_templates_get_iam_policy` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `projects_locations_workflow_templates_set_iam_policy` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors. |
| `projects_locations_workflow_templates_test_iam_permissions` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
| `projects_regions_workflow_templates_get_iam_policy` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `projects_regions_workflow_templates_set_iam_policy` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors. |
| `projects_regions_workflow_templates_test_iam_permissions` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
