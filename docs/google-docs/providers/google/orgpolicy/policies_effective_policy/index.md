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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_effective_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.orgpolicy.policies_effective_policy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint which this policy configures: * `projects/&#123;project_number&#125;/policies/&#123;constraint_name&#125;` * `folders/&#123;folder_id&#125;/policies/&#123;constraint_name&#125;` * `organizations/&#123;organization_id&#125;/policies/&#123;constraint_name&#125;` For example, `projects/123/policies/compute.disableSerialPortAccess`. Note: `projects/&#123;project_id&#125;/policies/&#123;constraint_name&#125;` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| <CopyableCode code="alternate" /> | `object` | Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch. |
| <CopyableCode code="dryRunSpec" /> | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
| <CopyableCode code="etag" /> | `string` | Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This 'etag' is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="spec" /> | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="folders_policies_get_effective_policy" /> | `SELECT` | <CopyableCode code="foldersId, policiesId" /> |
| <CopyableCode code="organizations_policies_get_effective_policy" /> | `SELECT` | <CopyableCode code="organizationsId, policiesId" /> |
| <CopyableCode code="projects_policies_get_effective_policy" /> | `SELECT` | <CopyableCode code="policiesId, projectsId" /> |
