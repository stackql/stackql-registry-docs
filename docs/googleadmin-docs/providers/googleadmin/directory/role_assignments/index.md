---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.role_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `roleId` | `string` | The ID of the role that is assigned. |
| `scopeType` | `string` | The scope in which this role is assigned. |
| `assignedTo` | `string` | The unique ID of the entity this role is assigned to—either the `user_id` of a user, the `group_id` of a group, or the `uniqueId` of a service account as defined in [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts). |
| `assigneeType` | `string` | Output only. The type of the assignee (`USER` or `GROUP`). |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | The type of the API resource. This is always `admin#directory#roleAssignment`. |
| `orgUnitId` | `string` | If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this role is restricted to. |
| `roleAssignmentId` | `string` | ID of this roleAssignment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customer, roleAssignmentId` | Retrieves a role assignment. |
| `list` | `SELECT` | `customer` | Retrieves a paginated list of all roleAssignments. |
| `insert` | `INSERT` | `customer` | Creates a role assignment. |
| `delete` | `DELETE` | `customer, roleAssignmentId` | Deletes a role assignment. |
