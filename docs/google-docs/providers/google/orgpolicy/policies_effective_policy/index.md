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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint which this policy configures: * `projects/&#123;project_number&#125;/policies/&#123;constraint_name&#125;` * `folders/&#123;folder_id&#125;/policies/&#123;constraint_name&#125;` * `organizations/&#123;organization_id&#125;/policies/&#123;constraint_name&#125;` For example, `projects/123/policies/compute.disableSerialPortAccess`. Note: `projects/&#123;project_id&#125;/policies/&#123;constraint_name&#125;` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| `spec` | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
| `alternate` | `object` | Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch. |
| `dryRunSpec` | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_policies_get_effective_policy` | `SELECT` | `foldersId, policiesId` |
| `organizations_policies_get_effective_policy` | `SELECT` | `organizationsId, policiesId` |
| `projects_policies_get_effective_policy` | `SELECT` | `policiesId, projectsId` |
