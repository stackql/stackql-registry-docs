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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.orgpolicy.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint which this policy configures: * `projects/&#123;project_number&#125;/policies/&#123;constraint_name&#125;` * `folders/&#123;folder_id&#125;/policies/&#123;constraint_name&#125;` * `organizations/&#123;organization_id&#125;/policies/&#123;constraint_name&#125;` For example, `projects/123/policies/compute.disableSerialPortAccess`. Note: `projects/&#123;project_id&#125;/policies/&#123;constraint_name&#125;` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| <CopyableCode code="alternate" /> | `object` | Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch. |
| <CopyableCode code="dryRunSpec" /> | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
| <CopyableCode code="spec" /> | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_policies_get" /> | `SELECT` | <CopyableCode code="foldersId, policiesId" /> | Gets a policy on a resource. If no policy is set on the resource, `NOT_FOUND` is returned. The `etag` value can be used with `UpdatePolicy()` to update a policy during read-modify-write. |
| <CopyableCode code="folders_policies_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Retrieves all of the policies that exist on a particular resource. |
| <CopyableCode code="organizations_policies_get" /> | `SELECT` | <CopyableCode code="organizationsId, policiesId" /> | Gets a policy on a resource. If no policy is set on the resource, `NOT_FOUND` is returned. The `etag` value can be used with `UpdatePolicy()` to update a policy during read-modify-write. |
| <CopyableCode code="organizations_policies_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Retrieves all of the policies that exist on a particular resource. |
| <CopyableCode code="projects_policies_get" /> | `SELECT` | <CopyableCode code="policiesId, projectsId" /> | Gets a policy on a resource. If no policy is set on the resource, `NOT_FOUND` is returned. The `etag` value can be used with `UpdatePolicy()` to update a policy during read-modify-write. |
| <CopyableCode code="projects_policies_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Retrieves all of the policies that exist on a particular resource. |
| <CopyableCode code="folders_policies_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Google Cloud resource. |
| <CopyableCode code="organizations_policies_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Google Cloud resource. |
| <CopyableCode code="projects_policies_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the policy already exists on the given Google Cloud resource. |
| <CopyableCode code="folders_policies_delete" /> | `DELETE` | <CopyableCode code="foldersId, policiesId" /> | Deletes a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or organization policy does not exist. |
| <CopyableCode code="organizations_policies_delete" /> | `DELETE` | <CopyableCode code="organizationsId, policiesId" /> | Deletes a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or organization policy does not exist. |
| <CopyableCode code="projects_policies_delete" /> | `DELETE` | <CopyableCode code="policiesId, projectsId" /> | Deletes a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or organization policy does not exist. |
| <CopyableCode code="_folders_policies_list" /> | `EXEC` | <CopyableCode code="foldersId" /> | Retrieves all of the policies that exist on a particular resource. |
| <CopyableCode code="_organizations_policies_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Retrieves all of the policies that exist on a particular resource. |
| <CopyableCode code="_projects_policies_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Retrieves all of the policies that exist on a particular resource. |
| <CopyableCode code="folders_policies_patch" /> | `EXEC` | <CopyableCode code="foldersId, policiesId" /> | Updates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
| <CopyableCode code="organizations_policies_patch" /> | `EXEC` | <CopyableCode code="organizationsId, policiesId" /> | Updates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
| <CopyableCode code="projects_policies_patch" /> | `EXEC` | <CopyableCode code="policiesId, projectsId" /> | Updates a policy. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy do not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields. |
