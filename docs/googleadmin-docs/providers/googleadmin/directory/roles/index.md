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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rolePrivileges` | `array` | The set of privileges that are granted to this role. |
| `etag` | `string` | ETag of the resource. |
| `isSuperAdminRole` | `boolean` | Returns `true` if the role is a super admin role. |
| `isSystemRole` | `boolean` | Returns `true` if this is a pre-defined system role. |
| `kind` | `string` | The type of the API resource. This is always `admin#directory#role`. |
| `roleDescription` | `string` | A short description of the role. |
| `roleId` | `string` | ID of the role. |
| `roleName` | `string` | Name of the role. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customer, roleId` | Retrieves a role. |
| `list` | `SELECT` | `customer` | Retrieves a paginated list of all the roles in a domain. |
| `insert` | `INSERT` | `customer` | Creates a role. |
| `delete` | `DELETE` | `customer, roleId` | Deletes a role. |
| `patch` | `EXEC` | `customer, roleId` | Patches a role. |
| `update` | `EXEC` | `customer, roleId` | Updates a role. |
