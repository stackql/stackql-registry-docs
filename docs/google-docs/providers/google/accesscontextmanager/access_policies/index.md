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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accesscontextmanager.access_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the `AccessPolicy`. Format: `accessPolicies/{access_policy}` |
| `scopes` | `array` | The scopes of a policy define which resources an ACM policy can restrict, and where ACM resources can be referenced. For example, a policy with scopes=["folders/123"] has the following behavior: - vpcsc perimeters can only restrict projects within folders/123 - access levels can only be referenced by resources within folders/123. If empty, there are no limitations on which resources can be restricted by an ACM policy, and there are no limitations on where ACM resources can be referenced. Only one policy can include a given scope (attempting to create a second policy which includes "folders/123" will result in an error). Currently, scopes cannot be modified after a policy is created. Currently, policies can only have a single scope. Format: list of `folders/{folder_number}` or `projects/{project_number}` |
| `title` | `string` | Required. Human readable title. Does not affect behavior. |
| `etag` | `string` | Output only. An opaque identifier for the current version of the `AccessPolicy`. This will always be a strongly validated etag, meaning that two Access Polices will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format. |
| `parent` | `string` | Required. The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organization_id}` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accessPolicies_get` | `SELECT` | `accessPoliciesId` | Returns an access policy based on the name. |
| `accessPolicies_list` | `SELECT` |  | Lists all access policies in an organization. |
| `accessPolicies_create` | `INSERT` |  | Creates an access policy. This method fails if the organization already has an access policy. The long-running operation has a successful status after the access policy propagates to long-lasting storage. Syntactic and basic semantic errors are returned in `metadata` as a BadRequest proto. |
| `accessPolicies_delete` | `DELETE` | `accessPoliciesId` | Deletes an access policy based on the resource name. The long-running operation has a successful status after the access policy is removed from long-lasting storage. |
| `accessPolicies_patch` | `EXEC` | `accessPoliciesId` | Updates an access policy. The long-running operation from this RPC has a successful status after the changes to the access policy propagate to long-lasting storage. |
