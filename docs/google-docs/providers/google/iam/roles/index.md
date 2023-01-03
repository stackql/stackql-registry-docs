---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - iam
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the role. When Role is used in CreateRole, the role name must not be set. When Role is used in output and other input such as UpdateRole, the role name is the complete path, e.g., roles/logging.viewer for predefined roles and organizations/{ORGANIZATION_ID}/roles/logging.viewer for custom roles. |
| `description` | `string` | Optional. A human-readable description for the role. |
| `title` | `string` | Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes. |
| `deleted` | `boolean` | The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole. |
| `etag` | `string` | Used to perform a consistent read-modify-write. |
| `includedPermissions` | `array` | The names of the permissions this role grants when bound in an IAM policy. |
| `stage` | `string` | The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `rolesId` | Gets the definition of a Role. |
| `list` | `SELECT` |  | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| `organizations_roles_get` | `SELECT` | `organizationsId, rolesId` | Gets the definition of a Role. |
| `organizations_roles_list` | `SELECT` | `organizationsId` | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| `projects_roles_get` | `SELECT` | `projectsId, rolesId` | Gets the definition of a Role. |
| `projects_roles_list` | `SELECT` | `projectsId` | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| `organizations_roles_create` | `INSERT` | `organizationsId` | Creates a new custom Role. |
| `projects_roles_create` | `INSERT` | `projectsId` | Creates a new custom Role. |
| `organizations_roles_delete` | `DELETE` | `organizationsId, rolesId` | Deletes a custom Role. When you delete a custom role, the following changes occur immediately: * You cannot bind a principal to the custom role in an IAM Policy. * Existing bindings to the custom role are not changed, but they have no effect. * By default, the response from ListRoles does not include the custom role. You have 7 days to undelete the custom role. After 7 days, the following changes occur: * The custom role is permanently deleted and cannot be recovered. * If an IAM policy contains a binding to the custom role, the binding is permanently removed. |
| `projects_roles_delete` | `DELETE` | `projectsId, rolesId` | Deletes a custom Role. When you delete a custom role, the following changes occur immediately: * You cannot bind a principal to the custom role in an IAM Policy. * Existing bindings to the custom role are not changed, but they have no effect. * By default, the response from ListRoles does not include the custom role. You have 7 days to undelete the custom role. After 7 days, the following changes occur: * The custom role is permanently deleted and cannot be recovered. * If an IAM policy contains a binding to the custom role, the binding is permanently removed. |
| `organizations_roles_patch` | `EXEC` | `organizationsId, rolesId` | Updates the definition of a custom Role. |
| `organizations_roles_undelete` | `EXEC` | `organizationsId, rolesId` | Undeletes a custom Role. |
| `projects_roles_patch` | `EXEC` | `projectsId, rolesId` | Updates the definition of a custom Role. |
| `projects_roles_undelete` | `EXEC` | `projectsId, rolesId` | Undeletes a custom Role. |
| `queryGrantableRoles` | `EXEC` |  | Lists roles that can be granted on a Google Cloud resource. A role is grantable if the IAM policy for the resource can contain bindings to the role. |
