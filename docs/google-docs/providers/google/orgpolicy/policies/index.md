---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.orgpolicy.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the Policy. Must be one of the following forms, where constraint_name is the name of the constraint which this Policy configures: * `projects/{project_number}/policies/{constraint_name}` * `folders/{folder_id}/policies/{constraint_name}` * `organizations/{organization_id}/policies/{constraint_name}` For example, "projects/123/policies/compute.disableSerialPortAccess". Note: `projects/{project_id}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| `alternate` | `object` | Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch. |
| `spec` | `object` | Defines a Cloud Organization `PolicySpec` which is used to specify `Constraints` for configurations of Cloud Platform resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_policies_get` | `SELECT` | `foldersId, policiesId` | Gets a `Policy` on a resource. If no `Policy` is set on the resource, NOT_FOUND is returned. The `etag` value can be used with `UpdatePolicy()` to update a `Policy` during read-modify-write. |
| `folders_policies_list` | `SELECT` | `foldersId` | Retrieves all of the `Policies` that exist on a particular resource. |
| `organizations_policies_get` | `SELECT` | `organizationsId, policiesId` | Gets a `Policy` on a resource. If no `Policy` is set on the resource, NOT_FOUND is returned. The `etag` value can be used with `UpdatePolicy()` to update a `Policy` during read-modify-write. |
| `organizations_policies_list` | `SELECT` | `organizationsId` | Retrieves all of the `Policies` that exist on a particular resource. |
| `projects_policies_get` | `SELECT` | `policiesId, projectsId` | Gets a `Policy` on a resource. If no `Policy` is set on the resource, NOT_FOUND is returned. The `etag` value can be used with `UpdatePolicy()` to update a `Policy` during read-modify-write. |
| `projects_policies_list` | `SELECT` | `projectsId` | Retrieves all of the `Policies` that exist on a particular resource. |
| `folders_policies_create` | `INSERT` | `foldersId` | Creates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Cloud resource. |
| `organizations_policies_create` | `INSERT` | `organizationsId` | Creates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Cloud resource. |
| `projects_policies_create` | `INSERT` | `projectsId` | Creates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Cloud resource. |
| `folders_policies_delete` | `DELETE` | `foldersId, policiesId` | Deletes a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or Org Policy does not exist. |
| `organizations_policies_delete` | `DELETE` | `organizationsId, policiesId` | Deletes a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or Org Policy does not exist. |
| `projects_policies_delete` | `DELETE` | `policiesId, projectsId` | Deletes a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or Org Policy does not exist. |
| `folders_policies_patch` | `EXEC` | `foldersId, policiesId` | Updates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
| `organizations_policies_patch` | `EXEC` | `organizationsId, policiesId` | Updates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
| `projects_policies_patch` | `EXEC` | `policiesId, projectsId` | Updates a Policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
