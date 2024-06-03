---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - accesscontextmanager
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
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accesscontextmanager.access_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the `AccessPolicy`. Format: `accessPolicies/&#123;access_policy&#125;` |
| <CopyableCode code="etag" /> | `string` | Output only. An opaque identifier for the current version of the `AccessPolicy`. This will always be a strongly validated etag, meaning that two Access Polices will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format. |
| <CopyableCode code="parent" /> | `string` | Required. The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/&#123;organization_id&#125;` |
| <CopyableCode code="scopes" /> | `array` | The scopes of the AccessPolicy. Scopes define which resources a policy can restrict and where its resources can be referenced. For example, policy A with `scopes=["folders/123"]` has the following behavior: - ServicePerimeter can only restrict projects within `folders/123`. - ServicePerimeter within policy A can only reference access levels defined within policy A. - Only one policy can include a given scope; thus, attempting to create a second policy which includes `folders/123` will result in an error. If no scopes are provided, then any resource within the organization can be restricted. Scopes cannot be modified after a policy is created. Policies can only have a single scope. Format: list of `folders/&#123;folder_number&#125;` or `projects/&#123;project_number&#125;` |
| <CopyableCode code="title" /> | `string` | Required. Human readable title. Does not affect behavior. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPoliciesId" /> | Returns an access policy based on the name. |
| <CopyableCode code="list" /> | `SELECT` |  | Lists all access policies in an organization. |
| <CopyableCode code="create" /> | `INSERT` |  | Creates an access policy. This method fails if the organization already has an access policy. The long-running operation has a successful status after the access policy propagates to long-lasting storage. Syntactic and basic semantic errors are returned in `metadata` as a BadRequest proto. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPoliciesId" /> | Deletes an access policy based on the resource name. The long-running operation has a successful status after the access policy is removed from long-lasting storage. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="accessPoliciesId" /> | Updates an access policy. The long-running operation from this RPC has a successful status after the changes to the access policy propagate to long-lasting storage. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists all access policies in an organization. |
