---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - iam
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the `Policy`, which must be unique. Format: `policies/&#123;attachment_point&#125;/denypolicies/&#123;policy_id&#125;` The attachment point is identified by its URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-deny-policy`. For organizations and folders, use the numeric ID in the full resource name. For projects, requests can use the alphanumeric or the numeric ID. Responses always contain the numeric ID. |
| `uid` | `string` | Immutable. The globally unique ID of the `Policy`. Assigned automatically when the `Policy` is created. |
| `updateTime` | `string` | Output only. The time when the `Policy` was last updated. |
| `annotations` | `object` | A key-value map to store arbitrary metadata for the `Policy`. Keys can be up to 63 characters. Values can be up to 255 characters. |
| `displayName` | `string` | A user-specified description of the `Policy`. This value can be up to 63 characters. |
| `rules` | `array` | A list of rules that specify the behavior of the `Policy`. All of the rules should be of the `kind` specified in the `Policy`. |
| `createTime` | `string` | Output only. The time when the `Policy` was created. |
| `etag` | `string` | An opaque tag that identifies the current version of the `Policy`. IAM uses this value to help manage concurrent updates, so they do not cause one update to be overwritten by another. If this field is present in a CreatePolicyRequest, the value is ignored. |
| `deleteTime` | `string` | Output only. The time when the `Policy` was deleted. Empty if the policy is not deleted. |
| `kind` | `string` | Output only. The kind of the `Policy`. Always contains the value `DenyPolicy`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policiesId, policiesId1, policiesId2` | Gets a policy. |
| `list_policies` | `SELECT` | `policiesId, policiesId1` | Retrieves the policies of the specified kind that are attached to a resource. The response lists only policy metadata. In particular, policy rules are omitted. |
| `create_policy` | `INSERT` | `policiesId, policiesId1` | Creates a policy. |
| `delete` | `DELETE` | `policiesId, policiesId1, policiesId2` | Deletes a policy. This action is permanent. |
| `_list_policies` | `EXEC` | `policiesId, policiesId1` | Retrieves the policies of the specified kind that are attached to a resource. The response lists only policy metadata. In particular, policy rules are omitted. |
| `update` | `EXEC` | `policiesId, policiesId1, policiesId2` | Updates the specified policy. You can update only the rules and the display name for the policy. To update a policy, you should use a read-modify-write loop: 1. Use GetPolicy to read the current version of the policy. 2. Modify the policy as needed. 3. Use `UpdatePolicy` to write the updated policy. This pattern helps prevent conflicts between concurrent updates. |
