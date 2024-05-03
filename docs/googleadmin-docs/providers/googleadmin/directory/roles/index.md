---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="isSuperAdminRole" /> | `boolean` | Returns `true` if the role is a super admin role. |
| <CopyableCode code="isSystemRole" /> | `boolean` | Returns `true` if this is a pre-defined system role. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. This is always `admin#directory#role`. |
| <CopyableCode code="roleDescription" /> | `string` | A short description of the role. |
| <CopyableCode code="roleId" /> | `string` | ID of the role. |
| <CopyableCode code="roleName" /> | `string` | Name of the role. |
| <CopyableCode code="rolePrivileges" /> | `array` | The set of privileges that are granted to this role. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customer, roleId" /> | Retrieves a role. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer" /> | Retrieves a paginated list of all the roles in a domain. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Creates a role. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customer, roleId" /> | Deletes a role. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customer, roleId" /> | Patches a role. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="customer, roleId" /> | Updates a role. |
