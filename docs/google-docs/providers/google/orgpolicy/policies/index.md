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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. |
| `policies` | `array` | All policies that exist on the resource. It will be empty if no policies are set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_policies_get` | `SELECT` | `foldersId, policiesId` | Gets a policy on a resource. If no policy is set on the resource, `NOT_FOUND` is returned. The `etag` value can be used with `UpdatePolicy()` to update a policy during read-modify-write. |
| `folders_policies_list` | `SELECT` | `foldersId` | Retrieves all of the policies that exist on a particular resource. |
| `organizations_policies_get` | `SELECT` | `organizationsId, policiesId` | Gets a policy on a resource. If no policy is set on the resource, `NOT_FOUND` is returned. The `etag` value can be used with `UpdatePolicy()` to update a policy during read-modify-write. |
| `organizations_policies_list` | `SELECT` | `organizationsId` | Retrieves all of the policies that exist on a particular resource. |
| `projects_policies_get` | `SELECT` | `policiesId, projectsId` | Gets a policy on a resource. If no policy is set on the resource, `NOT_FOUND` is returned. The `etag` value can be used with `UpdatePolicy()` to update a policy during read-modify-write. |
| `projects_policies_list` | `SELECT` | `projectsId` | Retrieves all of the policies that exist on a particular resource. |
| `folders_policies_create` | `INSERT` | `foldersId` | Creates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Google Cloud resource. |
| `organizations_policies_create` | `INSERT` | `organizationsId` | Creates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Google Cloud resource. |
| `projects_policies_create` | `INSERT` | `projectsId` | Creates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Google Cloud resource. |
| `folders_policies_delete` | `DELETE` | `foldersId, policiesId` | Deletes a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or organization policy does not exist. |
| `organizations_policies_delete` | `DELETE` | `organizationsId, policiesId` | Deletes a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or organization policy does not exist. |
| `projects_policies_delete` | `DELETE` | `policiesId, projectsId` | Deletes a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or organization policy does not exist. |
| `folders_policies_patch` | `EXEC` | `foldersId, policiesId` | Updates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
| `organizations_policies_patch` | `EXEC` | `organizationsId, policiesId` | Updates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
| `projects_policies_patch` | `EXEC` | `policiesId, projectsId` | Updates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
