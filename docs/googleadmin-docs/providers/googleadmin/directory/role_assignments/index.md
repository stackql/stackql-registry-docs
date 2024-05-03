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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.role_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assignedTo" /> | `string` | The unique ID of the entity this role is assigned to—either the `user_id` of a user, the `group_id` of a group, or the `uniqueId` of a service account as defined in [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts). |
| <CopyableCode code="assigneeType" /> | `string` | Output only. The type of the assignee (`USER` or `GROUP`). |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. This is always `admin#directory#roleAssignment`. |
| <CopyableCode code="orgUnitId" /> | `string` | If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this role is restricted to. |
| <CopyableCode code="roleAssignmentId" /> | `string` | ID of this roleAssignment. |
| <CopyableCode code="roleId" /> | `string` | The ID of the role that is assigned. |
| <CopyableCode code="scopeType" /> | `string` | The scope in which this role is assigned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customer, roleAssignmentId" /> | Retrieves a role assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer" /> | Retrieves a paginated list of all roleAssignments. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Creates a role assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customer, roleAssignmentId" /> | Deletes a role assignment. |
