---
title: policies_effective_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_effective_policy
  - orgpolicy
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
<tr><td><b>Name</b></td><td><code>policies_effective_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.orgpolicy.policies_effective_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the Policy. Must be one of the following forms, where constraint_name is the name of the constraint which this Policy configures: * `projects/{project_number}/policies/{constraint_name}` * `folders/{folder_id}/policies/{constraint_name}` * `organizations/{organization_id}/policies/{constraint_name}` For example, "projects/123/policies/compute.disableSerialPortAccess". Note: `projects/{project_id}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| `spec` | `object` | Defines a Cloud Organization `PolicySpec` which is used to specify `Constraints` for configurations of Cloud Platform resources. |
| `alternate` | `object` | Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_policies_getEffectivePolicy` | `SELECT` | `foldersId, policiesId` |
| `organizations_policies_getEffectivePolicy` | `SELECT` | `organizationsId, policiesId` |
| `projects_policies_getEffectivePolicy` | `SELECT` | `policiesId, projectsId` |
