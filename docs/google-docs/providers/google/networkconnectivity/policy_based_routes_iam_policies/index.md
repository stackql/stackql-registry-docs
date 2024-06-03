---
title: policy_based_routes_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_based_routes_iam_policies
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>policy_based_routes_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.policy_based_routes_iam_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="condition" /> | `object` | Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at https://github.com/google/cel-spec. Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() &lt; 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information. |
| <CopyableCode code="members" /> | `array` | Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values: * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account. * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account. Does not include identities that come from external identity providers (IdPs) through identity federation. * `user:&#123;emailid&#125;`: An email address that represents a specific Google account. For example, `alice@example.com` . * `serviceAccount:&#123;emailid&#125;`: An email address that represents a Google service account. For example, `my-other-app@appspot.gserviceaccount.com`. * `serviceAccount:&#123;projectid&#125;.svc.id.goog[&#123;namespace&#125;/&#123;kubernetes-sa&#125;]`: An identifier for a [Kubernetes service account](https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts). For example, `my-project.svc.id.goog[my-namespace/my-kubernetes-sa]`. * `group:&#123;emailid&#125;`: An email address that represents a Google group. For example, `admins@example.com`. * `domain:&#123;domain&#125;`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`. * `principal://iam.googleapis.com/locations/global/workforcePools/&#123;pool_id&#125;/subject/&#123;subject_attribute_value&#125;`: A single identity in a workforce identity pool. * `principalSet://iam.googleapis.com/locations/global/workforcePools/&#123;pool_id&#125;/group/&#123;group_id&#125;`: All workforce identities in a group. * `principalSet://iam.googleapis.com/locations/global/workforcePools/&#123;pool_id&#125;/attribute.&#123;attribute_name&#125;/&#123;attribute_value&#125;`: All workforce identities with a specific attribute value. * `principalSet://iam.googleapis.com/locations/global/workforcePools/&#123;pool_id&#125;/*`: All identities in a workforce identity pool. * `principal://iam.googleapis.com/projects/&#123;project_number&#125;/locations/global/workloadIdentityPools/&#123;pool_id&#125;/subject/&#123;subject_attribute_value&#125;`: A single identity in a workload identity pool. * `principalSet://iam.googleapis.com/projects/&#123;project_number&#125;/locations/global/workloadIdentityPools/&#123;pool_id&#125;/group/&#123;group_id&#125;`: A workload identity pool group. * `principalSet://iam.googleapis.com/projects/&#123;project_number&#125;/locations/global/workloadIdentityPools/&#123;pool_id&#125;/attribute.&#123;attribute_name&#125;/&#123;attribute_value&#125;`: All identities in a workload identity pool with a certain attribute. * `principalSet://iam.googleapis.com/projects/&#123;project_number&#125;/locations/global/workloadIdentityPools/&#123;pool_id&#125;/*`: All identities in a workload identity pool. * `deleted:user:&#123;emailid&#125;?uid=&#123;uniqueid&#125;`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:&#123;emailid&#125;` and the recovered user retains the role in the binding. * `deleted:serviceAccount:&#123;emailid&#125;?uid=&#123;uniqueid&#125;`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:&#123;emailid&#125;` and the undeleted service account retains the role in the binding. * `deleted:group:&#123;emailid&#125;?uid=&#123;uniqueid&#125;`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:&#123;emailid&#125;` and the recovered group retains the role in the binding. * `deleted:principal://iam.googleapis.com/locations/global/workforcePools/&#123;pool_id&#125;/subject/&#123;subject_attribute_value&#125;`: Deleted single identity in a workforce identity pool. For example, `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-pool-id/subject/my-subject-attribute-value`. |
| <CopyableCode code="role" /> | `string` | Role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. For an overview of the IAM roles and permissions, see the [IAM documentation](https://cloud.google.com/iam/docs/roles-overview). For a list of the available pre-defined roles, see [here](https://cloud.google.com/iam/docs/understanding-roles). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_policy" /> | `SELECT` | <CopyableCode code="policyBasedRoutesId, projectsId" /> | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| <CopyableCode code="_get_iam_policy" /> | `EXEC` | <CopyableCode code="policyBasedRoutesId, projectsId" /> | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| <CopyableCode code="set_iam_policy" /> | `EXEC` | <CopyableCode code="policyBasedRoutesId, projectsId" /> | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| <CopyableCode code="test_iam_permissions" /> | `EXEC` | <CopyableCode code="policyBasedRoutesId, projectsId" /> | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
